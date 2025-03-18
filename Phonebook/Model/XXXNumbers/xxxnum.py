
from Phonebook.Model.XXXNumbers.xxxfunc import *
# код - 10 цифр зашфрует в 6 знаков


def xxxnum(tel_num):
    import random
    k_random = random.randint(10, 99)
    random.seed(777)
    global spis_0


    spis_1 = list(spis_0)
    spis_1 = list_random(spis_1)
    x, y = int(str(k_random)[0]), int(str(k_random)[1])
    alpha_x   = spis_1[x][y]


    for j in range(k_random):
        spis_1 = list_random(spis_1)


    s = [[0] * 2 for _ in range(len(tel_num) // 2)]

    k = 0
    for j in range(len(tel_num) // 2):
        s[j][0] = int(tel_num[k])
        s[j][1] = int(tel_num[k + 1])
        k += 2

    sxx = ''
    for j in s:
        spis_1 = list_random(spis_1)
        sxx += spis_1[j[0]][j[1]]

    sxx += alpha_x


    sxx_2, count_1 = '', -1
    for j in range(len(sxx) // 2):
        sxx_2 += sxx[j] + sxx[count_1]
        count_1 -= 1


    return sxx_2

