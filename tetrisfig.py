import copy

class Tetris():
    '''Класс для фигур тетриса'''

    #свойства

    #координаты фигуры (массив с точками объекта)
    coords = []
    #ориентация
    orient = 0
    #статус остановки
    halt = 0

    #свойство - двумерный массив, содержащий все точки типовых фигур
    figures = [
        ["0_4","0_5","1_4","1_5"],
        ["0_3","0_4","0_5","0_6"]
    ]

    #конструктор класса: в зависимости от типа фигуры формирует массив точек фигуры
    def __init__(self,type):
        self.coords = []
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


new_obj = Tetris(1)
print(new_obj.coords)
print(new_obj.down([]))
print(new_obj.coords)
print(new_obj.down(["2_4"]))
print(new_obj.coords)
