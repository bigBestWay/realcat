#coding=utf-8
from androguard.core.bytecodes.apk import APK
from androguard.core.bytecodes.dvm import DalvikVMFormat
from androguard.core.analysis.analysis import Analysis
from androguard.decompiler.decompiler import DecompilerDAD
from androguard.core.androconf import show_logging
import logging
from androguard.misc import AnalyzeAPK
import sys
# Enable log output
#show_logging(level=logging.DEBUG)

class ActivityInfo:
    def __init__(self, name):
        self.name = name
        self.package_name = ''
        self.permission = ''
        self.deeplinks = []

    def __set_package_name__(self, package_name):
        self.package_name = package_name

    def __get_package_name__(self):
        return self.package_name

    def __set_name__(self, name):
        self.name = name

    def __get_name__(self):
        return self.name

    def __set_permission__(self, permission):
        self.permission = permission

    def __get_permission__(self):
        return self.permission

    def __get_deeplinks__(self):
        return self.deeplinks

    def __set_deeplinks__(self, urls):
        self.deeplinks = urls

#返回方法对象
def find_jsbridge_method(dvm):
    methods = []
    for adi in dvm.map_list.get_item_type("TYPE_ANNOTATIONS_DIRECTORY_ITEM"):
        if adi.get_method_annotations() == []:
            continue

        # Each annotations_directory_item contains many method_annotation
        for mi in adi.get_method_annotations():
            method = dvm.get_method_by_idx(mi.get_method_idx())
            # Each method_annotation stores an offset to annotation_set_item
            ann_set_item = dvm.CM.get_obj_by_offset(mi.get_annotations_off())
            # a annotation_set_item has an array of annotation_off_item
            for aoffitem in ann_set_item.get_annotation_off_item():
                # The annotation_off_item stores the offset to an annotation_item
                annotation_item = dvm.CM.get_obj_by_offset(aoffitem.get_annotation_off())
                # The annotation_item stores the visibility and a encoded_annotation
                # this encoded_annotation stores the type IDX, and an array of
                # annotation_element
                # these are again name idx and encoded_value's
                encoded_annotation = annotation_item.get_annotation()
                # Print the class type of the annotation
                annotation_class_name = dvm.CM.get_type(encoded_annotation.get_type_idx())
                if annotation_class_name == "Landroid/webkit/JavascriptInterface;":
                    methods.append(method)

                #for annotation_element in encoded_annotation.get_elements():
                #    print("   {} = {}".format(
                #        dvm.CM.get_string(annotation_element.get_name_idx()),
                        # Read the EncodedValue and then the real value - which is again some object...
                #        annotation_element.get_value().get_value(),
                #    ))
    return methods
#com.myapplicaption.example -> Lcom/myapplicaption/example
def class2path(name):
    name = name.replace('..', '/')
    name = name.replace('.', '/')
    return 'L' + name + ';'
#获取导出的browsable activity
def find_browsable_activitis(apk):
    namespace = '{http://schemas.android.com/apk/res/android}'
    xml = apk.get_android_manifest_axml().get_xml_obj()
    packagename = xml.attrib["package"]
    application = xml.find("application")

    exported_activities = []
    for activity in application:
        intent_filters = activity.findall("intent-filter")
        if intent_filters is None:
            break

        isActivityBrowsable = False
        urls = []
        for filter in intent_filters:
            actions = filter.findall('action')
            categorys = filter.findall('category')
            if actions is None or categorys is None:
                continue
            hasViewAction = False
            for action in actions:
                if "android.intent.action.VIEW" == action.attrib[namespace + "name"]:
                    hasViewAction = True
                    break
            hasBrowsableCateg = False
            for categ in categorys:
                if "android.intent.category.BROWSABLE" == categ.attrib[namespace + "name"]:
                    hasBrowsableCateg = True
                    break
            if hasBrowsableCateg is not True or hasViewAction is not True:
                continue

            isActivityBrowsable = True
            #一个intent_filter里有多条data, 一条data一个URL
            datas = filter.findall('data')
            if datas is None:
                continue
            for data in datas:
                scheme = data.attrib.get(namespace + 'scheme', None)
                if scheme is None:
                    continue
                host = data.attrib.get(namespace + 'host', None)
                port = data.attrib.get(namespace + 'port', None)
                path = data.attrib.get(namespace + 'path', None)
                pathPrefix = data.attrib.get(namespace + 'pathPrefix', None)
                pathPattern = data.attrib.get(namespace + 'pathPattern', None)
                mimetype = data.attrib.get(namespace + 'mimeType', None)
                url = scheme + '://'
                if host is not None:
                    url += host
                else:
                    url += '*'
                if port is not None:
                    url += ':' + port
                if path is not None:
                    url += path
                elif pathPattern is not None:
                    url += pathPattern
                elif pathPrefix is not None:
                    url += pathPrefix + '*'
                if mimetype is not None:
                    url = 'mimeType=' + mimetype + ", " + url
                urls.append(url)

        if isActivityBrowsable is not True:
            continue

        activity_name = activity.attrib[namespace + 'name']
        exported = activity.attrib.get(namespace + 'exported', 'true')
        if exported == 'true':
            exported_activity = ActivityInfo(activity_name)
            exported_activity.__set_package_name__(packagename)
            permission = activity.attrib.get(namespace + 'permission', None)
            if permission is not None:
                exported_activity.__set_permission__(permission)
            exported_activity.__set_deeplinks__(urls)
            exported_activities.append(exported_activity)
    return  exported_activities

#检测当前dex是否加壳
#如果存在动态插件加载的情况，也会导致Manifest.xml声明但DEX中没有，所以做一个阈值比较
def check_dex_packed(apk, dvms):
    classe_names = []
    for dvm in dvms:
        for clazz in dvm.get_classes():
            classe_names.append(clazz.get_name())
    not_found_count = 0
    total_count = 0
    for activity in apk.get_activities():
        name = class2path(activity)
        total_count += 1
        if name not in classe_names:
            #print("activity " + name + " not found in DEX.")
            not_found_count += 1
    percent = not_found_count/total_count
    #80%都没找到，肯定是加壳了
    #print(percent)
    if percent >= 0.8:
        return True
    return False

def print_activity_info(activitys):
    print("++++++ Browsable activities:")
    for activity in activitys:
        print("package: " + activity.__get_package_name__())
        print("name: " + activity.__get_name__())
        permisson = activity.__get_permission__()
        if len(permisson) > 0:
            print("permission: " + activity.__get_permission__())
        for url in activity.__get_deeplinks__():
            print("deeplink: " + url)
        print("----------------------------------")
    print("++++++ End")

if __name__=="__main__":
    if len(sys.argv) < 2:
        print("RealCat <apkfile>")
        exit(1)

    apkfile = sys.argv[1]
    a = APK(apkfile)
    exported_activities = find_browsable_activitis(a)
    if len(exported_activities) == 0:
        print("*** No exported BROWSABLE activity ***")
        exit(0)

    print_activity_info(exported_activities)

    print("Working...")
    a,d,dx = AnalyzeAPK(apkfile)
    if check_dex_packed(a, d) == True:
        print("**************************************")
        print("**** Warning:APK Dex maybe packed ****")
        print("**************************************")

    print ("\n++++++ JavascriptInterface:")
    for dex in d:
        try:
            methods = find_jsbridge_method(dex)
            for method in methods:
                print(method.get_class_name())
                src_code = method.get_source()
                print(src_code)
                print("----------------------------------")
        except Exception as e:
            print(str(e))
    print("++++++ End")