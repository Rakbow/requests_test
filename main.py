from requests_file import write_dict_to_csv, csv_to_excel
from requests_test import get_dict_for_html_text, get_person_html_text


def do(start, end):
    write_dict_to_csv(start, end)


csv_to_excel('person.csv')

# get_person_html_text(5000, 5001)

do(1, 5001)

# print(get_dict_for_html_text(8))
