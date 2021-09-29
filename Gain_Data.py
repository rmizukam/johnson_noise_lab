import numpy as np
import math
import matplotlib.pyplot as plt
from scipy import integrate

class Gain_Data:
    def __init__(self,freq,rmsin,rmsout,del_rmsin,del_rmsout):
        self.freq = freq
        self.rmsin = rmsin
        self.rmsout = rmsout
        self.drmsin = del_rmsin
        self.drmsout = del_rmsout

    def gain(self):
        if type(self.rmsin)==list and type(self.rmsout)==list:
            x = np.array(self.rmsout)
            y = np.array(self.rmsin)
            return np.divide(x, y)
        elif type(self.rmsin)==int or type(self.rmsin)==np.float64 and\
            type(self.rmsout)==int or type(self.rmsout)==np.float64:
            return self.rmsout / self.rmsin

    def dgain(self):
        if type(self.rmsin)==list and type(self.rmsout)==list\
            and type(self.drmsin)==list and type(self.drmsout)==list:
            x = np.array(self.rmsout) # type(x) = np.ndarray != list
            y = np.array(self.rmsin)
            dx = np.array(self.drmsout)
            dy = np.array(self.drmsin)
            array = [0] * len(x)
            for t in range(0, len(x)):
                array[t] = abs(x[t]/y[t]) * math.sqrt((dx[t]/x[t])**2 +\
                    (dy[t]/y[t])**2)
            return np.array(array)
        elif type(self.rmsout) == int or type(self.rmsout) == np.float64:
            return abs(self.rmsout/self.rmsin)*\
                math.sqrt((self.drmsout/self.rmsout)**2+\
                (self.drmsin/self.rmsin)**2)
        else:
            print('You Passed Data Unusable For dgain')

    def g2(self):
        x = self.gain()
        return np.power(x,2)

    def dg2(self):
        if type(self.gain())==np.ndarray and type(self.dgain())==np.ndarray:
            x=self.gain()
            y=self.gain()
            dx=self.dgain()
            dy=self.dgain()
            array = [0] * len(x)
            for t in range(0, len(x)):
                array[t] = abs(x[t]/y[t]) * math.sqrt((dx[t]/x[t])**2 +\
                    (dy[t]/y[t])**2)
            return np.array(array)
        elif type(self.gain()) == int or type(self.gain()) == np.float64:
            return abs(self.gain()/self.gain())*\
                math.sqrt((self.dgain()/self.gain())**2+\
                (self.dgain()/self.gain())**2)
        else:
            print('You Passed Data Unusable For dgain')

    def area_under_curve(self):
        return integrate.simps(self.g2(), self.freq)


    def del_plot(self,fignum,title,xlabel,ylabel,xscale,yscale,xdata,ydata,yer):
        figname = plt.figure(fignum)
        plt.xlabel(xlabel, fontsize = 12)
        plt.ylabel(ylabel, fontsize = 12)
        plt.title(title, fontsize = 12)
        plt.xscale(xscale)
        plt.yscale(yscale)
        plt.errorbar(xdata, ydata, yer, fmt='.',c='c')
        return figname
