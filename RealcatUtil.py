import os
import random
import string

def getRandFileName(bin):
    ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 8))
    return os.path.basename(bin) + "_" + ran_str