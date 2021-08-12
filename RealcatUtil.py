import os
import random
import string
from tempfile import NamedTemporaryFile


def getRandFileName(bin):
    ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 8))
    return os.path.basename(bin) + "_" + ran_str

def createTmpFile(rawdata):
    f = NamedTemporaryFile(mode='w+b', delete=False)
    f.write(rawdata)
    f.close()
    return f.name
#Lcom/baidu/location/Jni;
def java_method2jni_name(classPath, method_name):
    result = 'Java'
    splits = classPath[1:-1].split('/')
    for i in splits:
        result += '_' + i
    result += '_' + method_name
    return result

def c_comment_trim(s):
    news = s.lstrip()
    while news.startswith('//') is True:
        p = news.find('\n')
        if p != -1:
            news = news[p:]
        news = news.lstrip()
    return news

def writeFile(path, content):
    fo = open(path, "w")
    fo.write(content)
    fo.close()

def readFile(path):
    f = open(path, "r")
    content = f.read()
    f.close()
    return content
