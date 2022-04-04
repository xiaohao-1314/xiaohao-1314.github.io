#!/usr/bin/env python
# encoding: utf-8
'''
@author: ouyanting
@contact: oyt@ouyanting.com
@file: index.py
@time: 2020/3/14
@desc:
'''

import os
import shutil
import re

path = "source/_posts"
pattern = r'date: (\d{4})-(\d{2})-(\d{2})'

os.chdir(path)
file_list = os.listdir("./")

# 创建文件夹
def creatDir(path, nextPath):
  # 判断是否有该文件夹，没有则创建
  if not os.path.exists(path):
    os.mkdir(path)
  
  # 判断是否需要继续创建
  if nextPath:
    creatDir(path + "/" + nextPath, False)

def moveFile(file_path, dic_path):
  shutil.copy(file_path, dic_path)

def getAllFile():
  # 循环所有文件（夹）
  for file_name in file_list:
    # 判断是否是文件
    if os.path.isfile(file_name):
      # 打开文件
      with open(file_name, 'r', encoding='UTF-8') as f:
        # 读取文件内容
        contents = f.read()
        # print(contents)
        line = re.search(pattern, contents)
        if line is not None:
          year = line.group(1) 
          month = line.group(2) 

          creatDir(year, month)

          begin = os.getcwd() + "/" + file_name
          end = os.getcwd() + "/" + year + "/" + month
          print(file_name, os.getcwd())
          moveFile(begin,  end)

getAllFile()