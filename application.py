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
        #вызов функции создания холста
        self.createCanvas()

    #добавление холста на окно
    def createCanvas(self):
        self.canv = Canvas(self)
        self.canv["height"] = self.height
        self.canv["width"] = self.width
        self.canv["bg"] = self.bg
        self.canv.pack()
        self.master.bind("<Down>",self.downObj)
        #клик по холсту вызывает функцию play


    def downObj(self,e):
        #скопировать текущие координаты
        temp_array = copy.deepcopy(self.new_obj.coords)
        if self.new_obj.down(self.blockarray) == 0:
            print("hello")
            self.paint(temp_array,self.new_obj.coords)
            self.master.after(100,self.downObj,e)


    #окраска ячеек
    def paint(self,old_points,new_points):
        for item in old_points:
            self.canv.itemconfig(item,fill="white")
        for item in new_points:
            self.canv.itemconfig(item,fill="black")

    def new_game(self):
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
        self.new_obj = Tetris(randrange(3))
        self.paint(self.new_obj.coords,self.new_obj.coords)