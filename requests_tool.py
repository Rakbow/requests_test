import os
import random
from datetime import datetime, timedelta


def get_random_date_str():
    # 指定时间范围
    year = random.randint(2021, 2024)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    start_time = datetime(year, month, day)
    end_time = start_time + timedelta(days=random.randint(1, 365))

    # 生成随机时间戳
    time_diff = end_time - start_time
    random_time = start_time + timedelta(seconds=random.randint(0, int(time_diff.total_seconds())))

    # 将时间戳转换为指定格式的时间字符串
    time_string = random_time.strftime('%a, %d %b %Y %H:%M:%S GMT')
    return time_string


def open_text(i):
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

    return file_content
