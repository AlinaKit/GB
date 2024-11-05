# import json
# import  csv
import time
from collections.abc import Callable
from datetime import datetime
# from typing import  Callable
# import random
# import copy
# import sys
# from random import randint, uniform, choice, randrange, shuffle, sample
from functools import wraps, cache


def fst(count: int = 1):
    def snd(func: Callable):
        @wraps(func)
        def trd(*args, **kwargs):
            for _ in range(count):
                print('times: ', _)
                print('START', func.__name__)
                tmm = time.perf_counter()
                res = func(*args, **kwargs)
                print(f'END IN: {(time.perf_counter() - tmm):.2f}')
                'как увеличивать аргументы функции с каждой итерацией? ECCCCC!!!'
                arrs = []
                for i in args:
                    i += 1
                    arrs.append(i)
                args = arrs
            return res
        return trd
    return snd

@fst()
@fst()
def fun_n(a, b):
    c = a ** b
    return c, print(a, '^', b, '=', c)

fun_n(int(input('основание: ')), int(input('cтепень: ')))

@fst(3)
def fun_n(a, b):
    c = a ** b
    return c, print(a, '^', b, '=', c)

fun_n(int(input('начальное основание: ')), int(input('начальная cтепень: ')))

@cache
def known_cache(n: int):
    print('NEW')
    return n

print(known_cache(int(input('ENTER NUM: '))))
print(known_cache(int(input('ENTER NUM: '))))
print(known_cache(int(input('ENTER NUM: '))))
