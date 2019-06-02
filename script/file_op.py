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


# ----------------------      file store       ------------------------ #
# json
import json
def json_read(path='/name.json'):
    with open(path, 'r') as f:
        jsobj = json.loads(f.read())
        # 另外一种方式
        jsobj = json.load(f)

def json_save(path="/path/name.json"):
    dic = {}
    with open(path, 'w') as f:
        jsobj = json.dumps(dic, sort_keys=True, indent=4, separators=(',', ':'))
        f.write(jsobj)
        f.close()

        # 另外个一种方式
        json.dump(dic, f)

# xml

# txt

# csv
#######
import csv

def read():
    reader = csv.reader(open("path", encoding='utf-8'))
    for row in reader:
        print(row)

def write():
    out = open(path, 'w')
    writer = csv.writer(out)
    writer.writerow(["1", "2"])
