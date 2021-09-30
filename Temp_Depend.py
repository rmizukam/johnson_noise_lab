import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def lin_eqn(x,intercept,slope):
    y = intercept + slope *x
    return y

def error(self,data):
    return (np.amax(data) - np.amin(data)) /\
        2*math.sqrt(len(data))*10 / 600**2 / self.gain**2

def eaddsub(dx,dy):
    array = [0]*len(dx)
    for t in range(0,len(dx)):
        array[t] = math.sqrt(dx[t]**2 + dy**2)
    return array

class Temp_Depend:
    def __init__(self,tdiode,vdiode,d_vout,ra_val,rb_val,rc_val,gain,vout_ra,\
        vout_rb,vout_rc,i1,i10):
        # valuess to be given in an array from lowest temp to highest
        self.f1 = 1000
        self.f2 = 10000
        self.g1 = 600
        self.tempread = tdiode
        self.vout_diode = vdiode
        self.dvout = d_vout
        self.ra =ra_val
        self.rb = rb_val
        self.rc = rc_val
        self.c1 = i1
        self.c10 = i10
        self.g = gain

    def diode_calibration(self,fignum,title,xlabel,ylabel,xdata,ydata,yer):
        figname = plt.figure(fignum)
        plt.xlabel(xlabel, fontsize = 12)
        plt.ylabel(ylabel, fontsize = 12)
        plt.title(title, fontsize = 12)
        plt.rcParams["figure.figsize"] = (15,10)
        plt.xticks(fontsize=16)
        plt.yticks(fontsize=16)
        plt.errorbar(xdata, ydata, yer, fmt='.',c='c')
        return figname

    def plot_calibration(self,fignum):
        figname = plt.figure(fignum)
        plt.xlabel('Volts [V]', fontsize = 18)
        plt.ylabel('Temperature [Kelvin]', fontsize = 18)
        plt.title('Diode Calibration', fontsize = 18)
        plt.rcParams["figure.figsize"] = (15,10)
        plt.xticks(fontsize=16)
        plt.yticks(fontsize=16)
        plt.errorbar(self.vout_diode,self.tempread,self.dvout, fmt='.', c='c')
        ans, cov = curve_fit(lin_eqn,self.vout_diode,self.temp_diode,\
            sigma=self.dvout)
        fit_m = ans[1]
        fit_b = ans[0]
        t = np.arange(0.3,1.1,0.01)
        plt.plot(t,lin_eqn(t,fit_b,fit_m), label='model', c = 'r')
        plt.plot(self.vout_diode,self.temp_diode,c='r',\
            marker='o',linestyle='None',markersize=5)
        fit_db = math.sqrt(cov[0][0])
        fit_dm = math.sqrt(cov[1][1])
        return figname, fit_m, fit_b, fit_dm, fit_db

    def our_temps(self,v_diode_m,v_diode_b):
        temp1 = v_diode_m * self.c1[0] + v_diode_b
        temp2 = v_diode_m * self.c1[1] + v_diode_b
        temp3 = v_diode_m * self.c1[2] + v_diode_b
        temp4 = v_diode_m * self.c1[3] + v_diode_b
        return np.array([temp1, temp2, temp3, temp4])

    def cor_data_using_ra(self):
        rac = np.array([\
            (np.mean(self.vout_ra[0:4])*10/(self.gain[0]**2)),\
            (np.mean(self.vout_ra[5:9])*10/(self.gain[1]**2)),\
            (np.mean(self.vout_ra[10:14])*10/(self.gain[2]**2)),\
            (np.mean(self.vout_ra[15:19])*10/(self.gain[3]**2))])
        rac = np.divide(rac,(self.g1**2))
        rbc = np.array([\
            (np.mean(self.vout_rb[0:4])*10/(self.gain[4]**2)),\
            (np.mean(self.vout_rb[5:9])*10/(self.gain[5]**2)),\
            (np.mean(self.vout_rb[10:14])*10/(self.gain[6]**2)),\
            (np.mean(self.vout_rb[15:19])*10/(self.gain[7]**2))])
        rbc = np.divide(rbc,(self.g1**2))
        rbc = np.subtract(rbc,rac)
        rcc = np.array([\
            np.mean(self.vout_rc[0:4])*10/(self.gain[8]**2),\
            np.mean(self.vout_rc[5:9])*10/(self.gain[9]**2),\
            np.mean(self.vout_rc[10:14])*10/(self.gain[10]**2),\
            np.mean(self.vout_rc[15:19])*10/(self.gain[11]**2)])
        rcc = np.divide(rcc,(self.g1**2))
        rcc = np.subtract(rcc,rac)
        return rbc, rcc



    def cor_delta(self):
        drac = np.array([\
            (error(self.vout_ra[0:4])*10/(self.gain[0]**2)),\
            (error(self.vout_ra[5:9])*10/(self.gain[1]**2)),\
            (error(self.vout_ra[10:14])*10/(self.gain[2]**2)),\
            (error(self.vout_ra[15:19])*10/(self.gain[3]**2))])
        drac = np.divide(drac,(self.g1**2))
        drbc = np.array([\
            (error(self.vout_rb[0:4])*10/(self.gain[4]**2)),\
            (error(self.vout_rb[5:9])*10/(self.gain[5]**2)),\
            (error(self.vout_rb[10:14])*10/(self.gain[6]**2)),\
            (error(self.vout_rb[15:19])*10/(self.gain[7]**2))])
        drbc = np.divide(drbc,(self.g1**2))
        drcc = np.array([\
            (error(self.vout_rc[0:4])*10/(self.gain[8]**2)),\
            (error(self.vout_rc[5:9])*10/(self.gain[9]**2)),\
            (error(self.vout_rc[10:14])*10/(self.gain[10]**2)),\
            (error(self.vout_rc[15:19])*10/(self.gain[11]**2))])
        drcc = np.divide(drcc,(self.g1**2))
        cdrbc = eaddsub(drac,drbc)
        cdrcc = eaddsub(drac,drcc)
        return cdrbc, cdrcc

    def linplot(fig_num, title, xlabel, ylabel, xscale, yscale, xdata,\
            ydata, yerror, show_fit):
        fig_name= plt.figure(fig_num, figsize=(12,8))
        plt.xlabel(xlabel, fontsize = 16)
        plt.ylabel(ylabel, fontsize = 16)
        plt.title(title, fontsize = 18)
        plt.xscale(xscale)
        plt.yscale(yscale)
        plt.xticks(fontsize=16)
        plt.yticks(fontsize=16)
        plt.errorbar(xdata,ydata,yerror,fmt='none', c='c')
        ans, cov = curve_fit(lin_func, xdata, ydata, sigma = yerror)
        fit_b = ans[0]
        fit_m = ans[1]
        fit_x_span = np.arange(0, (np.amax(xdata)+1))
        del_fit_b = math.sqrt(cov[0][0])
        del_fit_m = math.sqrt(cov[1][1])
        if show_fit == 'y' or show_fit == 'yes':
            plt.plot(fit_x_span, lin_func(fit_x_span, fit_b, fit_m), c = 'orange')
        plt.plot(xdata,ydata,c='r', marker='o',linestyle='None',markersize=5)
        return fit_m, fit_b, del_fit_m, del_fit_b, fig_name
