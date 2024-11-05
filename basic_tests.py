print(6 - -81)

text = 'Gjdf vggGV KbhdGHG, LGG hgHGygj\nDFGHJK!&?'

from random import random
# введение в питон, комментарии - диез плюс пробел

# Придумайте название для переменной, в которой будет храниться «количество братьев и сестер короля» - num_king_bros_and_siss

def print_all(a, b, c):
    print(f'{str(a)} + {str(b)} = {str(c)}')
    d = 'ready'
    return d

magic = 45632

state = 'none'

hexx = hex(8)

print(str(hexx)[1])

print(int(10 * round(random(), 1)))

print(text)
print(f"H on {text.find('H')} of {len(text)} place")

state = print_all(3, hexx, text.find('H'))
print(state)

def get_hid_card(s, n=4):
    card = '*' * int(n) + str(s)[12:16]
    return card
card = get_hid_card(1254986575435618, 5)
print(card)

num = 'python'
nn = 3
mm = 2
print(str(num)[0 - int(nn):] * int(mm))

