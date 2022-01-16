# Запускайте эту програаму пж из cmd(терминала), тогда вывод будет самоочищаться
# Можете запускать из IDE, но тогда будут сохраняться все выводы(каждого дня)
# P.s. Если, что не работает закомментите вот такие строчки: "os.system('cls||clear')"(без кавычек)
# Тогда вывод будет сразу все дни. Я просто не знаю работает ли такое на Mac


import copy
import time
import random
import sys
import os

class Cell:
    def __init__(self, is_infect=False):
        self.is_infect = is_infect
    
    def infect(self):
        self.is_infect = True
        
    def recover(self):
        self.is_infect = False
        
    def __str__(self):
        return '#' if self.is_infect else '.'
    
    def __eq__(self, other):
        return self.is_infect == other.is_infect
        
        
class Field:
    def __init__(self, height, width):
        self.width = width
        self.height = height
        self.field = [[Cell() for j in range(width)] for i in range(height)]
        
    def show(self):
        for i in range(self.height):
            for j in range(self.width):
                print(self.field[i][j], end="")
            print()
            
    def count_neighbours(self, ind_hei, ind_wid):
        moves = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
        res = 0
        for move in moves:
            if (0 <= ind_hei + move[0] < self.height and 0 <= ind_wid + move[1] < self.width and self.field[ind_hei + move[0]][ind_wid + move[1]].is_infect):
                res += 1
        return res
    
    def life_iter(self):
        newfield = [[Cell() for j in range(self.width)] for i in range(self.height)]
        for i in range(self.height):
            for j in range(self.width):
                if self.field[i][j].is_infect:
                    if 2 <= self.count_neighbours(i, j) <= 3:
                        newfield[i][j].infect()
                    else:
                        newfield[i][j].recover()
                else:
                    if self.count_neighbours(i, j) == 3:
                        newfield[i][j].infect()
                    else:
                        newfield[i][j].recover()
        self.field = newfield
    
    def live(self, day=0):
        st = copy.deepcopy(self.field)
        self.life_iter()
        day += 1
        start = time.time()   
        while (time.time() - start < 0.8):
            pass
        if (st != self.field):
            os.system('cls||clear')
            print(f'День: {day}')
            self.show()      
            self.live(day)


def start():
    print("Здравствуйте, эта программа реализует иргу в жизнь. Хотите начать?(Да/Нет)")
    start = input()
    while(start != "Да" and start != "Нет"):
        print("Вы ввели, что-то другое попробуйте снова")
        start = input()
    if start == "Нет":
        print("До свидания")
        return False
    else:
        print("Начнём!!!")
        return True


def make_size():
    print("Каких размеров будет игра(два числа через пробел, размера до 20)")
    size = input().split()
    while(len(size) != 2 or not size[0].isdigit() or not size[1].isdigit() or int(size[0]) == 0 or int(size[1]) == 0):
        print("Нужно ввести 2 положительных числа через пробел, попробуйте снова")
        size = input().split()
    while(int(size[0]) > 20 or int(size[1]) > 20):
        print("Вы ввели слишком большие размеры")
        size = input().split()
    return int(size[0]), int(size[1])


def make_field(field):
    newfield = [[Cell() for j in range(len(field[0]))] for i in range(len(field))]
    for i in range(len(field)):
        s = input()
        if (s.count('.') + s.count('#') != len(field[0])):
            print("Вы ввели неверную строку, придёться начать ввод с начала")
            return make_field(field)
        else:
            for j in range(len(s)):
                newfield[i][j] = Cell(s[j] == '#')
    return newfield
   
   
def restart():
    print("Хотите повторить?(Да/Нет)")
    restart = input()
    while(restart != "Да" and restart != "Нет"):
        print("Вы ввели, что-то другое попробуйте снова")
        restart = input()
    if restart == "Нет":
        print("До свидания")
        return False
    else:
        os.system('cls||clear')
        print("Давайте!!!")
        return True    
    
    
def main():
    n, m = make_size()
    field = [[Cell() for j in range(m)] for i in range(n)]
    print("Как вы хотите создать игру(random/myself)")
    way = input()
    while(way != "random" and way != "myself"):
        print("Вы ввели, что-то другое попробуйте снова")
        way = input()
    if (way == "random"):
        print("Сколько заражённых клеток, вы хотите создать")
        count_inf = input()
        while(not count_inf.isdigit()):
            print("Вы ввели не число, попробуйте снова")
            count_inf = input()
        count_inf = int(count_inf)
        while(count_inf > n * m):
            print("Вы ввели слишком много заражённых клеток, попробуйте снова")
            count_inf = int(input())
        shuff_index = list(range(n * m))
        random.shuffle(shuff_index)
        for q in range(count_inf):
            field[shuff_index[q] // m][shuff_index[q] % m].infect()
    else:
        print("Введите ваше поле")
        field = make_field(field)
    game = Field(n, m)
    for i in range(n):
        for j in range(m):
            if field[i][j].is_infect:
                game.field[i][j].infect()
    print("Ваше поле")
    game.show()
    print("Игра началась")
    game.live()
    print("Игра закончилась")
    res_check = restart()
    if(res_check):
        main()
            
check = start()
if(check):
    main()