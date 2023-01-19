import json
import sys

# считывание аргументов командной строки
file1 = sys.argv[1]
file2 = sys.argv[2]


# рекурсивная функция чтения файла json
def report_list(list, values, list_json):
    for i in list:
        for k, v in i.items():
            if k == 'id':
                id = v
            if k == 'value':
                for value in values['values']:
                    if value['id'] == id:
                        list_json.append(value['value'])
            if k == 'values':
                report_list(v, values, list_json)


# функция чтения файла json
def report_write(tests, values, list_json):
    for k, v in tests.items():
        report_list(v, values, list_json)


# открытие файлов и работа с ними
with open(file1, "r+", encoding='utf-8') as first_file, \
        open(file2, "r", encoding='utf-8') as second_file, open('report.json', "w", encoding='utf-8') as report_file:
    tests = json.load(first_file)
    values = json.load(second_file)

    list_json = []
    stroka_json = json.dumps(tests)
    report_write(tests, values, list_json)

    num = 0
    f = 1
    while f:
        f = stroka_json.find('"value": ', f + 1)
        if f == -1:
            break
        stroka_json = stroka_json[:f + 10] + list_json[num] + stroka_json[stroka_json.find('"', f + 10):]
        num += 1
    # сериализация данных
    json.dump(json.loads(stroka_json), report_file, indent=2)
