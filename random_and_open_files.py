import random
from random import randint, uniform, choice, randrange, shuffle, sample

start = int(random.random() * 10 + 5)
end = int(random.random() * 100 + 10)
step = int(random.random() * 10 // 3 + 1)
nums = [1, 2, 3, 4, 5]
s_nums = sample(nums, 3)
text = ['dfghj', 'kjhgf']

print(start, end, step)
print(f'{randint(start, end) = }')
print(f'uniform(0, start //...) = {uniform(0, start // 5 + 1):.3f}')
print(f'{randrange(start, end, step) = }')
print(f'{nums = }')
shuffle(nums)
print(f'{choice(nums) = }')
print(f'shuffle(nums) = {nums}')
print(f'sample(nums, 3) = {s_nums}')
print(f'sample(nums, 3, counts=[1,2,8,0,0]) = {sample(nums, 3, counts=[1, 2, 8, 0, 0])}')
print(sample(range(start, end, step), 5))

txt = open('text.txt', 'r', encoding='utf-8', errors='replace')
print(f'old: {list(txt)}')
txt = open('text.txt', 'wb', buffering=2)  # w открывает либо создает новый файл и записывает все с нуля
txt.write('newline!\n'.encode('utf-8') + 'ххххххххх'.encode('cp1251'))
txt.close()
txt = open('text.txt', 'r', encoding='utf-8', errors='replace')
print(f'new wb: {list(txt)}')
txt = open('text.txt', 'a+', encoding='utf-8')  # а открывает либо создает новый файл и записывает все в конец
# х создает новый файл либо вызывает ошибку еслион есть
txt.write('X' * 10 + '\n')
txt.close()
txt = open('text.txt', 'r', encoding='utf-8', errors='replace')
print(f'new a: {list(txt)}')
# newline closefd

with open('text.txt', 'w+', encoding='utf-8', errors='replace') as txt:
    txt.write('zxcvbnm')
    print(f'{chr(10060) * 5 : >20}')
with open('text.txt') as txt:
    print(list(txt), chr(10060) * 1)
with open('text.txt', 'w+', encoding='utf-8', errors='replace') as txt:
    for line in text:
        print('!!!', line)
        txt.writelines('\n'.join(text))
with open('text.txt') as txt:
    print(list(txt), chr(10060) * 2)
with open('text.txt', 'r+', encoding='utf-8', errors='replace') as txt:
    for line in txt:
        txt.write('nothere')
with open('text.txt') as txt:
    print(list(txt), chr(10060) * 3)
# with open('text.txt', 'r+', encoding='utf-8', errors='replace') as txt:
#     i = 0
#     for line in txt:
#         print(line)
#         print(line, 'GLHF', file=txt)
#         txt[i] = ''
#         i += 1
# with open('text.txt') as txt:
#     print(list(txt), chr(11093) * 2)
with open('text.txt', 'r+', encoding='utf-8', errors='replace') as txt:
    while res := txt.readline(10):
        print(res, end='\n ?')
with open('text.txt', 'a', encoding='utf-8', errors='replace') as txt:
    for line in text:
        print(line, end='\n ?!?', file=txt)
with open('text.txt') as txt:
    print(list(txt), chr(10060) * 4)
