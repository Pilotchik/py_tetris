import copy

class Tetris():
    '''Класс для фигур тетриса'''

    #свойства

    #координаты фигуры (массив с точками объекта)
    coords = []
    #ориентация
    orient = 0
    #тип фигуры, который определяется при её инициализации
    type = 0

    #свойство - двумерный массив, содержащий все точки типовых фигур
    figures = [
        ["0_4","0_5","1_4","1_5"],
        ["0_3","0_4","0_5","0_6"]
    ]

    #конструктор класса: в зависимости от типа фигуры формирует массив точек фигуры
    def __init__(self,type):
        self.coords = []
        self.type = type
        #скопировать подмассив figures с индексом, который ввёл пользователь в массив coords
        self.coords = copy.deepcopy(self.figures[type])

    #функция перемещения вниз
    #входные значения - массив с заблокированными ячейками
    #выходные значения - статус возможности перемещения вниз. 0 - перемещение возможно, not(0) - невозможно
    def down(self,blockarray):
        #статус ошибки
        status = 0
        #проход по точкам фигуры
        for point in self.coords:
            #Этап 1. Проверка выхода строки, увеличенной на 1, за границы поля
            #point.split("_") - разбить строку формата строка_столбец на элементы массива,
            # если разделителем является нижнее подчёркивание
            if int(point.split("_")[0])+1 <= 15:
                #Этап 2. Проверка вхождения точки при увеличении строки в массив заблокированных ячеек
                #генерация точки с изменённой строкой
                new_point = str(int(point.split("_")[0])+1) + "_" + point.split("_")[1]
                #проверка присутствия точки в массиве заблокированных ячеек
                if new_point in blockarray:
                    status += 1
                    break
            else:
                status += 1
                break
        #если ошибок не было
        if status == 0:
            #перезаписать свойство объекта coords новыми точками
            for i in range(len(self.coords)):
                new_point = str(int(self.coords[i].split("_")[0])+1) + "_" + self.coords[i].split("_")[1]
                self.coords[i] = new_point
        return status

    #функция перемещения влево
    #входные значения - массив с заблокированными ячейками
    #выходные значения - статус возможности перемещения вниз. 0 - перемещение возможно, not(0) - невозможно
    def left(self,blockarray):
        #статус ошибки
        status = 0
        #проход по точкам фигуры
        for point in self.coords:
            #Этап 1. Проверка выхода строки, увеличенной на 1, за границы поля
            #point.split("_") - разбить строку формата строка_столбец на элементы массива,
            # если разделителем является нижнее подчёркивание
            if int(point.split("_")[1])-1 >= 0:
                #Этап 2. Проверка вхождения точки при увеличении строки в массив заблокированных ячеек
                #генерация точки с изменённой строкой
                new_point = point.split("_")[0] + "_" + str(int(point.split("_")[1])-1)
                #проверка присутствия точки в массиве заблокированных ячеек
                if new_point in blockarray:
                    status += 1
                    break
            else:
                status += 1
                break
        #если ошибок не было
        if status == 0:
            #перезаписать свойство объекта coords новыми точками
            for i in range(len(self.coords)):
                new_point = self.coords.split("_")[0] + "_" + str(int(self.coords.split("_")[1])-1)
                self.coords[i] = new_point
        return status

    #функция перемещения вправо
    #входные значения - массив с заблокированными ячейками
    #выходные значения - статус возможности перемещения вниз. 0 - перемещение возможно, not(0) - невозможно
    def right(self,blockarray):
        #статус ошибки
        status = 0
        #проход по точкам фигуры
        for point in self.coords:
            #Этап 1. Проверка выхода строки, увеличенной на 1, за границы поля
            #point.split("_") - разбить строку формата строка_столбец на элементы массива,
            # если разделителем является нижнее подчёркивание
            if int(point.split("_")[1])+1 <= 9:
                #Этап 2. Проверка вхождения точки при увеличении строки в массив заблокированных ячеек
                #генерация точки с изменённой строкой
                new_point = point.split("_")[0] + "_" + str(int(point.split("_")[1])+1)
                #проверка присутствия точки в массиве заблокированных ячеек
                if new_point in blockarray:
                    status += 1
                    break
            else:
                status += 1
                break
        #если ошибок не было
        if status == 0:
            #перезаписать свойство объекта coords новыми точками
            for i in range(len(self.coords)):
                new_point = self.coords.split("_")[0] + "_" + str(int(self.coords.split("_")[1])+1)
                self.coords[i] = new_point
        return status

    def rotate(self,blockarray):
        #возвращаемый методом статус (0 - всё хорошо, не 0 - всё плохо)
        status = 0
        temp_coords = copy.deepcopy(self.coords)
        #принцип:
        #1. создать копию массива точек текущей фигуры
        #2. в зависимости от типа и ориентации изменить её точки
        #3. проверить, все ли точки копии корректны (не выходят за границы и не пересекаются с заблокированными)
        #       если все точки корректны, то скопировать копию в оригинал обратно

        #если тип фигуры 0, то это квадрат и поэтому возвращать надо те же самые координаты
        if self.type == 0:
            status = 0
        else:
            #тип 1 - палка
            if self.type == 1:
                if self.orient == 0:
                    #изменить значение всех точек
                    temp_coords[0] = str(int(temp_coords[0].split("_")[0])-2)+"_"+str(int(temp_coords[0].split("_")[1])+2)
                    temp_coords[1] = str(int(temp_coords[1].split("_")[0])-1)+"_"+str(int(temp_coords[1].split("_")[1])+1)
                    temp_coords[3] = str(int(temp_coords[3].split("_")[0])+1)+"_"+str(int(temp_coords[3].split("_")[1])-1)
                #и так далее
            #проверка корректности точек
            for point in temp_coords:
                if point in blockarray:
                    status += 1
                    break
        if status == 0:
            #скопировать в оригинал копию
            self.coords = copy.deepcopy(temp_coords)
            if self.orient+1 < 4:
                self.orient += 1
            else:
                self.orient = 0


new_obj = Tetris(1)
print(new_obj.coords)
print(new_obj.down([]))
print(new_obj.coords)
print(new_obj.down(["2_4"]))
print(new_obj.coords)
