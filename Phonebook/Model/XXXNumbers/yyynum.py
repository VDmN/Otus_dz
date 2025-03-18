
from Phonebook.Model.XXXNumbers.xxxfunc import *
# расшифровка
# a = input('Введите зашифрованную 6-ти значную строку : ')

def yyynum(a):
    import random
    random.seed(777)

    global spis_0

    a = a[::2] + a[1::2][::-1]
    a2 = a[:-1]


    spis = list(spis_0)
    spis = list_random(spis)

    k_rand = ''
    for j in range(len(spis)):
        if a[-1] in spis[j]:
            k_rand += str(j)
            k_rand += str(spis[j].index(a[-1]))


    for _ in range(int(k_rand)):
        spis = list_random(spis)


    txx = ''
    for j in a2:
        spis = list_random(spis)
        for k in range(len(spis)):
            if j in spis[k]:
                txx += str(k) + str(spis[k].index(j))


    return f'({txx[:3]})-{txx[3:6]}-{txx[6:8]}-{txx[8:]}'

