import json


class Workstep_list:
    max_time = 3

    def __init__(self, name = '', clas = 'UNW'):  # появляется в экземплярах класса, но отсутствует в самом классе (выдаст ошибку при вызове)
        self.new = 10
        self.name = name
        self.clas = clas
        print('WOW!!!')

    def obj_name(self):
        for i, j in globals().items():
            if j is self:
                return i

    def max_time_up(self):
        self.max_time += 1
        print(self.obj_name(), ': LEVEL UP!!!')

print('1')
w1 = Workstep_list()
print('2')
w2 = Workstep_list('removing')
print('3')
w3 = Workstep_list('replacing', 'machine')
print(w1.max_time, '; ', w2.max_time, '; ',Workstep_list.max_time)
w1.max_time = 5
print(w1.max_time, '; ', w2.max_time, '; ',Workstep_list.max_time)
Workstep_list.max_time = 8
print(w1.max_time, '; ', w2.max_time, '; ',Workstep_list.max_time)
w2.max_time = 2
print(w1.max_time, '; ', w2.max_time, '; ',Workstep_list.max_time)
Workstep_list.start_time = 0
w1.start_time = 1
print(w1.start_time, '; ', w2.start_time, '; ',Workstep_list.start_time)
w1.stop_time = 4  # добавление ТОЛЬКО в конкретный экземпляр класса, при вызове в других экземплярах\исходном классе выдаст ошибку
print(w1.__dict__, ';\n', w2.__dict__, ';\n', w3.__dict__, ';\n', Workstep_list.__dict__)
w2.new = 13
print(w2.new)
w2.max_time = 13
print(w2.max_time)
w2.max_time_up()
w2.max_time_up()
print(w2.max_time)
