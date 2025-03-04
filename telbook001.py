import json

print('Привет! Это программа для записи, поиска и хранения контактов.')
sl2 = {}  # основной, словарь для чтения/записи для файла .json
a = ''  # переменная для поиска по имени/части имени
list_inf = []  # этот список будет значением словаря


def create_writen_file():  # запись/создание файла .json
    with open('telbook1.json', 'w', encoding='UTF-8') as tbook1:
        json.dump(sl2, tbook1, ensure_ascii=False, indent=5)

def get_value():   # формируем список - это value для нашего словаря
    name, tel, infx = input('Введите Фио: '), input('Введите телефон: '), input('Введите примечание: ')
    return [name, tel, infx]


def get_sorted_dict(s):  # Сортировка словаря по имени value[0] и раздача ключей по порядку следования
    s = sorted(s.values(), key=lambda k: k[0].lower())
    return {j + 1: s[j] for j in range(len(s))}


k2 = False
try:
    with open('telbook1.json', 'r', encoding='UTF-8') as tbook1:
        sl2 = json.load(tbook1)

    k2 = input('Введите: 1 - поиск контакта, 2 - записать новый контакт, 3 - изменить, 4 - удалить, 5 - просмотреть всё: ')

except:
    print('ВНИМАНИЕ!!! Файл с контактами не найден! Cоздан пустой файл.')
    create_writen_file()

if k2:
    if k2 == '1':
        if not len(sl2):
            print('Список контактов пуст.')
        else:
            a = input('Введите имя: ')
    elif k2 == '2':
        list_inf = get_value()

    elif k2 == '3':
        key_x = input('Введите номер/ключ контакта для его изменения: ')
        if key_x not in sl2:
            print('Некорректный ввод номера контакта.')
        else:
            sl2[key_x] = get_value()
            create_writen_file()
            sl2 = get_sorted_dict(sl2)
            create_writen_file()
            print('Контакт изменен.')

    elif k2 == '4':
        key_x = input('Введите номер/ключ контакта для его удаления: ')
        if key_x not in sl2:
            print('Некорректный ввод номера контакта.')
        else:
            del sl2[key_x]
            sl2 = get_sorted_dict(sl2)
            create_writen_file()
            print('Контакт удален.')

    elif k2 == '5':
        if not len(sl2):
            print('Список контактов пуст.')
        else:
            for k, v in sl2.items():
                print(k, end=': ')
                print(*v, sep=' - ')
    else:
        print('Некорректный ввод')

if a:
    n = 0
    for k, v in sl2.items():
        if a.lower() in v[0].lower():
            n += 1
            print(k, end=': ')
            print(*v, sep=' - ')
    if not n:
        print('Контакты не найдены.')

elif list_inf:
    sl2['A'] = list_inf
    sl2 = get_sorted_dict(sl2)
    create_writen_file()
    print('Контакт сохранен.')