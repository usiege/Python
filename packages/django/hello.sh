#!/bin/bash -l

#这是一个bash shell脚本

export DEBUG=on
export ALLOWED_HOSTS=localhost,example.com
python3 hello.py runserver

#删除环境变量
#unset DEBUG

: '
这是一个多行注释
注意冒号后边有空格
'
echo DEBUG
echo ALLOWED_HOSTS

# 通过使用startproject使用模板
# django-admin.py startproject foo --template=project_name
# pip install Pillow

#打开python安装模块路径
open /usr/local/lib/python3.6/site-packages