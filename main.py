from application import *

#инициализация окна
root = Tk()
root.title = "ТЕТРИС"
root.geometry("500x520+200+100")



#инициализация приложения
app = Application(master=root)
app.mainloop()
