# PlottingAndFittingMacros
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import math


def lin_func(x,b,m):
    y = b + m * x
    return y

def linerrplt(fig_num,title, xlabel, ylabel, xscale, yscale, xdata,\
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
    fit_x_span = np.arange((np.amin(xdata)-0.1), (np.amax(xdata)+0.5))
    del_fit_b = math.sqrt(cov[0][0])
    del_fit_m = math.sqrt(cov[1][1])
    if show_fit == 'y' or show_fit == 'yes':
        plt.plot(fit_x_span, lin_func(fit_x_span, fit_b, fit_m), c = 'orange')
    plt.plot(xdata,ydata,c='r', marker='o',linestyle='None',markersize=4)
    return fit_m, fit_b, del_fit_m, del_fit_b, fig_name

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

def errpropmultiply(x, y, dx, dy):
    if type(x) == np.ndarray:
        array = [0]*len(x)
        for t in range(0,len(x)):
            array[t] = len(x[t]*y[t]) * math.sqrt((dx[t]/x[t])**2 +\
                (dy[t]/y[t])**2)
        return array
    elif type(x) == int or type(x) == np.float64:
        return abs(x*y) * math.sqrt((dx/x)**2 + (dy/y)**2)
    else:
        print('You Passed Data Unusable For This Program')

def errpropaddsubtract(dx,dy):
    if type(dx)== np.ndarray and type(dy)==np.ndarray:
        if len(dx) != len(dy):
            yy = [dy]*len(dx)
            array = [0]*len(dx)
            array = np.array(array)
        for t in range(0,len(dx)):
            xx = (dx[t])**2
            yy = (dy[t])**2
            array[t] = math.sqrt(xx + yy)
        return array
    elif type(dx) == np.ndarray and type(dy) == np.float64 or type(dy) == float:
         array = [dy] * len(dx)
         array = np.array(array)
         for t in range(0,len(dx)):
             xx = (dx[t])**2
             yy = (array[t])**2
             array[t] = math.sqrt(xx + yy)
         return array
    elif type(dx) != np.ndarray and type(dy) != np.ndarray:
        return math.sqrt(dx**2 + dy**2)

def errconst(c,x):
    return abs(c*x)

def errpow(x,dx,pow_factor):
    if type(x) == np.ndarray:
        array = [0]*len(x)
        for t in range(0,len(x)):
            array[t]
    elif type(x) == int or type(x) == np.float64:
        return abs(pow_factor) * x^(pow_factor - 1) * dx

def pdiff(x,y):
    return abs(x-y)/ ((x + y)/2)*100

def printkbr(m,dm,denom):
    kb_true = 1.38064852E-23 # m^2 * kg * s^-2 * K^-1
    del_f1 = 110961 #hz
    temperature_of_room = 293 # Kelvin
    kb = m / (denom)
    dkb = dm / (denom)
    print('Boltzmann Constant 1: ', kb, ' +/- ', dkb)
    print('% diff = ', pdiff(kb_true,kb))
    print('..................................................')

def uncertinmean(data):
    return (np.amax(data) - np.amin(data)) / (2*math.sqrt(len(data)))
