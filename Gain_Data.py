import numpy as np
import math
import matplotlib.pyplot as plt

class Gain_Data:
    def __init__(self, rmsin,rmsout,del_rmsin, del_rmsout):
        self.rmsin = rmsin
        self.rmsout = rmsout
        self.drmsin = del_rmsin
        self.drmsout = del_rmsout

    def gain(self):
        if type(self.rmsin)==np.ndarray and type(self.rmsout)==np.ndarray:
            return np.divide(self.rmsout, self.rmsin)
        elif type(self.rmsin)==int or type(self.rmsin)==np.float64 and\
            type(self.rmsout)==int or type(self.rmsout)==np.float64:
            return self.rmsout / self.rmsin

    def del_gain(self):
        if type(self.drmsin)==np.ndarray and type(self.drmsout)==np.ndarray:
            array = []*len(self.drmsin)
            for t in range(0, len(del_rmsin)):
                array[x] = math.sqrt((self.drmsin[x]**2)+(self.drmsout[x]**2))
            return array
        elif type(self.drmsin)==int or type(self.drmsin)==np.float64 and\
            type(self.drmsout)==int or type(self.drmsout)==np.float64:
            return math.sqrt(self.drmsin**2 + self.drmsout**2)

    def del_plot(self,fignum,title,xlabel,ylabel,xscale,yscale,xdata,ydata,yerr):
        plt.figure(fignum)
        plt.xlabel(xlabel, fontsize = 12)
        plt.ylabel(ylabel, fontsize = 12)
        plt.title(title, fontsize = 12)
        plt.xscale(xscale)
        plt.yscale(yscale)
        plt.errorbar(xdata,ydata,yerr,fmt='.',c='c')
