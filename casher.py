# -*- coding: utf-8 -*-
##### Форма запуска кассового места #####
import sys
import udevices.managerdevice as mdevice
import udevices.shtrihm 
import uforms.ufrmhelp as helpinfo 


if __name__ == "__main__":
    listdev = mdevice.UmanagerDevices()
    helpinfo.showinfo()
    pass