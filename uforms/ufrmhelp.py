# -*- coding: utf-8 -*-
#-----------------------------
# Форма отображает информацию о прилобении
# вер: 0.1

import sys  # sys нужен для передачи argv в QApplication
from tkinter import *

def showinfo():
    wndRoot = Tk()
    wndRoot.title("Информация о приложении!")
    wndRoot.geometry('600x400')
    wndRoot.mainloop()
    pass
