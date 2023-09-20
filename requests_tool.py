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

