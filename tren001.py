import time
import math

class Decorator1:
    def __init__(self, func):
        self.func = func
        self.summa = 0
        self.level = 0


    def __call__(self, *args, **kwargs):
        # if self.level == 0:
        #     print(f'Это первый вызов функции {self.func.__name__}')
        # print(f'{self.func.__name__} вызвана на уровне {self.level}')
        t_0 = time.time()  # Засекли время начала работы функции
        self.level += 1
        result = self.func(*args, **kwargs)  # запустили функцию
        self.level -= 1
        # print(f'{self.func.__name__} закончила расчет на уровне {self.level}')
        t_end = time.time()  # Засекли время окончания работы функции
        dt = t_end - t_0  # Вычисляем время работы
        self.summa += dt  # добавлено для рекурсии
        if self.level == 0:
            # print(f'Функция снова вернулась на исходный уровень {self.level}. Выводим сумму времени.')
            print(f"Время работы: {self.summa * 1_000_000} микросекунд")  # Перевод в микросекунды: * 10**6
        return result


@Decorator1
def get_fact(n):   # Свой какой-то вариант функции, возвращает факториал
    s = 1
    for j in range(1, n+1):
        s *= j
    return s


@Decorator1
def fff(p):
    def get_rec_fact(n):   # Свой какой-то вариант рекурсивной функции, возвращает факториал
        if n < 2:
            return 1
        return n * get_rec_fact(n-1)
    return get_rec_fact(p)

a = math.factorial   # чтобы запустить без декоратора - надо поставить '#' на следующую строчку
a = Decorator1(a)   # декорируем функцию из модуля math, которая возвращает факториал

num = int(input())
print('Встроенная. Результат: ', a(num), '\n')
print('Самописная. Результат: ', get_fact(num), '\n')
print('Рекурсивная. Результат:', fff(num))

