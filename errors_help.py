def endless_division(inputtext):
    global dd
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
            break
        except ValueError as e:  #  ошибка преобразования input к int
            print(f'{e}\nTry again')
    try:  # попытка деления, ловим деление на 0 => бесконечность
        div = dd / num
    except ZeroDivisionError as e:  #  ошибка деления на 0 => бесконечность
        div = float('inf')
    return num, div

n, d = endless_division('Input integer number')
print(f'100 / {n} = {d}')
n, d = endless_division_right('Input integer')
print(f'{dd} / {n} = {d}')