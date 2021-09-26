# PlottingAndFittingMacros
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import math

from scipy.optimize.nonlin import _array_like

def lin_func(x,b,m):
    y = b + m * x
    return y

def linerrplt(fig_num,title,xlabel,ylabel,xscale,yscale,xdata,ydata,yerror,plot_color,fit_color):
    plt.figure(fig_num)
    plt.xlabel(xlabel, fontsize = 16)
    plt.ylabel(ylabel, fontsize = 16)
    plt.title(title, fontsize = 16)
    plt.xscale(xscale)
    plt.yscale(yscale)
    plt.errorbar(xdata,ydata,yerror,fmt='.',c=plot_color)
    ans, cov = curve_fit(lin_func, xdata, ydata, sigma = yerror)
    fit_b = ans[0]
    fit_m = ans[1]
    fit_x_span = np.arange(0, (np.amax(xdata)+1))
    plt.plot(fit_x_span, lin_func(fit_x_span, fit_b, fit_m), c = fit_color)
    del_fit_b = math.sqrt(cov[0][0])
    del_fit_m = math.sqrt(cov[1][1])
    return fit_m, fit_b, del_fit_m, del_fit_b

def errpropdiv(x,y,dx,dy):
    if type(x) == np.ndarray:
        array = [0] * len(x)
        for t in range(0, len(x)):
            array[t] = abs(x[t]/y[t]) * math.sqrt((dx[t]/x[t])**2 + (dy[t]/y[t])**2)
        return array
    elif type(x) == int: 
        return abs(x/y) * math.sqrt((dx/x)**2 + (dy/y)**2)
    else:
        print('You Passed Unuseable Data (errpropdiv)')

def errpropmultiply(x, y, dx, dy):
    if type(x) == np.ndarray:
        array = [0]*len(x)
        for t in range(0,len(x)):
            array[t] = len(x[t]*y[t]) * math.sqrt((dx[t]/x[t])**2 + (dy[t]/y[t])**2)
        return array
    elif type(x) == int:
        return abs(x*y) * math.sqrt((dx/x)**2 + (dy/y)**2)
    else:
        print('You Passed Unsuable Data (errpropmultiply)')

def errpropaddsubtract(dx,dy):
    if len(dx) != len(dy):
        yy = [dy]*len(dx)
        array = [0]*len(dx)
        for x in range(0,len(dx)):
            xx = dx[x]**2
            yy = dy[x]**2
            array[x] = math.sqrt(xx + yy)
    return array 

def errconst(c,x):
    return abs(c*x)

def errpow(x,dx,pow_factor):
    if type(x) == np.ndarray:
        array = [0]*len(x)
        for t in range(0,len(x)):
            array[t] = abs(pow_factor[t]) * x[t]^(pow_factor[t] - 1) * dx[t]
        return array
    elif type(x) == np.ndarray:
        return abs(pow_factor) * x^(pow_factor - 1) * dx
    else:
        print('You Passed Unuseable Data (errpow)')

def uncertinmean(data):
    return (np.amax(data) - np.amin(data))/(2*math.sqrt(len(data)))
