import hashlib
import json
import os
import stat
import RealcatUtil

import wget
import zipfile
import shutil

GHIDRA_VER = {
    '10.0.2' : {
        'url' : 'https://github.com/NationalSecurityAgency/ghidra/releases/download/Ghidra_10.0.2_build/ghidra_10.0.2_PUBLIC_20210804.zip',
        'hash': '5534521ccb958b5cde04fc5c51bfa2918d475af49e94d372fa7c117cc9fe804b',
    },

    '9.1.2' : {
        'url':'https://github.com/NationalSecurityAgency/ghidra/releases/download/Ghidra_9.1.2_build/ghidra_9.1.2_PUBLIC_20200212.zip',
        'hash':'ebe3fa4e1afd7d97650990b27777bb78bd0427e8e70c1d0ee042aeb52decac61'
    }
}

def CalcFileSha256(filname):
    ''' calculate file sha256 '''
    with open(filname, "rb") as f:
        sha256obj = hashlib.sha256()
        sha256obj.update(f.read())
        hash_value = sha256obj.hexdigest()
        return hash_value

if __name__ == "__main__":
    INSTALL_VER = '9.1.2'
    ghidra_url = GHIDRA_VER[INSTALL_VER]['url']
    out_name =  os.path.basename(ghidra_url)
    hash = GHIDRA_VER[INSTALL_VER]['hash']
    GHIDRA_HOME = os.path.join(os.getcwd(), 'ghidra_' + INSTALL_VER + '_PUBLIC')
    if os.path.isfile(out_name) is not True:
        wget.download(ghidra_url, out=out_name)

    if CalcFileSha256(out_name) != hash:
        print("SHA256 check failed!!")
        exit(1)

    os.chmod(out_name, stat.S_IWRITE)
    if os.path.isfile(GHIDRA_HOME) is True:
        os.removedirs(GHIDRA_HOME)
    zfile = zipfile.ZipFile(out_name, "r")
    zfile.extractall()

    config_json = {
        'GHIDRA_VERSION' : INSTALL_VER
    }
    json_str = json.dumps(config_json, indent=4, sort_keys=True, ensure_ascii=False)
    RealcatUtil.writeFile('config.json', json_str)
    print("\nInstall Finish.")
