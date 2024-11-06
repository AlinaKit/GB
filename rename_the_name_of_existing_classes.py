import sys
from random import choice, choices


class RenameInt(int):
    '''многострочная
    строка документации'''
    def __new__(cls, value, name):
      instance = super().__new__(cls, value)
      instance.name = name
      print(f'даём имя числу {value} в рамках данного класса')
      return instance

    def __del__(self):
        print(f'Удаление {self.name}')

class Singleton:
    'cтрока документации __doc__'
    _instance = None
    'а это строка комментария, так как идёт не в нужной строке'
    def __new__(cls, *args, **kwargs):
        'и тут'
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, name):
        self.name = name

    def __str__(self):
        'print(), print({})'
        namme = self.name
        return f'экземпляр класса синглтон {namme}'

    def __repr__(self):
        'print(repr()), print({ = })'
        return f'Singleton({self._instance}, {self.name})'

class NoClassic:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Vector({self.x}, {self.y})'

    def __add__(self, other):  # radd ищется если нет add, у него селф - символ справа от знака
        x = self.x + other.x
        y = self.y + other.y
        return NoClassic(x, y)

class Closet:
    CLOTHES=('one', 'two', 'three')

    def __init__(self, count, storeroom=None):
        self.count = count
        if storeroom is None:
            self.storeroom = choices(self.CLOTHES, k=count)
            print(f'In closet {', '.join(self.storeroom)}, {self.count}')
        else:
            self.storeroom = storeroom

    def __str__(self):
        names = ', '.join(self.storeroom)
        return f'In closet {names}, {self.count}'

    def __rshift__(self, other):
        shift = self.count if other > self.count else other
        self.count -= shift
        return Closet(self.count, choices(self.storeroom, k=self.count))

class MultiStr(str):
    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls, *args, **kwargs)
        return instance

    def __rmul__(self, other):
        words = other.split()
        result = self.join(words)
        return MultiStr(result)

a = RenameInt(42, 'Главный ответ жизни, вселенной и вообще')
b = RenameInt(73, 'Второе лyчшее число')
print(f'{a} - {a.name}\n{b} - {b.name}')

c = Singleton('Name')
print(f'{c.name = }')
d = Singleton('Noname')
print(f'{c.name = }, {d.name = }')
print(c, repr(c))
print('a =',sys.getrefcount(a) - 1, '\nb =', sys.getrefcount(b) - 1)
b = a
cd = a
print('a =', sys.getrefcount(a) - 1, '\nb =', sys.getrefcount(b) - 1)
del a
print('del a')
print('b =', sys.getrefcount(b) - 1)
print('close session')
av = NoClassic(1, 1)
bv = NoClassic(2, 2)
cv = av + bv
print(f'{av = }\n{bv = }\n{cv = }')
cl1 = Closet(10)
for _ in range(3):
    cl1 = cl1 >> 4
    print(cl1)
text = 'one two three'
s = MultiStr('!!!')
print(text * s)
