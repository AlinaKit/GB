from random import random, randint


class Player:
    max_life = 3
    lvl = 0

    def obj_name(self):
        for i, j in globals().items():
            if j is self:
                return i

    def __init__(self, clas = 'UNKNOW'):  # появляется в экземплярах класса, но отсутствует в самом классе (выдаст ошибку при вызове)
        namme = self.obj_name()
        # for i, j in globals().items():
        #     if j is self:
        #         namme = str(i)
        self.name = namme
        self.clas = clas
        self.health = 100

    def get_bottle(self, bottle):
        self.bottle_cup = bottle

    def lvl_up(self):
        self.lvl += 1
        print(self.name, ': LEVEL UP!!!')

    def heal(self, quantity):
        try:
            quantity = int(quantity) and quantity > 0
        except:
            print('неверно, попробуйте другое целое положительное число')
            quantity = 0
        self.health += quantity
        self.bottle_cup.now_v -= quantity

    def vamp_attack(self, other, quantity):
        while quantity <= 0:
            try:
                quantity = int(quantity) and quantity > 0
            except:
                print('неверно, попробуйте другое целое положительное число')
                quantity = 0
        self.health += quantity * 0.5
        other.health -= quantity


class Heal_Potion:
    lvl = 1
    volume = 200 * lvl * 0.5
    now_v = 100

player_1 = Player('HUMAN')
player_2 = Player('notHUMAN')
bottle_1 = Heal_Potion()
bottle_2 = Heal_Potion()
player_1.get_bottle(bottle_1)
player_2.get_bottle(bottle_2)
print(player_1.__dict__, player_2.__dict__, bottle_1.__dict__, bottle_2.__dict__)
player_1.vamp_attack(player_2, randint(10, 20))
print(player_1.__dict__, player_2.__dict__, bottle_1.__dict__, bottle_2.__dict__)
player_1.heal(20)
print(player_1.__dict__, bottle_1.__dict__, player_2.__dict__, bottle_2.__dict__)

player_1.lvl_up()