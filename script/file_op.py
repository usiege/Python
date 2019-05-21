# file operation

import os
import sys

def file_walk(dir):

    for root, dirs, files in os.walk(dir):
        print(root) # current root
        print(dirs) # under root all dirs
        print(files) # under root all files


def file_list(dir):

    for file in os.listdir(dir):
        print(file) # list under dir


# file store
# json
import json

def json_save(path="/path/name.json"):
    dic = {}
    with open(path, 'w') as f:
        jsobj = json.dumps(dic, sort_keys=True, indent=4, separators=(',', ':'))
        f.write(js)
        f.close()


# xml

# txt
