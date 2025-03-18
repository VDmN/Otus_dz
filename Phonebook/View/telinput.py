from Phonebook.Model.XXXNumbers.xxxnum import *

def get_value():
    ''' формирование списка [имя, тел, примечание] - это value для нашего словаря .json.
        На ввод каждого элемента дается 3 попытки'''

    name, tel, infx = '', '', ''
    inf_0 = 'Некорректный ввод данных 3 раза подряд! Выберите нужное действие:'
    for _ in range(3):
        tmp = input('Введите имя, 3-35 знаков: ')
        if not 2 < len(tmp) < 36:
            print('Некорректная длина имени, введите повторно ')
        else:
            name = tmp
            break

    if name:
        for _ in range(3):
            tmp = input('Введите телефон - строго 10 цифр: ')
            if len(tmp) != 10 or not tmp.isdigit():
                print('Некорректно введен номер! Введите строго 10 цифр: ')
            else:
                tmp = xxxnum(tmp)
                tel = tmp
                break

        if tel:
            for _ in range(3):
                tmp = input('Введите примечание не более 37 знаков, или нажмите Enter: ')
                if not len(tmp) < 38:
                    print('Некорректная длина примечания, введите повторно: ')
                else:
                    infx = tmp
                    break

        else:
            print(inf_0)

    else:
        print(inf_0)

    if name and tel:
        return [name, tel, infx]
    else:
        return [None]

