__author__ = 'Александр'

from tkinter import *
import copy
from random import randrange
from tkinter.messagebox import *

#массив заполненных точек
all_block_points = []
#идентификатор анамации
id_after = 0

#окраска точек фигуры
def paint(type):
    global current_fig_points,current_fig_type
    for k in current_fig_points:
        canv.itemconfig(str(k[0])+"_"+str(k[1]),fill=type)

def new_figure():
    global current_fig_points,current_fig_type,current_fig_rotate
    #случайная первая фигура
    anyfigure = randrange(1,6)
    if anyfigure == 1:
        #если случайная переменная равна 1, то текущей фигурой будет палка
        current_fig_points = copy.deepcopy(palka)
    elif anyfigure == 2:
        current_fig_points = copy.deepcopy(box)
    elif anyfigure == 3:
        current_fig_points = copy.deepcopy(z_left)
    elif anyfigure == 4:
        current_fig_points = copy.deepcopy(z_right)
    elif anyfigure == 5:
        current_fig_points = copy.deepcopy(g_right)
    paint("black")
    #тип текущей фигуры
    current_fig_type = anyfigure
    #текущий угол поворота
    current_fig_rotate = 0
    #раскраска фигуры



def check_line():
    #статус окончания игры
    fin = 0
    lines = []
    #количество линий, которые надо убрать
    smesh = 0
    for i in range(16):
        s = 0
        for item in all_block_points:
            if item[1] == i:
                s += 1
        lines.append(s)
    print(lines)
    #закрасить все заблокированные точки в белый
    for k in all_block_points:
            canv.itemconfig(str(k[0])+"_"+str(k[1]),fill="white")
    cur_line = 15

    for i in range(len(lines)):
        #если в строке 10 заблокированных ячеек
        if lines[cur_line] == 10:
            #удалить текущие
            for j in range(10):
                print(cur_line,lines[cur_line])
                print("      ",j,cur_line)
                if [j,cur_line] in all_block_points:
                    all_block_points.remove([j,cur_line])
            #сдвинуть остальные координаты на одну строку ниже
            for k in all_block_points:
                if k[1] < cur_line:
                    k[1] += 1
            #передвинуть все суммы в массиве lines
            m = len(lines) - 1
            while m > 0:
                lines[m] = lines[m-1]
                m -= 1
            lines[0] = 0
        else:
            cur_line -= 1
    for k in all_block_points:
            canv.itemconfig(str(k[0])+"_"+str(k[1]),fill="black")
            #проверить, нет ли заблокированных точек на третьей строке. Если есть - GAME OVER
            if k[1] == 2:
                showinfo("TETRIS","GAME OVER")
                canv.delete('all')
                fin = 1
                print(k)
                break
    return fin


def checking(point):
    status = 0
    global all_block_points
    for k in all_block_points:
        if k[0]==point[0] and k[1]==point[1]:
            status = 1
            break
    return status

def left(e):
    #сообщаем функции, что информацию о текущей фигуре мы берём из главной программы
    global current_fig_points,current_fig_type
    #заливка текущих координат фигуры белым
    paint("white")
    #изменение координат
    #проверяем, не выйдет ли после изменения координат первая точка за левый край
    if current_fig_points[0][0] > 0:
        #изменить первую составляющию точек на -1
        for k in current_fig_points:
            k[0] -= 1
        #print(current_fig_points, current_fig_points[0][0])
    #окраска фигуры с новыми текущими координатами чёрным
    paint("black")

def right(e):
    global current_fig_points,current_fig_type
    paint("white")
    #проверить, есть ли точка, у которой столбец равен 9
    status = 0
    for l in range(len(current_fig_points)):
        #если есть точка с крайним правым столбцом, то статус = 1 и перемещать нельзя
        if current_fig_points[l][0] == 9:
            status = 1
    if status == 0:
        for k in current_fig_points:
            k[0] += 1
    paint("black")

