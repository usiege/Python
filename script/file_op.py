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
