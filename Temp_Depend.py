import numpy as np
import math
import matplotib.pyplot as plt
from scipy.optimize import curve_fit

def lin_eqn(x,intercept,slope):
    y = intercept + slope *x
    return y

class Temp_Depend:
    def __init__(self, temp_diode, vout_diode,ra,rb,rc,gra,grb,grc,vout_ra,\
        vout_rb,vout_rc,current_1,current_10):
        self.f1 = 1000
        self.f2 = 10000
        self.g1 = 600
        self.tempread = np.array(temp_diode)
        self.vout_diode = np.divide((np.array(vout_diode)),1000)
        self.dvout = np.array([0.001]*len(vout_diode))
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

    def plot_calibration(self,fignum):
        figname = plt.figure(fignum)
        plt.xlabel('Volts [V]', fontsize = 12)
        plt.ylabel('Temperature [Kelvin]', fontsize = 12)
        plt.title('Diode Calibration', fontsize = 12)
        plt.errorbar(self.vout_diode,self.temp_diode,self.dvout, fmt='.', c='c')
        ans, cov = curve_fit(lin_eqn,self.vout_diode,self.temp_diode,\
            sigma=self.dvout)
        fit_m = ans[1]
        fit_b = ans[0]
        t = np.arange(0.3,1.1,0.01)
        plt.plot(t,lin_eqn(t,fit_b,fit_m), label='model', c = 'r')
        fit_db = math.sqrt(cov[0][0])
        fit_dm = math.sqrt(cov[1][1])
        return figname, fit_m, fit_b, fit_dm, fit_db
