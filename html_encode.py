#!/usr/bin/env python
# encoding: utf-8
# @Time      :2023/9/20 1:10
# @Author    :Rakbow
# @File      :html_encode.py

import os
import chardet

from file_tools import open_text


def encode_html(i):
    # 指定目录
    dir_path = './html'
    # 指定文件名和扩展名
    file_name = 'person_{}.txt'.format(i)
    print(file_name)
    file_content = ''

    # 遍历目录下所有文件名
    for filename in os.listdir(dir_path):
        # 判断是否是指定文件名和扩展名的文件
        if filename.startswith(file_name):
            # 打开文件并读取内容
            with open(os.path.join(dir_path, filename), 'r', encoding='utf-8') as f:
                file_content = f.read()

    possible_encodings = ['utf-8', 'ISO-8859-1', 'gbk', 'cp1252']

    decoded_string = None

    for encoding in possible_encodings:
        try:
            decoded_string = file_content.encode(encoding).decode('utf-8')
            break
        except UnicodeDecodeError:
            continue

    if decoded_string is not None:
        print("解码成功:", decoded_string)
    else:
        print("无法解码字符串")


def is_malformed(text):
    # 检测字符串的编码
    result = chardet.detect(text.encode())

    # 获取编码和可信度
    encoding = result['encoding']
    confidence = result['confidence']

    # 判断编码是否为ASCII以外的编码，并且可信度低于某个阈值（例如0.9）
    if encoding.lower() != 'ascii' and confidence < 0.9:
        return True
    else:
        return False

def is_no_normal(text):
    if 'ç•ªç»„è®¡å' in text:
        return True
    else:
        return False

def check_encode(start, end):
    file_path = './file/no_normal_id.txt'

    tmp = []

    for i in range(start, end + 1):
        print('========={}/{}========='.format(i, end))
        if is_no_normal(open_text(i)):
            tmp.append(i)

    with open(file_path, 'w') as file:
        for number in tmp:
            file.write(str(number) + '\n')