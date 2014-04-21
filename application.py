__author__ = 'Александр'

from random import randrange
from time import time
from tkinter import *
from tetrisfig import *
from tkinter.messagebox import *
from tetrisfig import *
import copy

class Application(Frame):
    '''
    Приложение. Наследует класс Frame. Создание окна, холста и всех функций для реализации приложения
    '''
    #ширина рабочего поля
    width = 325
    #высота рабочего поля
    height = 520
    #цвет фона холста
    bg = "white"
    #отступ между ячейками
    indent = 2
    #размер одной из сторон квадратной ячейки
    gauge = 30
    #скорость по умолчанию
    speed_def = 1000
    #скорость при смещении фигуры быстро вниз
    speed_down = 10
    #статус начала игры
    play = 0
    #количество доступных фигур
    fig_count = 7
    #идентификатор анимации
    id_after = 0

    blockarray = []

    def __init__(self, master=None):
        #инициализация окна
        Frame.__init__(self, master)
        self.pack()
        self.master = master
        self.blockarray = []
        #инициализация меню
        self.m = Menu(master)
        master.config(menu = self.m)
        self.m_play = Menu(self.m)
        self.m.add_cascade(label = "Игра",menu = self.m_play)
        self.m_play.add_command(label="Новая игра", command = self.new_game)
        self.m_level = Menu(self.m)
        self.m.add_cascade(label = "Уровень",menu = self.m_level)
        self.m_level.add_radiobutton(label="Новичок", command = self.game_level_1)
        self.m_level.add_radiobutton(label="Опытный", command = self.game_level_2)
        self.m_level.add_radiobutton(label="Профи", command = self.game_level_3)

        #установить скорость равной скорости по умолчанию
        self.speed = self.speed_def
        #вызов функции создания холста
        self.createCanvas()

    def game_level_1(self):
        self.speed_def = 1000
        self.speed = self.speed_def

    def game_level_2(self):
        self.speed_def = 500
        self.speed = self.speed_def

    def game_level_3(self):
        self.speed_def = 100
        self.speed = self.speed_def

    #добавление холста на окно
    def createCanvas(self):
        self.canv = Canvas(self)
        self.canv["height"] = self.height
        self.canv["width"] = self.width
        self.canv["bg"] = self.bg
        self.canv.pack()
        self.master.bind("<Down>",self.downObj)
        self.master.bind("<Return>",self.rotateObj)
        self.master.bind("<Right>",self.rightObj)
        self.master.bind("<Left>",self.leftObj)
        self.master.bind("<space>",self.fastDown)
        #клик по холсту вызывает функцию play

    #функция удаления точек строки
    def delString(self,numb_array):
        for string in sorted(numb_array):
            print(string)
            for item in range(len(self.blockarray)):
                if int(self.blockarray[item].split("_")[0]) == string:
                    #удалить ячейки
                    self.blockarray[item] = "16_16"
                else:
                    #сдвиг ячеек после того, как убираются строки
                    if int(self.blockarray[item].split("_")[0]) < string and int(self.blockarray[item].split("_")[0]) >= 0:
                        self.blockarray[item] = str(int(self.blockarray[item].split("_")[0]) + 1)+"_"+self.blockarray[item].split("_")[1]

    #Функция проверки заполненных строк или переполнения
    def check(self):
        #проверить, есть ли заполненные строки
        temp_array = copy.deepcopy(self.blockarray)
        strings = [0]*17
        delstrings = []
        for item in self.blockarray:
            #просматривать только те строки, которые входят в окно
            if int(item.split("_")[0]) < 16 and int(item.split("_")[0]) >= 0:
                strings[int(item.split("_")[0])] += 1
                #если накопилось в строке 10 точек, то добавить строку в массив delstrings
                if strings[int(item.split("_")[0])] == 10:
                    delstrings.append(int(item.split("_")[0]))
        #перерисовать поле, если были изменения
        if len(delstrings) > 0:
            self.delString(delstrings)
            self.paint(temp_array,self.blockarray,"black")
        #если все строки заполнены хоть чем-то, то конец игры. ДОДЕЛАТЬ
        return 0

    #быстрый спуск
    def fastDown(self,e):
        self.speed = self.speed_down

    def downObj(self,e):
        self.play = 1
        self.master.after_cancel(self.id_after)
        #скопировать текущие координаты
        temp_array = copy.deepcopy(self.new_obj.coords)
        #если можно сдвинуть вниз, то перерисовать фигуру,
        # если сдвиг вниз невозможен:
        # 1 координаты текущей фигуры добавить в массив blockarray
        # 2 проверить, не сложилась ли строка (если да, то обработать)
        # 3 генерировать новую фигуру
        if self.new_obj.down(self.blockarray) == 0:
            self.paint(temp_array,self.new_obj.coords,self.new_obj.color)
            self.id_after = self.master.after(self.speed,self.downObj,e)
        else:
            for item in self.new_obj.coords: self.blockarray.append(item)
            if self.check() == 0:
                self.new_obj = Tetris(randrange(self.fig_count))
                self.paint(self.new_obj.coords,self.new_obj.coords,self.new_obj.color)
                #установить скорость по умолчанию
                self.speed = self.speed_def
                self.downObj(e)

    def rightObj(self,e):
        if self.play == 1:
            self.master.after_cancel(self.id_after)
        #скопировать текущие координаты
        temp_array = copy.deepcopy(self.new_obj.coords)
        if self.new_obj.right(self.blockarray) == 0:
            self.paint(temp_array,self.new_obj.coords,self.new_obj.color)
            self.id_after = self.master.after(self.speed,self.downObj,e)

    def leftObj(self,e):
        if self.play == 1:
            self.master.after_cancel(self.id_after)
        #скопировать текущие координаты
        temp_array = copy.deepcopy(self.new_obj.coords)
        if self.new_obj.left(self.blockarray) == 0:
            self.paint(temp_array,self.new_obj.coords,self.new_obj.color)
            self.id_after = self.master.after(self.speed,self.downObj,e)

    def rotateObj(self,e):
        if self.play == 1:
            self.master.after_cancel(self.id_after)
        #скопировать текущие координаты
        temp_array = copy.deepcopy(self.new_obj.coords)
        if self.new_obj.rotate(self.blockarray) == 0:
            self.paint(temp_array,self.new_obj.coords,self.new_obj.color)
            self.master.after(self.speed,self.downObj,e)
        else:
            print(self.new_obj.orient,self.new_obj.type)

    #окраска ячеек
    def paint(self,old_points,new_points,color):
        for item in old_points:
            self.canv.itemconfig(item,fill="white")
        for item in new_points:
            self.canv.itemconfig(item,fill=color)

    def new_game(self):
        self.blockarray = []
        self.canv.delete('all')
        #добавление игровых полей пользователя и компьютера
        #создание поля для пользователя
        #перебор строк
        for i in range(16):
            #перебор столбцов
            for j in range(10):
                xn = j*self.gauge + (j+1)*self.indent
                xk = xn + self.gauge
                yn = i*self.gauge + (i+1)*self.indent
                yk = yn + self.gauge
                #добавление прямоугольника на холст с тегом в формате:
                #префикс_строка_столбец
                self.canv.create_rectangle(xn,yn,xk,yk,tag = str(i)+"_"+str(j))
        self.new_obj = Tetris(randrange(self.fig_count))
        self.paint(self.new_obj.coords,self.new_obj.coords,self.new_obj.color)