def rotate(e):
    global current_fig_points,current_fig_type,current_fig_rotate
    root.after_cancel(id_after)
    #в зависимости от типа фигуры вращать её
    status = 0
    #массив временных значений
    temp_fig = []
    #копирование координат текущей фигуры во временный массив
    temp_fig = copy.deepcopy(current_fig_points)
    #палка из горизонтали в вертикаль
    #print(current_fig_rotate)
    #если текущая фигура - палка и статус поворота чётный
    if current_fig_type == 1 and current_fig_rotate%2==0:
        temp_fig[0][0] += 2
        #после изменения проверить, можно ли вращать
        temp_fig[0][1] -= 1
        temp_fig[1][0] += 1
        temp_fig[2][1] += 1
        temp_fig[3][0] -= 1
        temp_fig[3][1] += 2
    #палка из вертикали в горизонталь
    if current_fig_type == 1 and current_fig_rotate%2!=0:
        temp_fig[0][0] -= 2
        #после изменения проверить, можно ли вращать
        temp_fig[0][1] += 2
        temp_fig[1][0] -= 1
        temp_fig[1][1] += 1
        temp_fig[3][0] += 1
        temp_fig[3][1] -= 1
    if current_fig_type == 3 and current_fig_rotate%2==0:
        temp_fig[0][1] += 2
        temp_fig[3][0] -= 2
    if current_fig_type == 3 and current_fig_rotate%2!=0:
        temp_fig[0][1] -= 2
        temp_fig[3][0] += 2
    if current_fig_type == 4 and current_fig_rotate%2==0:
        temp_fig[0][0] += 2
        temp_fig[3][1] += 2
    if current_fig_type == 4 and current_fig_rotate%2!=0:
        temp_fig[0][0] -= 2
        temp_fig[3][1] -= 2
    if current_fig_type == 5 and current_fig_rotate%4==0:
        temp_fig[0][0] += 1
        temp_fig[0][1] += 2
        temp_fig[1][0] += 1
        temp_fig[1][1] += 2
    if current_fig_type == 5 and current_fig_rotate%4==1:
        temp_fig[2][0] -= 2
        temp_fig[2][1] += 2
        temp_fig[3][0] -= 2
    if current_fig_type == 5 and current_fig_rotate%4==2:
        temp_fig[0][0] -= 1
        temp_fig[0][1] -= 2
        temp_fig[1][0] -= 1
        temp_fig[1][1] -= 2
    if current_fig_type == 5 and current_fig_rotate%4==3:
        temp_fig[2][0] += 2
        temp_fig[2][1] -= 2
        temp_fig[3][0] += 2
    #проверка возможности поворота
    #1 - нет ли новой точки фигуры в массиве заблокированных точек
    #2 - не выходят ли точки после поворота за границы окна
    for k in temp_fig:
        #проверка наличия точки в массиве заблокированных
        status += checking(k)
    if status == 0:
        current_fig_rotate += 1
        paint("white")
        current_fig_points = copy.deepcopy(temp_fig)
        paint("black")
        down()

def down(e = ""):
    global current_fig_points,current_fig_type,current_fig_rotate,id_after,all_block_points
    fin = 0
    root.after_cancel(id_after)
    status = 0
    temp_fig = copy.deepcopy(current_fig_points)
    for k in range(len(current_fig_points)):
        temp_fig[k][1] += 1
        #проверка наличия точки в массиве заблокированных
        status += checking(temp_fig[k])
        #проверить, нет ли точек, у которых строка стала больше высоты
        if temp_fig[k][1]>15:
            #проверить, не столкнулись ли мы с полом
            status += 1
    if status == 0:
        paint("white")
        current_fig_points = copy.deepcopy(temp_fig)
        paint("black")
    else:
        #остановка фигуры
        #добавить в массив заблокированных точек точки фигуры
        #print(temp_fig,current_fig_points)
        for k in current_fig_points:
            all_block_points.append(k)
        #проверка линий и финиша
        if check_line() == 0:
            #сгенерировать новую фигуру
            new_figure()
        else:
            fin = 1
            root.after_cancel(id_after)
    if fin == 0:
        id_after = root.after(300,down,e)


def pausing(e):
    root.after_cancel(id_after)


root = Tk()
root.geometry("305x500+200+100")
root.title("TETRIS")

canv = Canvas(root, height=500,width=305,bg="white")
canv.pack()

#инициализация элементов
#палка - двумерный массив
palka = [[3,0],[4,0],[5,0],[6,0]]
box = [[4,0],[5,0],[4,1],[5,1]]
z_left = [[3,0],[4,0],[4,1],[5,1]]
z_right = [[3,1],[4,1],[4,0],[5,0]]
g_right = [[3,0],[4,0],[5,0],[5,1]]

#отрисовка поля (квадратов)
for i in range(10):
    for j in range(16):
        xn = i*30+2
        yn = j*30+2
        xk = xn + 30
        yk = yn + 30
        canv.create_rectangle(xn,yn,xk,yk,tag=str(i)+"_"+str(j),width=1,outline="gray")

new_figure()

#запуск анимации (функция down)
root.after(1000,down)

root.bind("<Return>",rotate)
root.bind("<Left>",left)
root.bind("<Right>",right)
root.bind("<Down>",down)
root.bind("<Escape>",pausing)

root.mainloop()