#!/usr/bin/env python
# encoding: utf-8
# @Time      :2023/9/20 22:58
# @Author    :Rakbow
# @File      :file_tools.py
import os


def delete_file(file_path: str):
    try:
        os.remove(file_path)
        print(f"文件 {file_path} 已成功删除。")
    except OSError as e:
        print(f"删除文件 {file_path} 时发生错误：{e}")


def write_list_to_file(number_list: list, file_path: str):
    with open(file_path, 'w') as file:
        for number in number_list:
            file.write(str(number) + '\n')


def open_text(dir_path: str, file_name: str):
    # 指定目录
    # dir_path = './html'
    # # 指定文件名和扩展名
    # file_name = 'person_{}.txt'.format(i)
    # print(file_name)
    file_content = ''

    # 遍历目录下所有文件名
    for filename in os.listdir(dir_path):
        # 判断是否是指定文件名和扩展名的文件
        if filename.startswith(file_name):
            # 打开文件并读取内容
            with open(os.path.join(dir_path, filename), 'r', encoding='utf-8') as f:
                file_content = f.read()

    return file_content


def txt_file_to_number_list(file_path: str):
    """
    从文本文件中读取每行的数字并返回一个数字列表。

    :param file_path: 包含数字的文本文件的路径
    :return: 包含读取数字的列表，如果文件不存在或包含无法转换为数字的行，则返回空列表
    """
    numbers = []
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            numbers = [int(line.strip()) for line in lines]
    except FileNotFoundError:
        print(f"文件 '{file_path}' 未找到。")
    except ValueError:
        print(f"文件 '{file_path}' 包含无法转换为数字的行。")
    return numbers
