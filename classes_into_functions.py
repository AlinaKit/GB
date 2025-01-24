from  collections import defaultdict

class Numbers:
    def __init__(self, num):
        self.num = num

class ElClassico:
    def __init__(self):
        self.storage = defaultdict(list)

    def __str__(self):
        txt = '\n'.join((f'{k}: {v}' for k,v in self.storage.items()))
        return  f'Objects:\n{txt}'

    def __call__(self, value):
        self.storage[type(value)].append(value)
        return f'{value} add into {type(value)}'

class Fibonacci:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
        self.first = 0
        self.second = 1

    def __iter__(self):
        return self

    def __next__(self):
        while self.first < self.stop:
            self.first, self.second = self.second, self.first + self.second
            if self.start <= self.first <= self.stop:
                return self.first
        raise StopIteration

class Checking:
    def __init__(self, value):
        self.text = value

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def validate(self, value):
        if not isinstance(value, str):
            raise TypeError('Допустимы только буквы.')

class User:
    prev_names = []
    _f_name = Checking(str.istitle)
    _l_name = Checking(str.istitle)
    def __init__(self, f_name, l_name):
        self._f_name = f_name.title()
        self._l_name = l_name.title()

    @property  #  GETTER - необходим, если добавлен SETTER!
    def name(self):
        return f'{self._f_name} {self._l_name}'

    @name.setter  #  SETTER
    def name(self, value):
        self.prev_names.append((self._f_name, self._l_name))
        f, *l = value.split(' ')
        self._f_name = f
        self._l_name = ''
        i = 0
        while i < len(l):
            self._l_name = ' '.join(l)
            i += 1

    @name.deleter
    def name(self):
        self._f_name = None
        self._l_name = None



n = Numbers(42)
print(f'callable(class) = {callable(Numbers)}')
print(f'callable(n) = {callable(n)}')

s = ElClassico()
print(s(42))
print(s('Hello'))
print(s(0))
print(s)

fib = Fibonacci(10, 55)  # 13 21 34
for num in fib:
    print(num)

user = User('Steeve', 'Speeve')
print(f'{user.name = }, {user._f_name}, {user._l_name}')  # так нельзя, потому что _attr на самом деле . а name без скобок, потому что @
# user.name = 'smth new'    # нельзя, потому что метод и _
user._l_name = 'thats'  # вообще тоже нельзя, потому что _, но синтаксически не ошибка
print(f'{user.name = }, {user._f_name}, {user._l_name}')
user.name = 'new name'
print(f'{user.name = }, {user._f_name}, {user._l_name}')
user.name = 'brand new name'
print(f'{user.name = }, {user._f_name}, {user._l_name}\n{user.prev_names = }')
