import copy

class Tetris():
    '''Класс для фигур тетриса'''

    #свойства
    #координаты фигуры
    coords = []
    #ориентация
    orient = 0
    #статус остановки
    halt = 0

    figures = [
        ["0_4","0_5","1_4","1_5"],
        ["0_3","0_4","0_5","0_6"]
    ]

    #конструктор класса: в зависимости от типа фигуры формирует массив точек фигуры
    def __init__(self,type):
        self.coords = []
        self.coords = copy.deepcopy(self.figures[type])

    #функция перемещения вниз
    def down(self,blockarray):
        #статус ошибки
        status = 0
        #проход по точкам фигуры
        for point in self.coords:
            if int(point.split("_")[0])+1 <= 15:
                new_point = str(int(point.split("_")[0])+1) + "_" + point.split("_")[1]
                if new_point in blockarray:
                    status += 1
                    break
            else:
                status += 1
                break
        if status == 0:
            for i in range(len(self.coords)):
                new_point = str(int(self.coords[i].split("_")[0])+1) + "_" + self.coords[i].split("_")[1]
                self.coords[i] = new_point
        return status


obj = Tetris(0)
print(obj.coords)

print(obj.down([]))
print(obj.coords)
print(obj.down(["3_5"]))
print(obj.coords)
