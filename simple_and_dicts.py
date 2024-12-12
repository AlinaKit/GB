import copy
from random import random

word = 'ASdfGHJKiUHGF DFGHJk WSDjhgtreWSDCVB THNbvcxS1@!'
nums = 86258
len_num = int(input('Enter num: '))
print('your num - {}'.format(len_num))  # one of formatting method
letter = str(input('Enter letter: '))
print('your letter - %s' % (letter))  # old formatting of string - % + first letter of type(d=didgit)

def func(a, b:int, c=0):   # start function
    return a[c:b]

print(func(word, len_num))  # print on screen

print(word[::-1])  #  reverse string

print(hex(len_num))  # num in 16x view

print(round(random(), 1))  # random num round to 1 sign after point

print(len(word))  # length of string

print(word.find(letter))  # find 'letter' in word (string)

print(f'dfg {(letter + str(len_num)):>10} and {nums:.2f} + jhgfd')  # f'' is string with operations in {},\
# u can format digits with :.nf (n = number), \
# выровнять - > to right, < to left, и число - количество отступов, ^ - center

print(f'{nums = :_}') # печать числа с разделителями и =

print(f'{word} string is {isinstance(word, str)} but {nums} integer is {isinstance(nums, int)} and string is {isinstance(nums, str)}')  # return bool of equal of obj and type

def guess_number(num:int):  # if-construction
    return 'You win!' if num == 42 else 'Try again!'

def else_c(a):   # if-else
    b = ''
    c = 0
    if isinstance(a, str):
        b = 'string'
        c = 1
    elif isinstance(a, int):
            b = 'integer'
            c = 2
    else:
            b = 'other'
            c = 3
    return b, c

def match_fun(smt):  # if-concstr with no if
    ch = ''
    match smt:
        case 1:
            print(1)
            ch = str(smt)
        case '':
            print('empty')
            ch = 'empty'
        case _:
            print('not 1 or empty')
            ch = 'NO!'
    return ch

def back_nums(wrd): # while-structure
    i = len(wrd) - 1
    while i >= 0:
        print(f'{i}: {wrd[i]}')
        i -= 1
    print('finished!')

def fac(max): # while-structire for factorial
    i = 1
    f = 1
    all = '1'
    while i <= max:
        f *= i
        all += '*' + str(i)
        i += 1
    print(f'{f}\n{all}')

def num_let(string:str, letter:str):
    i = 0
    max = len(string)
    count = 0
    while i < max:
        if string[i] == letter:
            count += 1
        i += 1
    print(f'in {string} {letter} is {count} times')

def count_chars(string, char):  # no register
    index = 0
    count = 0
    char = char.lower()
    string = string.lower()
    while index < len(string):
        if string[index] == char:
            count += 1
        index += 1
    return count

def is_arguments_for_substr_correct(strg, ind, leng):
    if ind < 0 or leng < 0 or ind >= len(strg) or ind + leng > len(strg):
        return 'False'
    return 'True'

def is_contains_char(strk, smbl):  # q cicle
    i = 0
    max = len(strk)
    while i < max:
        if strk[i] == smbl:
            return True
        i += 1
    return False

def reverse_string(text):
    result = ''
    for char in text:
        result = char + result
    return result

def filter_string(strk, symb):  # for
    res = ''
    for char in strk:
        if char.lower() != symb.lower():
            res = res + char
    return res

for i in range(1, 3):
    print(i)
print('new')
for i in range(3, 0, -1):
    print(i)
print('new')
for i in range(3):
    print(i)
print('new')

def print_table_of_squares(fro, to):
    for i in range(fro, to + 1):
        print(f'square of {i} is {i ** 2}')

print(guess_number(42))
print(nums == 42 and 'win!' or 'again!')
print_table_of_squares(2, 4)
print(filter_string(word, 'H'))

ln = len_num
cc = int(input('num:  '))
while cc < nums:
    ln += 5
    cc = cc + ln
    print(ln, cc)
    if ln >= 100:
        print('overmore!')
        break
else:
    print(cc)

for i, symb in enumerate(str(nums), start=1): # перебор с i
    print(i, symb)

  # мнимое с j


a, b, *_ = word.split(' ') # split string on few sub and write all more then change in timing _
print(a, b)
print(_)
c = '/'.join(_) # join string with /
print(c)
print(word.startswith('UHGF', 9))
print(word.endswith('bvc', 0, -5))
print(word.index('W', 2)) # index 'A' with start of string in 2

