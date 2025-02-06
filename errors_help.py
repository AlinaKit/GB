from tkinter.scrolledtext import example


def endless_division(inputtext):
    global dd  # для переиспользования значения вне функции
    while True:
        try:
            num = int(input(inputtext))
            div = 100 / num
            break
        except ValueError as e:  # ошибка преобразования input к int
            print(f'{e}\nTry again')
        except ZeroDivisionError as e:  #  ошибка деления на 0
            div = float('inf')
            break
    dd = div
    return num, div

def endless_division_right(inputtext):  #
    while True:  # повторение пока не введено целое число
        try:  # попытка преобразования к инт
            num = int(input(inputtext))
            break  # сработает только если нет ошибки выше
        except ValueError as e:  #  ошибка преобразования input к int
            print(f'{e}\nTry again')
    try:  # попытка деления, ловим деление на 0 => бесконечность
        div = dd / num
    except ZeroDivisionError as e:  #  ошибка деления на 0 => бесконечность
        div = float('inf')
    return num, div

def endless_division_else(inputtext):  #
    while True:  # повторение пока не введено целое число
        try:  # попытка преобразования к инт
            num = int(input(inputtext))
        except ValueError as e:  #  ошибка преобразования input к int
            print(f'{e}\nTry again')
        else:  #  если нет ошибки, идёт после блока try
            try:  # попытка деления, ловим деление на 0 => бесконечность
                div = dd / num
            except ZeroDivisionError as e:  #  ошибка деления на 0 => бесконечность
                div = float('inf')
            return num, div  # выход из функции и цикла

def example_try():
    c = True
    num = 'defolt'
    dv = 'defolt'
    nn = 'defolt'
    while c:
        try:
            num = int(input('try: попытка действия (int)'))
            print(f'try: ошибка не вызвана, {num = }')
            dv = num / 2
            print(f'try: {dv = }')
        except ValueError as e:
            print(f'exc: сработало с ошибкой, {num = }, {dv = }')
        else:
            nn = dv / 2
            print(f'else: сработало без ошибки, {nn = }')
        finally:
            print(f'fin: выполнилось в любом случае после except либо else:\n{num = }, {dv = }, {nn = }')
            c = bool(int(input('fin: 1 - продолжить, 0 - прервать')))



n, d = endless_division('Input integer number')
print(f'100 / {n} = {d}')
n, d = endless_division_right('Input integer')
print(f'{dd} / {n} = {d}')
n, d = endless_division_right('Input integer')
print(f'{dd} / {n} = {d}')
example_try()