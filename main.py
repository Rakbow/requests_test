import random
import time

from file_tools import txt_file_to_number_list, delete_file
from requests_test import get_html_text


# def do(start, end):
#     write_dict_to_csv(start, end)


# csv_to_excel('person.csv')

# get_person_html_text(9999, 10000)

def test():
    tmp_list = txt_file_to_number_list('./file/no_normal_id.txt')
    base_url = 'https://bangumi.tv/person/{}'
    file_name = 'person_{}.txt'
    save_html_path = './html'
    error_file_no_list = []
    for i in tmp_list:
        try:
            # 尝试进行操作，可能会抛出异常
            url = base_url.format(i)
            html_text = get_html_text(url)
            with open(f'{save_html_path}/' + file_name.format(i), 'w+', encoding='utf-8') as file:
                file.write(html_text)
            time.sleep(random.randint(1, 4))
            print('========={}/{}========='.format(i, len(tmp_list)))
        except ValueError:
            # 如果遇到异常（这里是值错误），捕获并输出消息
            print('========={}获取失败========='.format(i))
            error_file_no_list.append(i)
            continue

    print(error_file_no_list)


test()