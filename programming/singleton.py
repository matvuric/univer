import requests
import xml.etree.ElementTree as elTree


def singleton(cls):
    instances = {}

    def get_instance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]
    return get_instance


@singleton
class CurrenciesList:
    def __init__(self):
        print('__init__ called')

    def get_currencies(self, currencies_ids_lst=None):
        if currencies_ids_lst is None:
            currencies_ids_lst = ['R01239', 'R01235', 'R01035', 'R01815', 'R01585F', 'R01589', 'R01625', 'R01670',
                                  'R01700J', 'R01710A']
        cur_res_str = requests.get('https://www.cbr.ru/scripts/XML_daily.asp')
        result = {}
        cur_res_xml = elTree.fromstring(cur_res_str.content)
        valutes = cur_res_xml.findall("Valute")

        for _v in valutes:
            valute_id = _v.get('ID')
            if str(valute_id) in currencies_ids_lst:
                valute_cur_val = _v.find('Value').text
                valute_cur_name = _v.find('Name').text
                result[valute_id] = (valute_cur_val, valute_cur_name)
        return result


my_cur_list = CurrenciesList()

print(id(my_cur_list))
my_cur_list2 = CurrenciesList()
res = my_cur_list2.get_currencies(["R01090B", "R01720", "R01565"])
print(res)
