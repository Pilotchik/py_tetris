__author__ = 'Александр'

from random import randrange
from time import time
from tkinter import *
from tetrisfig import *
from tkinter.messagebox import *

class Application(Frame):
    '''
    Приложение. Наследует класс Frame. Создание окна, холста и всех функций для реализации приложения
    '''

    def __init__(self, master=None):
        #инициализация окна
        Frame.__init__(self, master)
        self.pack()

        #инициализация меню
        self.m = Menu(master)
        master.config(menu = self.m)
        self.m_play = Menu(self.m)
        self.m.add_cascade(label = "Игра",menu = self.m_play)
        self.m_play.add_command(label="Новая игра", command = self.new_game)
        #вызов функции создания холста
        #self.createCanvas()
