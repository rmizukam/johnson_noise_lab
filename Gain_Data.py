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

    def errpropdiv(x,y,dx,dy):
        if type(x) == np.ndarray:
            array = [0] * len(x)
            for t in range(0, len(x)):
                array[t] = abs(x[t]/y[t]) * math.sqrt((dx[t]/x[t])**2 +\
                    (dy[t]/y[t])**2)
            return array
        elif type(x) == int or type(x) == np.float64:
            return abs(x/y) * math.sqrt((dx/x)**2 + (dy/y)**2)
        else:
            print('You Passed Data Unusable For This Program')

    def del_plot(self,fignum,title,xlabel,ylabel,xscale,yscale,xdata,ydata,yerr):
        plt.figure(fignum)
        plt.xlabel(xlabel, fontsize = 12)
        plt.ylabel(ylabel, fontsize = 12)
        plt.title(title, fontsize = 12)
        plt.xscale(xscale)
        plt.yscale(yscale)
        plt.errorbar(xdata,ydata,yerr,fmt='.',c='c')
