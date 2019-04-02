# -*- coding: utf-8 -*-
#-----------------------------
# Форма авторизации польбзхователя
# вер: 0.1

import sys  # sys нужен для передачи argv в QApplication
from tkinter import Tk, Frame, BOTH, Toplevel, Button, Entry

class frameAuth(Frame):
    def __init__(self, parent):
        
        Frame.__init__(self, parent, )   
        self.parent = parent
        self.initUI()

    def initUI(self):
        txtAuth = Entry(self.parent,width=20,bd=3)
        btnAuth = Button(self.parent,text='Авторизация',command=self.EnterAuth)
        
        #self.btnAuth.
        txtAuth.pack()
        btnAuth.pack()
        self.pack(fill=BOTH, expand=1)   

    def EnterAuth(self):
        self.parent.exit()

class FrmAuth(Toplevel):
    def __init__(self,parent):
        super().__init__(parent)
        self.initUI()
    
    def initUI(self):
        self.title('Авторизация')
        self.geometry('300x300') 
        self.resizable(False, False)
        self.grab_set()
        self.focus_set()
        frameAuth(self)
 
        