from random import random
import sys


def pos_non_pos(pos = 0, /, posnonpos = 0, *, keysnonpos = 0):  # по порядку / по порядку либо имени * по имени
    return pos + posnonpos + keysnonpos

print(pos_non_pos(1, 2, keysnonpos=3))
print(pos_non_pos(1, posnonpos=2, keysnonpos=3))

def summs(*arg):  # по сути получение кортежа
    return sum(arg)

print(summs(1))
print(summs(1, 2))

def corts(**krg):  # по сути получение словаря
    """описание результата действий функции (Return the maximum number)
    
    :param: описание параметра и его типа/наполнения (tuple of int or float numbers)
    :return: описание возврата и его типа/наполнения (int or float number from the tuple args)
    """  # сторка для многострочной документации (описания функции)
    for i in krg:
        print(krg[i])

corts(fst=1)
corts(fst=1, sec=2)

def list_app(n, list=None):  # !!! список изменяем и при получении списка на вход изменится он, а не ссылка на него !!!
    """описание действий функции - тут добавление n элементов в конец нового либо сущ-го списка."""  # сторка для документации (описания функции)
    print(locals())
    if list is None:         # !!!
        list = []            # !!!
    for i in range(1, n + 1):
        list.append(i)
    return list

lambda_anon_func = lambda a, b, c: a + b ** c  # плохая практика! присвоение переменной функции, далее переменная вызывается с действием () и параметрами
print(lambda_anon_func(5, 10, 2))

dict_ry = {'t': 'h', 'm': 'j', 'a':'w'}
dict2 = {}
dict2.update(dict([('10', 11), ('11', 12)]))
sort_key = sorted(dict_ry.items())                      # сортировка по ключу
sort_val = sorted(dict_ry.items(), key=lambda x: x[1])  # сортировка по значению
print(f'сортировка без доп аргументов: {sort_key}\nсортировка лямбдой {sort_val}')

print(*map(lambda x: x.upper(), dict_ry))
# print(*map(lambda x: x.upper(), dict_ry.items()))   ???
d = list_app(2)
dd = [1, 0, 3]
ddd = [1, 2]
emp = []
for ds, dds, ddds in zip(d, dd, ddd):
    print(f'{ds}, {dds:.2f}, {ddds}')

print(tuple(filter(lambda x: x > 1, dd)))
print(*filter(lambda x: x > 1, dd), sep='\t')

print(max(dd))   # мах из кортежа и списка
print(max(dict2, key=lambda x: x[1])) # [1] - по значению, [0] - по ключу, -х - взятие с обратным знаком, not x.startwith('__') - не начинающиеся с __
print(max(emp, default='пусто!'))
print(max(*dd))

print(min(dd))  # аналогично мах

print(sum(dd))   # сумма в кортеже
print(sum(dd, start=100))   # сумма в кортеже + start

print(f'{all(dd)}: все true')  # false если хоть один не true (0, '', [], (), None)
# print(f'{len(all(map(lambda x: x > 0, dd))) == len(dd)}: все >0')

print(f'{any(dd)}: большинство true')  # false если большинство не true (0, '', [], (), None)
# print(f'{len(any(map(lambda x: x > 0, dd))) >= len(dd)/2}: большинство >0')

# номер символа и символ номера
charr = 'g'
nchr = ord(charr)
num = int(1000000 * round(random(), 6))
print(f'{nchr} = {chr(nchr)}, {num} = {chr(num)}')

print(*filter(lambda x: not x[0].startswith('__'), globals().items()))
print(*filter(lambda x: not x[0].startswith('__'), vars().items()))
print(vars(list_app))

print(f'{d = }, {dd = }')
d, dd = dd, d
print(f'{d = }, {dd = }')

# распаковки левого в правое
a, b = input('введите 2:')
print(a, b)
a, *b = input('введите от 2')
print(a, b)
a, *b, c = input('ведите больше 3') # *_ используется для "удаления" полученного списка
print(a, b, c)

l_i = iter(d)
print(*l_i)
print(*l_i)

l_i = iter(d)
for i in range(0, len(d) + 1):
    print(next(l_i, 'end'))
a, c = 1, 7
generr = (chr(i) for i in range(97 + int(a), 98 + int(c), int(a)) if i % 2 != 0)  # если элементы нужны по одному
for x in generr:
    print(x)

gen_list = [chr(i) for i in range(97 + int(a), 98 + int(c), int(a)) if i % 2 != 0]  # если элементы нужны все сразу
print(gen_list)
for x in gen_list:
    print(x)

gen_set = {chr(i) for i in range(97 + int(a), 98 + int(c), int(a)) if i % 2 != 0}  # элементы уникальны
print(gen_set)
gen_dict = {i: chr(i) for i in range(97 + int(a), 98 + int(c), int(a)) if i % 2 != 0}
print(gen_dict)

def generr_lk_fnc(a: int, c: int):
    for i in range(97 + a, 98 + c, a):
        if i % 2 != 0:
            b = chr(i)
            yield b
a, c = 3, 20
print(*generr_lk_fnc(a, c))
for i, n in enumerate(generr_lk_fnc(a, c)):
    print(i, ', ', n)
    nn = 'nine!!!'

l_i = iter(generr_lk_fnc(a, c))
print(next(l_i, nn))
print(next(l_i, nn))
print(next(l_i, nn))
print(next(l_i, nn))