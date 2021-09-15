#coding=utf-8
import getopt
import json
import os
import traceback
from enum import Enum

from androguard.core.bytecodes.apk import APK
from androguard.core.bytecodes.dvm import DalvikVMFormat
from androguard.core.analysis.analysis import Analysis
from androguard.decompiler.decompiler import DecompilerDAD
from androguard.core.androconf import show_logging
import logging
from androguard.misc import AnalyzeAPK
import sys
import GhidraHelper
import RealcatUtil
# Enable log output
#show_logging(level=logging.DEBUG)

Component = Enum("Component", ('Activity','Service','ContentProvider','BroadcastReceiver'))
ARCH = Enum("ARCH", ('x86', 'x86_64', 'arm64-v8a', 'armeabi', 'armeabi-v7a'))

class ComponentInfo:
    def __init__(self, name):
        self.type = None
        self.name = name
        self.package_name = ''
        self.permission = ''
        self.deeplinks = []
        self.browsable = None

    def __set_type__(self, type):
        self.type = type

    def __get_type__(self):
        return self.type

    def __set_browsable__(self, flag):
        self.browsable = flag

    def __get_browsable__(self):
        return self.browsable

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
        if len(adi.get_method_annotations()) == 0:
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

def find_exported_coms(apk):
    namespace = '{http://schemas.android.com/apk/res/android}'
    xml = apk.get_android_manifest_axml().get_xml_obj()
    packagename = xml.attrib["package"]
    application = xml.find("application")

    exported_coms = []
    for element in application:
        type = None
        if element.tag == 'activity':
            type = Component.Activity
        elif element.tag == 'provider':
            type = Component.ContentProvider
        elif element.tag == 'service':
            type = Component.Service
        elif element.tag == 'receiver':
            type = Component.BroadcastReceiver
        else:
            continue

        intent_filters = element.findall("intent-filter")
        urls = []
        isActivityBrowsable = False

        if type == Component.Activity:
            for intentfilter in intent_filters:
                actions = intentfilter.findall('action')
                categorys = intentfilter.findall('category')
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
                if hasBrowsableCateg is True and hasViewAction is True:
                    isActivityBrowsable = True
                # 一个intent_filter里有多条data, 一条data一个URL
                datas = intentfilter.findall('data')
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

        exported = element.attrib.get(namespace + 'exported')
        activity_name = element.attrib[namespace + 'name']
        is_activity_exported = False
        if exported is None and intent_filters is not None:
            is_activity_exported = True
        elif exported == 'true':
            is_activity_exported = True

        if is_activity_exported is True:
            exported_com = ComponentInfo(activity_name)
            exported_com.__set_type__(type)
            exported_com.__set_package_name__(packagename)
            permission = element.attrib.get(namespace + 'permission', None)
            if permission is not None:
                exported_com.__set_permission__(permission)
            if type == Component.Activity:
                exported_com.__set_deeplinks__(urls)
                exported_com.__set_browsable__(isActivityBrowsable)
            exported_coms.append(exported_com)
    return exported_coms

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

def add_components_result(dict, Components):
    activitys = []
    services = []
    receivers = []
    providers = []
    for com in Components:
        if dict.get('package_name', None) == None:
            dict['package_name'] = com.__get_package_name__()
        if com.__get_type__() == Component.Activity:
            e = {}
            e['name'] = com.__get_name__()
            if com.__get_permission__() != '':
                e['permission'] = com.__get_permission__()
            if len(com.__get_deeplinks__()) != 0:
                e['deeplinks'] = com.__get_deeplinks__(),
            e['browsable'] = com.__get_browsable__()
            activitys.append(e)
        elif com.__get_type__() == Component.Service:
            e = {}
            e['name'] = com.__get_name__()
            if com.__get_permission__() != '':
                e['permission'] = com.__get_permission__()
            services.append(e)
        elif com.__get_type__() == Component.ContentProvider:
            e = {}
            e['name'] = com.__get_name__()
            if com.__get_permission__() != '':
                e['permission'] = com.__get_permission__()
            providers.append(e)
        elif com.__get_type__() == Component.BroadcastReceiver:
            e = {}
            e['name'] = com.__get_name__()
            if com.__get_permission__() != '':
                e['permission'] = com.__get_permission__()
            receivers.append(e)

    dict['activity'] = activitys
    dict['service'] = services
    dict['ContentProvider'] = providers
    dict['BroadcastReceiver'] = receivers
    return dict

def add_jsbridge_result(dict, methods):
    method_json = []
    for method in methods:
        print(method.get_class_name())
        src_code = method.get_source()
        m = {
            "class": method.get_class_name(),
            "method": method.get_name() + method.get_descriptor(),
            "src_code": method.get_source()
        }
        method_json.append(m)
        print(src_code)
        print("----------------------------------")
    dict['JavascriptInterface'] = method_json
    return dict

