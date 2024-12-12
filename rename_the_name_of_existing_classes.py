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

    # __slots__ = ('_x', '_y')

    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __repr__(self):  # repr(a) == f'{a = }' == collections (?)
        return f'Vector({self._x}, {self._y})'

    def __add__(self, other):  # radd ищется если нет add, у него селф - символ справа от знака
        x = self._x + other._x
        y = self._y + other._y
        return NoClassic(x, y)

    def __iadd__(self, other):
        x = self._x + other._x
        y = self._y + other._y
        return NoClassic(x, y)

    # def

    def __eq__(self, other):
        return (self._x == other._x and self._y == other._y) or (sorted((self._x, self._y)) == sorted((other._x, other._y)))

    # def __ne__(self, other):
    #     return not (self.x == other.x and self.y == other.y)

    def __gt__(self, other):
        return (self._x ** 2 + self._y ** 2) > (other._x ** 2 + other._y ** 2)

    # def __ge__(self, other):
    #     return (self.x ** 2 + self.y ** 2) <= (other.x ** 2 + other.y ** 2)

    def __lt__(self, other):
        return (self._x ** 2 + self._y ** 2) < (other._x ** 2 + other._y ** 2)

    # def __le__(self, other):
    #     return (self.x ** 2 + self.y ** 2) >= (other.x ** 2 + other.y ** 2)

    def __hash__(self):
        return hash((self._x, self._y))

    # def __getattribute__(self, item):  # по умолчанию
    #     return object.__getattribute__(self, item)

    def __setattr__(self, key, value):  # установка хначения атрибута, в случае несуществования стаботает иф
        if key not in ('_x', '_y'):
            raise AttributeError('Неверный атрибут')
        return object.__setattr__(self, key, value)

    def __getattr__(self, item):  # вместо проверки на ошибку в __getattribute__, срабатывает только при ошибке __getattribute__
        print('Неверный атрибут!')
        return None

    # def __delattr__(self, item):
    #     if item in ('_x', '_y'):
    #         setattr(self, item, 0)
    #     else:
    #         object.__delattr__(self, item)

class Closet:
    CLOTHES=('one', 'two', 'three')

    def __init__(self, count, storeroom=None):
        self.count = count
        if storeroom is None:
            self.storeroom = choices(self.CLOTHES, k=count)
            print(f'In closet {', '.join(self.storeroom)}, {self.count}')
        else:
            self.storeroom = storeroom

    def __str__(self):  # a == f'a'
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
print(c, '\n', repr(c))
print('a =',sys.getrefcount(a) - 1, '\nb =', sys.getrefcount(b) - 1)
b = a
cd = a
print('a =', sys.getrefcount(a) - 1, '\nb =', sys.getrefcount(b) - 1)
del a
print('del a')
print('b =', sys.getrefcount(b) - 1)
av = NoClassic(1, 1)
bv = NoClassic(2, 2)
cv = av + bv
print(f'{av = }\n{bv = }\n{cv = }')
dv = av
print(f'{av = }\n{dv = }')
print(f'{av == dv}')
dv += bv
print(f'{dv = }')
print(f'{cv == dv}\n{av == dv}')
cl1 = Closet(10)
for _ in range(3):
    cl1 = cl1 >> 4
    print(cl1)
text = 'one two three'
s = MultiStr('!!!')
print(text * s)  # не наоборот, text * MultiStr выдаст ошибку!




print('close session')