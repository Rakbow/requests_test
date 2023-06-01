import csv
import json

import pandas as pd
from requests_test import get_dict_for_html_text

keys = ['id', '名称', '职业', '简体中文名', '别名', '性别', '生日', '血型', '身高', '星座', '出身地区', '所属公司', '引用来源',
        '个人状态', '官网', 'FanClub', 'Twitter', 'Facebook']


def write_dict_to_csv(start, end):
    csv_path = 'person.csv'

    with open(csv_path, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        data = list(reader)

    for i in range(start, end):
        new_data: dict = get_dict_for_html_text(i)

        insert_data = []

        for key in keys:
            current_data = new_data.get(key)

            if type(current_data) == list:
                if len(current_data) == 1:
                    insert_data.append(str(current_data[0]))
                elif len(current_data) > 1:
                    str_tmp = json.dumps(current_data, ensure_ascii=False)
                    insert_data.append(str_tmp)
                else:
                    insert_data.append('')
            else:
                insert_data.append(current_data)

        # 将数据添加到 CSV 文件的最后一行
        data.append(insert_data)

    # 将更新后的数据写入 CSV 文件中
    with open(csv_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_NONE, escapechar='\\')
        writer.writerows(data)


def csv_to_excel(csv_path):

    # 读取CSV文件数据
    df = pd.read_csv(csv_path, encoding='utf-8', quoting=csv.QUOTE_ALL, escapechar='\\')

    # 将数据保存为Excel文件
    df.to_excel('person.xlsx', index=False)