a = {'keyone': 'mean', 'keytwo': 2, letter: 'let'}
b = dict(keyone='mean', keytwo=2)
c = dict([('keyone', 'mean'), ('keytwo', 2)])
c['newkey'] = nums  # new key with mean
d = dict(keyone='mean', keytwo=2)
print(a[letter], '\n', b, '\n', c['keyone'], '\n', d.get('key', 'defolt_if_nothing')) # print dictionary b, and mean of key from dicts a, c and d (d with defolt if key not exist)
s = a.setdefault('none')
print(f'{s = }\t{a = }')
s = a.setdefault('nothing', 'NONE')
print(f'{s = }\t{a = }')
s = a.setdefault('none', 'none')
print(f'{s = }\t{a = }')
s = a.setdefault(2)
print(f'{s = }\t{a = }')  # усли нет ключа - ставится либо None либо запись после запятой, если есть - вызывается
print(f'{a.keys() = }')
for keys in a.keys():  # equal "for keys in a"
    print(keys)
for vals in a.values():  # non equal "for vals in a"
    print(vals)
for keys, vals in a.items():  # equal "for tuple in a.items()": ту запись ключа и значения в 2 переменные(хорошо), \
    # эквивалентно записи в кортеж tuple как (ключ, знач), где tuple[0]=keys, tuple[1]=vals
    print(f'{keys} is {vals}')
s = a.pop(letter)  # ONLY EXISTING KEYS, GET VALUE
print(f'{s = }\t{a = }')
s = a.pop(2)  # ONLY EXISTING KEYS, GET VALUE
print(f'{s = }\t{a = }')
s = a.popitem()  # get last pair key-value
print(f'{s = }\t{a = }')
a.update(dict(key10=10))
a.update(dict([(10, 11), (11, 12)]))
print(a, 'update')
nd = a | b | c | d
print(nd)

sets = {3, 2, 'ten', letter, 1.12}  # grade by ups numbers, change, (tuple), string
print(sets)
f_sets = frozenset((3, letter, 'str', 1.1))  # grade by string, numbers, changes???
sets.add((1, 'new'))
print(sets)
sets.remove((1, 'new'))   # discard позволяет удалить существующие и не вызвать ошибку несуществующими
print(sets)
print(f_sets)
new = sets.intersection(f_sets)  # equal set1 & set2 - общее
print(new, ' - общее\n', sets, ' - начальный')
new = sets.union(f_sets)  # equal set1 | set2 - всё в одном экземпляре
print(new, ' - сумма\n', sets, ' - начальный')
new = sets.difference(f_sets)  # equal set1 - set2 - первое мн-во без общего
print(new, ' - разница\n', sets, ' - начальный')
new2 = f_sets.difference(sets)  # суммарное множество?!
print(new2, ' - разница наоборот\n', f_sets, ' - начальный')
all_lists = new.copy()
all_lists.add(new2)
print('1: ', new, '\n2: ', new2, '\n3: ', all_lists)


test = 'GKjh 8 098'
test_utf = test.encode('utf-8')
test_ascii = test.encode('ascii')

print(f'{test = }, {type(test) = }')
print(f'{test_utf = }, {type(test_utf) = }')
print(f'{test_ascii = }, {type(test_ascii) = }')

'логика массивов'
a = {'keyone': 'one', 'keytwo': 2, 'keythree': 'one'}
b = {'keyone': 1, 'keythree': 'one', 'keyfour': 2}
print(f'{a = }, {b = }')
# print(f'{a & b = }')
print(f'{a | b = }')
# print(f'{a + b = }')
# print(f'{a - b = }')
print(f'{a = }, {b = }')
a = b
b.update(dict(newkey='new'))
print(f'{a = }, {b = }\n')

a = {1, 2, 3}
b = {2, 3, 4, 5}
print(f'{a = }, {b = }')
print(f'{a & b = }')
print(f'{a | b = }')
# print(f'{a + b = }')
print(f'{a - b = }')
print(f'{b - a = }')
print(f'{a = }, {b = }')
a = b
b.add('new')
print(f'{a = }, {b = }\n')

a = [1, 2, 3]
b = [2, 3, 4, 5]
print(f'{a = }, {b = }')
# print(f'{a & b = }')
# print(f'{a | b = }')
print(f'{a + b = }')
# print(f'{a - b = }')
print(f'{a = }, {b = }')
a = b
b.append('new')
print(f'{a = }, {b = }\n')

a = (1, 2, 3)
b = (2, 3, 4, 5)
print(f'{a = }, {b = }')
# print(f'{a & b = }')
# print(f'{a | b = }')
print(f'{a + b = }')
# print(f'{a - b = }')
print(f'{a = }, {b = }')
c = b
b = b + a
print(f'{c = }, {b = }\n')

a = ((1, 2, 3))
b = ((2, 3, 4, 5))
print(f'{a = }, {b = }')
# print(f'{a & b = }')
# print(f'{a | b = }')
print(f'{a + b = }')
# print(f'{a - b = }')
print(f'{a = }, {b = }')
c = b
b = b + a
print(f'{c = }, {b = }\n')