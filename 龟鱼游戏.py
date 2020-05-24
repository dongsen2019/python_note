# 龟鱼游戏

"""
假设游戏场景为范围(x,y)为 0 <= x <= 10 , 0 <= y <=10
游戏生成1只乌龟和10条鱼
他们的移动方向均随机
乌龟最大的移动能力是2(乌龟可以随机选择移动1或者2)，鱼的最大移动能力是1
当移动到场景边缘，自动向反方向移动
乌龟初始化体力为100(上限)
乌龟每移动一次，体力消耗1
当乌龟和鱼重叠，乌龟吃掉鱼，乌龟体力值加20
鱼不计算体力
当乌龟体力值为0或者鱼的数量为0时，游戏结束
"""

import random
import time


class Cell():
    def __init__(self, i, j):
        self.x = i
        self.y = j

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False


class Game():
    row = 10
    col = 10
    wall = '1'
    passage = '0'
    fish = 'f'
    tortoise = 't'
    fish_num = 0
    tortoise_power = 100
    fish_list = []
    tortoise_list = []
    store = []

    def __init__(self):
        for i in range(0, 12):
            temp = []
            for j in range(0, 12):
                if i == 0 or i == 11:
                    temp.append(self.wall)
                else:
                    if j == 0 or j == 11:
                        temp.append(self.wall)
                    else:
                        temp.append(self.passage)
            self.store.append(temp)

        while True:
            mk = None
            tmp = None
            if len(self.fish_list) == 10:
                break
            else:
                tmp = Game.rand_cell()
                for i in self.fish_list:
                    if tmp == i:
                        mk = True

            if mk == True:
                continue
            else:
                self.fish_list.append(tmp)
                Game.fish_num += 1

        while True:
            mk = None
            if len(self.tortoise_list) == 1:
                break
            else:
                tmp = Game.rand_cell()

            for i in self.fish_list:
                if i == tmp:
                    mk = True

            if mk == True:
                continue
            else:
                self.tortoise_list.append(tmp)

        for i in self.fish_list:
            self.store[i.x][i.y] = self.fish

        self.store[self.tortoise_list[0].x][self.tortoise_list[0].y] = self.tortoise

    @staticmethod
    def rand_cell():
        x = random.randint(1, 10)
        y = random.randint(1, 10)
        return Cell(x, y)

    def update_coord(self):
        d_list = ['u', 'd', 'l', 'r']
        for i in self.fish_list:
            self.store[i.x][i.y] = self.passage
            res = random.randint(0, 3)
            if d_list[res] == 'u':
                if i.x - 1 == 1:
                    i.x += 1
                else:
                    i.x -= 1
            elif d_list[res] == 'd':
                if i.x + 1 == 11:
                    i.x -= 1
                else:
                    i.x += 1
            elif d_list[res] == 'l':
                if i.y - 1 == 1:
                    i.y += 1
                else:
                    i.y -= 1
            else:
                if i.y + 1 == 11:
                    i.y -= 1
                else:
                    i.y += 1

        for j in self.tortoise_list:
            self.store[j.x][j.y] = self.passage
            step = random.randint(1, 2)
            for k in range(step):
                res = random.randint(0, 3)
                if self.store[res] == 'u':
                    if j.x - 1 == 1:
                        j.x += 1
                    else:
                        j.x -= 1
                elif self.store[res] == 'd':
                    if j.x + 1 == 11:
                        j.x -= 1
                    else:
                        j.x += 1
                elif self.store[res] == 'l':
                    if j.y - 1 == 1:
                        j.y += 1
                    else:
                        j.y -= 1
                else:
                    if j.y + 1 == 11:
                        j.y -= 1
                    else:
                        j.y += 1

    def refresh(self):
        for i in self.fish_list:
            if i == self.tortoise_list[0]:
                self.fish_list.remove(i)
                self.fish_num -= 1

        for i in self.fish_list:
            self.store[i.x][i.y] = self.fish
        self.tortoise_power -= 1

        self.store[self.tortoise_list[0].x][self.tortoise_list[0].y] = self.tortoise

    def print_store(self):
        for x in self.store:
            for y in x:
                print(y, end=' ')
            print()


g = Game()

while True:
    g.print_store()
    g.update_coord()
    g.refresh()
    time.sleep(1)
    print('-'*22)
    if g.tortoise_power == 0 or g.fish_num == 0:
        print("游戏结束")
        break
    else:
        continue

# c1 = Cell(3,2)
# c2 = Cell(2,4)
# c3 = Cell(3,2)
# print(c1 == c2,id(c1),id(c2))
# print(c1 == c3,id(c1),id(c3))