def print_com_info(components):
    print("++++++ Exported Components:")
    for com in components:
        print("package: " + com.__get_package_name__())
        print("type: " + str(com.__get_type__()))
        print("name: " + com.__get_name__())
        permisson = com.__get_permission__()
        if len(permisson) > 0:
            print("permission: " + com.__get_permission__())
        if com.__get_browsable__() is not None:
            print("browsable: " + str(com.__get_browsable__()))
        for url in com.__get_deeplinks__():
            print("deeplink: " + url)
        print("----------------------------------")
    print("++++++ End")

def find_native_method(dx):
    methods = []
    for method in dx.get_methods():
        m = method.get_method()
        access_str = m.get_access_flags_string()
        #print(access_str)
        if access_str.find('native') != -1:
            methods.append(m)
    return methods

def get_so_functions(apk):
    so_functions = {}
    libs = {}
    for f in apk.get_files():
        if f.endswith('.so') is True:
            # 多架构下同一个库选择一个
            splits = f.split('/')
            # lib/x86/liblocSDK6a.so
            if len(splits) != 3:
                continue
            arch = splits[1]
            libname = splits[2]
            libs[libname] = f

    for k in libs.keys():
        rawdata = apk.get_file(libs[k])
        if len(rawdata) == 0:
            continue
        print('------- Disass ' + k);
        tmpPath = RealcatUtil.createTmpFile(rawdata)
        try:
            func_list = GhidraHelper.disass(tmpPath)
            #print(func_list)
            for func in func_list:
                if func['name'].startswith('Java_'):
                    print(func['name'])
            so_functions[k] = func_list
        except Exception as e:
            #raise e
            traceback.format_exc()
        finally:
            if os.path.exists(tmpPath):
                os.unlink(tmpPath)
    return so_functions

def usage():
    print("RealCat [OPTION] -i <apkfile> -o [projectdir]")
    print("OPTION: \n\t -j: use GHIDRA to recompile so.")

if __name__ == "__main__":
    opts, args = getopt.getopt(sys.argv[1:], "hji:o:", ["help", "jni", "input=", "output="])
    proj_dir = '.'
    apkfile = ''
    is_use_ghidra = False
    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-o", "--output"):
            proj_dir = a
        elif o in ("-i", "--input"):
            apkfile = a
        elif o in ("-j", "--jni"):
            is_use_ghidra = True
        else:
            usage()
            sys.exit()

    if len(apkfile) == 0:
        usage()
        exit(1)

    report_json = {}
    outjson = proj_dir + '/' + RealcatUtil.getRandFileName(apkfile) + ".json"

    apk = APK(apkfile)
    exported_coms = find_exported_coms(apk)
    if len(exported_coms) == 0:
        print("*** No exported activity ***")
    else:
        print_com_info(exported_coms)
        report_json = add_components_result(report_json, exported_coms)

    print("Working...")
    apk, d, dx = AnalyzeAPK(apkfile)

    if check_dex_packed(apk, d) is True:
        print("**************************************")
        print("**** Warning:APK Dex maybe packed ****")
        print("**************************************")

    jni_methods = []
    #反编译so
    so_functions = {}
    if is_use_ghidra is True:
        so_functions = get_so_functions(apk)
    print("\n++++++ Native Methods:")
    native_methods = find_native_method(dx)
    for m in native_methods:
        jni_name = RealcatUtil.java_method2jni_name(m.get_class_name(), m.get_name())
        func_obj = {
            'class':m.get_class_name(),
            'method':m.get_name() + m.get_descriptor()
        }
        for so in so_functions.keys():
            for func in so_functions.get(so):
                if func.get('name', None) == jni_name:
                    func_obj['jni_lib'] = so
                    func_obj['address'] = func['address']
                    func_obj['src_code'] = func['src_code']
        print(m.get_class_name() + " -> " + m.get_name() + m.get_descriptor())
        jni_methods.append(func_obj)
    report_json['jni_method'] = jni_methods
    print("++++++ End")

    print("\n++++++ JavascriptInterface:")
    js_methods = []
    for dex in d:
        try:
            methods = find_jsbridge_method(dex)
            js_methods += methods
        except Exception as e:
            print(str(e))
    report_json = add_jsbridge_result(report_json, js_methods)
    print("++++++ End")
    json_str = json.dumps(report_json, indent=4, sort_keys=True, ensure_ascii=False)
    RealcatUtil.writeFile(outjson, json_str)
    print("Report %s generated."%outjson)
