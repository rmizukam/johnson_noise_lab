import numpy as np
from Trial_Data import Trial_Data
from scipy.optimize import curve_fit
import math
import matplotlib.pyplot as plt
from Plotting_Fitting_Macros import linerrplt,errpropaddsubtract,pdiff,printkbr
from Gain_Data import Gain_Data
import Temp_Depend as Temp_Depend
kb_true = 1.38064852E-23 # m^2 * kg * s^-2 * K^-1
del_f = 110961 #hz
temperature_of_room = 293 # Kelvin

x = np.array([100, 10, 1])
y = np.array([1.8315374787953484e-13, 2.3431525657312636e-14,\
    5.375970101756927e-15])
yer = np.array([4.39205230578942e-15, 4.39205230578942e-15,\
    6.5880784586841286e-15])
m,b,dm,db,f1 = linerrplt(1,'Johnson Noise vs Resistance: Log-Log Scale',\
    'Resistance [$\Omega$]','<$V_j^2$> [$v^2$]', 'log','log',x,y,yer,'y')
m,b,dm,db,f2 = linerrplt(2,'Johnson Noise vs Resistance: Linear Scale',\
    'Resistance [$\Omega$]','<$V_j^2$> [$v^2$]', 'linear','linear',x,y,yer,'y')
denom = 4*temperature_of_room*del_f
printkbr(m,dm,denom)

x = np.array([99900,99700,99000,32000,32900,9900,9000,2300,3200])
y = np.array([2.57000000e-11,2.56777778e-11,2.55111111e-11,5.94892089e-12,\
    8.34567901e-12,1.81913580e-12,1.58827161e-12,3.40603618e-13,\
    5.94307322e-13])
yer = np.array([6.21129994e-14,9.31694991e-14,9.31694991e-14,5.52255614e-14,\
    6.90144437e-14,2.07043331e-14,1.38028887e-14,3.58535832e-15,\
    1.72810417e-14])
m,b,dm,db,f3 = linerrplt(3,'Johnson Noise vs ($f_1 - f_2$)', 'Frequency [Hz]',\
    '$<V_J^2>$ [$V^2$]','linear','linear',x,y,yer,'y')
denom = 4*temperature_of_room*10000
printkbr(m,dm,denom)
print('percent diff freq = ', abs(9997-9025) / ((9997+9025)/2)*100)

x = np.array([110961,110739,109961,35543,36543,10996,9997,2576,3554])
y = np.array([1.8912320414546205e-11, 1.8890098192323978e-11,\
    1.8723431525657315e-11, 5.952476403007196e-12, 6.1500072672047295e-12,\
    1.820089821960613e-12, 1.5892256244297488e-12, 3.407709860742579e-13,\
    5.944746897779617e-13])
yer = np.array([1.3040596561669184e-14, 1.9051466958009287e-14,\
    1.9051466958009287e-14, 1.1121128721112227e-14, 1.3866023570428908e-14,\
    4.192989632217931e-15, 2.8381640480502557e-15, 8.705832370161745e-16,\
    3.4912890804492292e-15])
m,b,dm,db,f4 = linerrplt(4,'Johnson Noise vs Equivalent Noise Bandwidth',\
    'Frequency [Hz]','$<V_J^2>$ [$V^2$]','linear','linear',x,y,yer,'y')
printkbr(m,dm,denom)

print('percent diff kb_t = ', abs(1.23e-23-kb_true) / ((kb_true+1.23e-23)/2)*100)

x = np.array([994.419,967.032,944.477,921.305,897.616,873.417,848.864,823.964,\
    798.691,773.213,747.485,721.533,695.363,669.002,642.448,615.748,588.907,\
    561.837,534.655,507.311,497.881,452.258,424.465,396.645,368.731]) # mV
x = np.divide(x,1000)
y = np.array([77.320,90,100,110,120,130,140,150,160,170,180,190,200,210,220,\
    230,240,250,260,270,280,290,300,310,320]) # Kelvin
yer = np.array([0.001]*len(y))
m,b,dm,db,f5 = linerrplt(5,'Diode Calibration',\
    'Volts [V]','Temperature [Kelvin]','linear','linear',x,y,yer,'y')

xt = np.array([297.41174216,84.42128213, 102.52103313, 159.63751815])
yt = np.array([2.22764054e-12, 1.03129878e-12, 1.13973780e-12, 1.41868945e-12])
yert = np.array([1.95202325e-15, 3.86500603e-15, 4.21637021e-15, 3.29403923e-15])
m,b,dm,db,f6 = linerrplt(6,'Temperature Dependence of Johnson Noise',\
    'Temperature [Kelvin]','$<V_J^2>$ [$V^2$]','linear','linear',xt,yt,yert,'y')
denom = 4*10996*np.mean(x)
printkbr(m,dm,denom)
print('percent diff kb_t = ', abs(1.29e-23-kb_true) / ((kb_true+1.29e-23)/2)*100)

plt.close(f1)
plt.close(f2)
plt.close(f3)
plt.close(f4)
plt.close(f5)
plt.show()
