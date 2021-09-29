import numpy as np
import matplotib.pyplot as plt

class Temp_Depend:
    def __init__(self, temp_diode, vout_diode,ra,rb,rc):
        self.f1 = 1000
        self.f2 = 10000
        self.g1 = 600
        self.tempread = np.array(temp_diode)
        self.vout_diode = np.divide(np.array(vout_diode),1000)
        self.ra = np.array(ra)
        self.rb = np.array(rb)
        self.rc = np.array(rc)

    def diode_calibration(self,fignum,title,xlabel,ylabel,xdata,ydata,yer):
        figname = plt.figure(fignum)
        plt.xlabel(xlabel, fontsize = 12)
        plt.ylabel(ylabel, fontsize = 12)
        plt.title(title, fontsize = 12)
        plt.errorbar(xdata, ydata, yer, fmt='.',c='c')
        return figname
