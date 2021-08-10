import os
import platform
import RealcatUtil

GHIDRA_HOME = 'D:\\ghidra_9.1.2_PUBLIC'
POST_SCRIPT_ENABLED = "-postScript"
#POST_SCRIPT_NAME="DecompileHeadless.java"
POST_SCRIPT_NAME = "RealcatDecompile.java"
SCRIPT_PATH = "-scriptPath"
SCRIPT_PATH_VALUE = GHIDRA_HOME + "/Ghidra/Features/Decompiler/ghidra_scrips"

def disass(bin):
    __projects_path = GHIDRA_HOME + '/ghidra_projects'
    try:
        os.mkdir(__projects_path)
    except:
        pass
    os_platform = platform.platform()
    outxml = RealcatUtil.getRandFileName(bin) + ".xml"
    cmd = ''
    if os_platform.find("Linux") == 0:
        __headless_path = GHIDRA_HOME + '/support/analyzeHeadless'
    elif os_platform.find("Windows") == 0:
        __headless_path = GHIDRA_HOME + '/support/analyzeHeadless.bat'
    else:
        raise Exception('unsupported platform')
    cmd = __headless_path + " " + __projects_path + " ANewProject -readOnly " + POST_SCRIPT_ENABLED + " " + POST_SCRIPT_NAME + " " + outxml + " " + SCRIPT_PATH + " " + SCRIPT_PATH_VALUE
    cmd += " -import " + bin
    print(cmd)
    if os.system(cmd) == 0:
        return outxml
    else:
        raise Exception('execute cmd %s fail' % cmd)

#print(disass('Z:\\ctf'))
