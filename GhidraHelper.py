import json
import os
import platform
import RealcatUtil
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

#解析GHIDRA的XML文件，获得函数列表
def xml_parse(outxml):
    func_list = []
    tree = ET.ElementTree(file=outxml)
    root = tree.getroot()
    for child in root:
        if child.tag == 'function':
            addr = child.attrib['address']
            name = ''
            returntype = ''
            arglist = []

            #去掉开头注释
            text = RealcatUtil.c_comment_trim(child.text)
            #解析函数名，找左大括号
            left_bracket = text.find('{')
            if left_bracket != -1:
                func_declare = text[0:left_bracket].rstrip()
                l = func_declare.find('(')
                if l != -1:
                    return_type_flag = func_declare[0:l].rstrip()
                    p = return_type_flag.rfind(' ')
                    if p != -1:
                        name = return_type_flag[p:].strip()
                        returntype = return_type_flag[0:p].strip()
                    else:
                        p = return_type_flag.rfind('\n')
                        if p != -1:
                            name = return_type_flag[p:].strip()
                            returntype = return_type_flag[0:p].rstrip()
                    #if name == '':
                    #    print(return_type_flag)
                    #    print(text)
                    #    exit(1)
                    r = func_declare.rfind(')')
                    if r != -1:
                        args = func_declare[l+1 : r]
                        arglist = args.split(',')
            f = {
                "name":name,
                "address":addr,
                "src_code":text,
                "args" : arglist,
                "return_type":returntype
            }
            #print(f)
            func_list.append(f)
    return func_list

def disass(bin):
    config = json.loads(RealcatUtil.readFile('config.json'))
    GHIDRA_HOME = os.path.join(os.getcwd(), 'ghidra_' + config['GHIDRA_VERSION'] + '_PUBLIC')
    POST_SCRIPT_NAME = "RealcatDecompile.java"
    SCRIPT_PATH_VALUE = os.getcwd()
    __projects_path = os.path.join(GHIDRA_HOME, 'ghidra_projects')
    try:
        os.mkdir(__projects_path)
    except:
        pass
    os_platform = platform.platform()
    outxml = RealcatUtil.getRandFileName(bin) + ".xml"
    cmd = ''
    if os_platform.find("Linux") == 0:
        __headless_path = os.path.join(GHIDRA_HOME, 'support/analyzeHeadless')
    elif os_platform.find("Windows") == 0:
        __headless_path = os.path.join(GHIDRA_HOME, 'support/analyzeHeadless.bat')
    else:
        raise Exception('unsupported platform')
    cmd = ' '.join([__headless_path,  __projects_path, "ANewProject", "-readOnly", '-scriptPath', SCRIPT_PATH_VALUE, '-postScript', POST_SCRIPT_NAME, outxml, '-import', bin])
    print(cmd)
    if os.system(cmd) == 0:
        func_list = []
        try:
            func_list = xml_parse(outxml)
        except Exception as e:
            raise e
        finally:
            os.unlink(outxml)
        return func_list
    else:
        raise Exception('execute cmd %s fail' % cmd)

#print(disass('Z:\\ctf'))
