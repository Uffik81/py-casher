# -*- coding: utf-8 -*-
##### Форма запуска кассового места #####
import sys
import udevices.managerdevice as mdevice
import udevices.shtrihm 
import uforms.ufrmhelp as helpinfo
import uforms.ufrmauth as frmauth
from tkinter import *

def startForm():
    root = Tk()
    if sys.platform != 'linux2':
        root.wm_state('zoomed')
    else:
        root.wm_attributes('-zoomed', True)
    
    authFrm = frmauth.FrmAuth(root)
    root.mainloop()

if __name__ == "__main__":
    #listdev = mdevice.UmanagerDevices()
    #helpinfo.showinfo()
    startForm()
    pass