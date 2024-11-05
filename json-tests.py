import gc
import json
import csv
import re
from types import NoneType

from unicodedata import numeric

with open('testusers.json', 'r', encoding='utf-8') as f:
    loaded_file = json.load(f)

text = """
[
{
  "id": 2,
  "name": "Bucha Willy",
  "username": "Superdeath",
  "company": {
    "name": "The Boys",
    "address": {
      "country": "USA",
      "town": "New York"
    }
  },
  "bday": "23.10.1980",
  "wday": "15.01.2005"
}
]
"""

print(f'{loaded_file[0]["id"] = }')
print(f'{loaded_file[0]["name"] = }')
print(f'{loaded_file[0]["company"]["address"]['town'] = }')

loaded_list = json.loads(text)
print(type(loaded_list), loaded_list)

dicty = {
    "id": 3,
    "name": "Anny January",
    "username": "Starlight",
    "company": [
        {
        "name": "The Boys",
        "address": [
            {
            "country": "USA",
            "town": "New York",
            "street": None,
            "house": None,
            "office": None
            }
        ],
        "email": None
        }
    ],
    "bday": "03.09.1999",
    "wday": "07.03.2020"
}

with open('user_2.json', 'w') as f:
    json.dump(loaded_list[0], f)

hey = json.dumps(dicty, indent=4, separators=(', ', ': '))
print(hey)
with open('user_3.json', 'w') as f:
    json.dump(hey, f, ensure_ascii=True) # False для русского языка - последний аттрибут, чтобы буквы не кодировались в файле

def read_csv(filename):
    with open(filename, 'r', newline='', encoding='utf-8') as fl:
        file = csv.reader(fl, delimiter=';') # dialect: exel - запятая-разделитель, exel-tab - табуляция-разделитель
        for line in file:
            print(line)
        print(type(line), chr(10060) * 10)

# filenow = 'workstep_list.csv'
# read_csv(filenow)
# filenow = 'order_list_cd.csv'
# read_csv(filenow)
# filenow = 'machines_list.csv' # неправильная кодировка файла
# read_csv(filenow)
# filenow = 'calendar_list.csv'
# read_csv(filenow)

def csv_to_json(from_csv, to_json, timed_csv, code_code):
    with (
        open(from_csv, 'r', newline='', encoding=code_code) as readed,
        open(to_json, 'w', newline='', encoding=code_code) as writed,
        open(timed_csv, 'w', newline='', encoding=code_code) as timed
    ):
        reading = csv.reader(readed, delimiter=';')
        timing = csv.writer(timed, delimiter=';', quoting=csv.QUOTE_NONNUMERIC)
        all_data = []
        tim_names = []
        for i, line in enumerate(reading):
            if line[0] != '':  # повод для прерывания - первый пустой показатель первого столбца
                if i == 0:
                    # timing.writerow(line)
                    leng = len(line)
                    for j in range(0, leng):
                        tim_names.append(line[j])
                    tim_names.append('id')
                else:
                    for j in range(0, leng):
                        if line[j].isnumeric():
                            line[j] = int(line[j])
                        elif line[j] == '':
                                line[j] = None
                        else:
                            if line[j].find(','):
                                tst = line[j].replace(',', '', 1)
                            if tst.isnumeric():
                                line[j] = line[j].replace(',', '.')
                                line[j] = float(line[j])
                all_data.append(line)
        timing.writerows(all_data)
        all_data = {}
        timed.close()
        with open(timed_csv, 'r', newline='', encoding=code_code) as t_r:
            tim_dict = csv.DictReader(t_r, fieldnames=tim_names, delimiter=';')
            for i, line in enumerate(tim_dict):
                if i == 0:
                    writed.write('[')
                else:
                    line['id'] = i  # пока id равен номеру строки
                    for k in tim_names:
                        kk = {}
                        kkk = line.pop(k)
                        if isinstance(kkk, str):
                            if kkk.find('.'):
                                tst = kkk.replace('.', '', 1)
                            if kkk.isnumeric():
                                kkk = int(kkk)
                            elif tst.isnumeric():
                                kkk = float(kkk)
                        kk.setdefault(k, kkk)
                        all_data.update(kk)
                        # writed.write('\n')
                        # if k == tim_names[-1]:
                        #     writed.write('}')
                        # else:
                        #     writed.write(',\n')
                    json.dump(all_data, writed)
                    writed.write(',')
                writed.write('\n')
            json.dump({}, writed)
            writed.write(']')
                # all_data[0] = i
                # print(all_data)
            # hey = json.dumps(tim_dict, indent=4, separators=(', ', ': '))
            # json.dump(hey, writed)

csv_to_json('workstep_list.csv', 'workstep_list.json', 'timed_workstep_list.csv', 'utf-8')
csv_to_json('order_list_cd.csv', 'order_list_cd.json', 'timed_order_list_cd.csv',  'utf-8')
csv_to_json('machines_list.csv', 'machines_list.json', 'timed_machines_list.csv',  'cp1251')
csv_to_json('calendar_list.csv', 'calendar_list.json', 'timed_calendar_list.csv',  'utf-8')