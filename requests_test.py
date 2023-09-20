import random
import time

import requests  # 导库
from bs4 import BeautifulSoup

from requests_tool import get_random_date_str
from file_tools import open_text, write_list_to_file

common_property_list = [
    '简体中文名: ',
    '别名: ',
    '性别: ',
    '生日: ',
    '血型: ',
    '身高: ',
    '星座: ',
    '出身地区: ',
    '所属公司: ',
    '引用来源: ',
    '个人状态: ',
    '官网: ',
    'FanClub: ',
    'Twitter: ',
    'Facebook: '
]

special_property_list = [
    '职业: ',
]


# 获取html页面文本
def get_html_text(url):
    param = {
        'Connection': 'close',
        'Content-Encoding': 'gzip',
        'Content-Type': 'text/html',
        'Server': 'nginx',
        'Transfer-Encoding': 'chunked',
        'Vary': 'Accept-Encoding'
    }
    header = {'Content-Type': 'text/html; charset=utf-8'}
    user_agent_list = [
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.5; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15",
    ]
    header['User-Agent'] = random.choice(user_agent_list)
    param['Date'] = get_random_date_str()
    r = requests.get(url, params=param, headers=header, timeout=30)
    r.raise_for_status()  # 如果状态不是200，引发HTTPError异常
    r.encoding = r.apparent_encoding  # 因为apparent更准确
    return r.text


def get_dict_for_html_text(i):
    file_content = open_text(i)
    res_dict = {'id': i}

    # 解析HTML代码
    html_code = BeautifulSoup(file_content, 'html.parser')

    # 固定属性
    for common_property in common_property_list:
        span_list = []
        spans = html_code.find_all("span", string=common_property)
        for span in spans:
            if span:
                span_list.append(span.parent.text.replace(common_property, '').strip())
        res_dict[common_property.replace(':', '').strip()] = span_list

    # 职业
    h2s = html_code.find_all('h2', {'class': 'subtitle'})
    for h2 in h2s:
        if h2.text.find('职业:') != -1:
            res_dict['职业:'.replace(':', '').strip()] = h2.text.replace('职业:', '').strip().split('    ')

    # 原名
    h1s = html_code.find_all('h1', {'class': 'nameSingle'})
    for h1 in h1s:
        res_dict['名称'] = h1.find('a').text

    return res_dict


def get_person_html_text(start, end):
    base_url = 'https://bangumi.tv/person/{}'
    file_name = 'person_{}.txt'
    save_html_path = './html'
    error_file_no_list = []
    for i in range(start, end):
        try:
            # 尝试进行操作，可能会抛出异常
            url = base_url.format(i)
            html_text = get_html_text(url)
            with open(f'{save_html_path}/' + file_name.format(i), 'w+', encoding='utf-8') as file:
                file.write(html_text)
            time.sleep(random.randint(1, 4))
            print('========={}/{}========='.format(i, end))
        except ValueError:
            # 如果遇到异常（这里是值错误），捕获并输出消息
            print('========={}获取失败========='.format(i))
            error_file_no_list.append(i)
            continue

    write_list_to_file(error_file_no_list, save_html_path + '')



