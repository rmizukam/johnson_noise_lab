# main
import numpy as np
from Trial_Data import Trial_Data
from scipy.optimize import curve_fit
import math
import matplotlib.pyplot as plt
from Plotting_Fitting_Macros import linerrplt,errpropaddsubtract

room_temp = 293 #Kelvin
kb_true = 1.38064852E-23 # m^2 * kg * s^-2 * K^-1

# Data for Noise vs Resistance
tri1 = Trial_Data(np.array([0.979, 0.980, 0.978, 0.977, 0.977]),1,2000,\
    np.array([100,100000,110961])) # raw_data, resistance, gain
tri2 = Trial_Data(np.array([0.981, 0.980, 0.982, 0.980, 0.981]),10,2000,\
    np.array([100,100000,110961]))
tri3 = Trial_Data(np.array([1.003, 1.004, 1.005, 1.003, 1.004]),100,2000,\
    np.array([100,100000,110961]))
tri4 = Trial_Data(np.array([0.702, 0.702, 0.703, 0.701, 0.702]),1000,1500,\
    np.array([100,100000,110961]))
tri5 = Trial_Data(np.array([0.924, 0.923, 0.923, 0.925, 0.926]),10000,1000,\
    np.array([100,100000,110961]))
tri6 = Trial_Data(np.array([0.874, 0.873, 0.872, 0.872, 0.871]),100000,400,\
    np.array([100,100000,110961]))
tri7 = Trial_Data(np.array([0.949, 0.952, 0.948, 0.949, 0.950]),1000000,300,\
    np.array([100,100000,110961]))

# Data for Noise vs Frequency
ftri1 = Trial_Data(np.array([0.926, 0.926,0.925, 0.924, 0.925]),10000,1000,\
    np.array([100, 100000, 110961])) #raw_data,resist,gain,highpass,lowpass,ENBW
ftri2 = Trial_Data(np.array([0.923, 0.924, 0.926, 0.924, 0.925]),10000,1000,\
    np.array([300, 100000, 110739]))
ftri3 = Trial_Data(np.array([0.920, 0.918, 0.918, 0.919, 0.917]),10000,1000,\
    np.array([1000, 100000, 109961]))
ftri4 = Trial_Data(np.array([0.660, 0.658, 0.659, 0.661, 0.662]),10000,1500,\
    np.array([1000, 33000, 35543]))
ftri5 = Trial_Data(np.array([0.679, 0.676, 0.675, 0.676, 0.674]),10000,1500,\
    np.array([100, 33000, 36543]))
ftri6 = Trial_Data(np.array([0.804, 0.807, 0.801, 0.803, 0.805]),10000,3000,\
    np.array([100, 10000, 10996]))
ftri7 = Trial_Data(np.array([0.729, 0.727, 0.730, 0.731, 0.729]),10000,3000,\
    np.array([1000, 10000, 9997]))
ftri8 = Trial_Data(np.array([0.729, 0.727, 0.730, 0.731, 0.729]),10000,6000,\
    np.array([1000, 3300, 2576]))
ftri9 = Trial_Data(np.array([1.06, 1.07, 1.06, 1.05, 1.05]),10000,6000,\
    np.array([100, 3300, 3554]))

# Data Used to correct the Frequency Trials
ftri4_1 = Trial_Data(np.array([0.712, 0.712, 0.713, 0.711, 0.713]),1,3000,\
    np.array([100, 100000, 110961]))
ftri4_10 = Trial_Data(np.array([0.713, 0.714, 0.713, 0.712, 0.713]),10,3000,\
    np.array([100, 100000, 110961]))
ftri4_100 = Trial_Data(np.array([0.728, 0.729, 0.732, 0.731, 0.730]),100,3000,\
    np.array([100, 100000, 110961]))
ftri4_1000 = Trial_Data(np.array([0.909, 0.907, 0.911, 0.909, 0.906]),1000,\
    3000, np.array([100, 100000, 110961]))
ftri6_1 = Trial_Data(np.array([0.861, 0.851, 0.861, 0.863, 0.856]),1,6000,\
    np.array([100, 10000, 10996]))
ftri6_10 = Trial_Data(np.array([0.864, 0.857, 0.856, 0.857, 0.858]),10,6000,\
    np.array([100, 10000, 10996]))
ftri6_100 = Trial_Data(np.array([0.881, 0.877, 0.8800, 0.884, 0.888]),100,6000,\
    np.array([100, 10000, 10996]))
ftri9_1 = Trial_Data(np.array([0.795, 0.798, 0.798, 0.800, 0.795]),1,10000,\
    np.array([100, 3300, 3554]))
ftri9_10 = Trial_Data(np.array([0.809, 0.802, 0.806, 0.803, 0.804]),10,10000,\
    np.array([100, 3300, 3554]))
ftri9_100 = Trial_Data(np.array([0.811, 0.827, 0.811, 0.825, 0.814]),100,10000,\
    np.array([100, 3300, 3554]))

tri1.m, tri1.b, tri1.dm, tri1.db, f1 = linerrplt(1,\
    'Correction Curve $\Delta$ f = 11kHz', 'Resistance $\Omega$',\
    '$<V_J^2 + V_N^2>$','linear','linear',\
    np.array([1,10,100]),\
    np.array([tri1.inferred, tri2.inferred, tri3.inferred]),\
    np.array([tri1.error(), tri2.error(), tri3.error()]),'yes')
tri2.m, tri2.b, tri2.dm, tri2.db = tri1.m, tri1.b, tri1.dm, tri1.db
tri3.m, tri3.b, tri3.dm, tri3.db = tri1.m, tri1.b, tri1.dm, tri1.db

m1, d1, dm1, db1, f2 = linerrplt(2,'Johnson Noise vs Resistance: Linear Scale',\
    'Resistance [$\Omega$]', '<$V_j^2$> [$v^2$]', 'linear', 'linear',\
    np.array([tri1.resistance, tri2.resistance, tri3.resistance]),\
    np.array([tri1.corrected_data(),tri2.corrected_data(),\
    tri3.corrected_data()]),\
    np.array([tri1.corrected_del(),tri2.corrected_del(),tri3.corrected_del()]),\
    'yes')
print('kb_noise_vs_r',(m1 / 4/room_temp/tri1.enbw))

ml1, bl1, dml1, dbl1, f3 = linerrplt(3,\
    'Johnson Noise vs Resistance: Logarithmic Scale', 'Resistance [$\Omega$]',\
    '<$V_j^2$> [$v^2$]', 'log', 'log',\
    np.array([tri1.resistance, tri2.resistance, tri3.resistance]),\
    np.array([tri1.corrected_data(),tri2.corrected_data(),\
    tri3.corrected_data()]),\
    np.array([tri1.corrected_del(),tri2.corrected_del(),tri3.corrected_del()]),\
    'yes')
print('kb_noise_vs_r_log', (ml1/4/room_temp/tri1.enbw))


ftri4.m, ftri4.b, ftri4.dm, ftri4.db, f4 = linerrplt(4,\
    'Correction for frequency band = 25kHz', 'Resistance [$\Omega$]',\
    '$<V_j^2$ + $V_N^2> [V^2]$', 'linear', 'linear',\
    np.array([ftri4_1.resistance, ftri4_10.resistance, ftri4_100.resistance]),\
    np.array([ftri4_1.inferred,ftri4_10.inferred, ftri4_10.inferred]),\
    np.array([ftri4_1.error(),ftri4_10.error(), ftri4_100.error()]), 'yes')
ftri4_1.m, ftri4_1.b, ftri4_1.dm, ftri4_1.db = \
    ftri4.m, ftri4.b, ftri4.dm, ftri4.db
ftri4_10.m, ftri4_10.b, ftri4_10.dm, ftri4_10.db = \
    ftri4.m, ftri4.b, ftri4.dm, ftri4.db
ftri4_100.m, ftri4_100.b, ftri4_100.dm, ftri4_100.db = \
    ftri4.m, ftri4.b, ftri4.dm, ftri4.db
ftri4_1000.m, ftri4_1000.b, ftri4_1000.dm, ftri4_1000.db = \
    ftri4.m, ftri4.b, ftri4.dm, ftri4.db

ftri6.m, ftri6.b, ftri6.dm, ftri6.db, f5 = linerrplt(5,\
    'Correction for frequency band = 11kHz', 'Resistance [$\Omega$]',\
    '$<V_j^2$ + $V_N^2> [V^2]$', 'linear', 'linear',\
    np.array([ftri6_1.resistance, ftri6_10.resistance, ftri6_100.resistance]),\
    np.array([ftri6_1.inferred,ftri6_10.inferred, ftri6_10.inferred]),\
    np.array([ftri6_1.error(),ftri6_10.error(), ftri6_10.error()]), 'yes')
ftri7.m, ftri7.b, ftri7.dm, ftri7.db = ftri6.m, ftri6.b, ftri6.dm, ftri6.db

ftri9.m, ftri9.b, ftri9.dm, ftri9.db, f6 = linerrplt(6,\
    'Correction for frequency band = 10kHz', 'Resistance [$\Omega$]',\
    '$<V_j^2$ + $V_N^2> [V^2]$', 'linear', 'linear',\
    np.array([ftri9_1.resistance, ftri9_10.resistance, ftri9_100.resistance]),\
    np.array([ftri9_1.inferred,ftri9_10.inferred, ftri9_10.inferred]),\
    np.array([ftri9_1.error(),ftri9_10.error(), ftri9_10.error()]), 'yes')
ftri8.m, ftri8.b, ftri8.dm, ftri8.db = ftri9.m, ftri9.b, ftri9.dm, ftri9.db

correct_freq_data = np.array([ftri1.corrected_data(), ftri2.corrected_data(),\
    ftri3.corrected_data(),ftri4.corrected_data(),ftri5.corrected_data(),\
    ftri6.corrected_data(),ftri7.corrected_data(),ftri8.corrected_data(),\
    ftri9.corrected_data()])

correct_freq_del = np.array([ftri1.corrected_del(),ftri2.corrected_del(),\
    ftri3.corrected_del(),ftri4.corrected_del(),ftri5.corrected_del(),\
    ftri6.corrected_del(),ftri7.corrected_del(),ftri8.corrected_del(),\
    ftri9.corrected_del()])

hpm, hpb, dhpm, dhpb, f7 = linerrplt(7,\
    'Relationship of Johnson Noise and High Pass Cut Off Frequency',\
    'Frequency [Hz]','$<V_j^2> [V^2]$', 'linear', 'linear',\
    np.array([ftri1.hp,ftri2.hp,ftri3.hp,ftri4.hp,ftri5.hp,ftri6.hp,ftri7.hp,\
        ftri8.hp,ftri9.hp]),\
    np.array([ftri1.corrected_data(), ftri2.corrected_data(),\
        ftri3.corrected_data(),ftri4.corrected_data(),ftri5.corrected_data(),\
        ftri6.corrected_data(),ftri7.corrected_data(),ftri8.corrected_data(),\
        ftri9.corrected_data()]),\
    np.array([ftri1.corrected_del(),ftri2.corrected_del(),\
        ftri3.corrected_del(),ftri4.corrected_del(),ftri5.corrected_del(),\
        ftri6.corrected_del(),ftri7.corrected_del(),ftri8.corrected_del(),\
        ftri9.corrected_del()]), 'yes')

lpm, lpb, dlpm, dlpb, f8 = linerrplt(8,\
    'Relationship of Johnson Noise and Low Pass Cut Off Frequency',\
    'Frequency [Hz]','$<V_j^2> [V^2]$', 'linear', 'linear',\
    np.array([ftri1.lp,ftri2.lp,ftri3.lp,ftri4.lp,ftri5.lp,ftri6.lp,ftri7.lp,\
        ftri8.lp,ftri9.lp]),\
    np.array([ftri1.corrected_data(), ftri2.corrected_data(),\
        ftri3.corrected_data(),ftri4.corrected_data(),ftri5.corrected_data(),\
        ftri6.corrected_data(),ftri7.corrected_data(),ftri8.corrected_data(),\
        ftri9.corrected_data()]),\
    np.array([ftri1.corrected_del(),ftri2.corrected_del(),\
        ftri3.corrected_del(),ftri4.corrected_del(),ftri5.corrected_del(),\
        ftri6.corrected_del(),ftri7.corrected_del(),ftri8.corrected_del(),\
        ftri9.corrected_del()]), 'yes')

dim, dib, ddim, ddib, f9 = linerrplt(9,\
    'Johnson Noise vs ($f_2 - f_1$)',\
    'Frequency [Hz]','$<V_j^2> [V^2]$', 'linear', 'linear',\
    np.array([ftri1.diff,ftri2.diff,ftri3.diff,ftri4.diff,ftri5.diff,\
        ftri6.diff,ftri7.diff,ftri8.diff,ftri9.diff]),\
    np.array([ftri1.corrected_data(), ftri2.corrected_data(),\
        ftri3.corrected_data(),ftri4.corrected_data(),ftri5.corrected_data(),\
        ftri6.corrected_data(),ftri7.corrected_data(),ftri8.corrected_data(),\
        ftri9.corrected_data()]),\
    np.array([ftri1.corrected_del(),ftri2.corrected_del(),\
        ftri3.corrected_del(),ftri4.corrected_del(),ftri5.corrected_del(),\
        ftri6.corrected_del(),ftri7.corrected_del(),ftri8.corrected_del(),\
        ftri9.corrected_del()]), 'yes')

enbwm, enbwb, denbwm, denbwb, f10 = linerrplt(10,\
    'Johnson Noise vs Effective Noise Bandwidth',\
    'Frequency [Hz]','$<V_j^2> [V^2]$', 'linear', 'linear',\
    np.array([ftri1.enbw,ftri2.enbw,ftri3.enbw,ftri4.enbw,ftri5.enbw,\
        ftri6.enbw,ftri7.enbw,ftri8.enbw,ftri9.enbw]),\
    np.array([ftri1.corrected_data(), ftri2.corrected_data(),\
        ftri3.corrected_data(),ftri4.corrected_data(),ftri5.corrected_data(),\
        ftri6.corrected_data(),ftri7.corrected_data(),ftri8.corrected_data(),\
        ftri9.corrected_data()]),\
    np.array([ftri1.corrected_del(),ftri2.corrected_del(),\
        ftri3.corrected_del(),ftri4.corrected_del(),ftri5.corrected_del(),\
        ftri6.corrected_del(),ftri7.corrected_del(),ftri8.corrected_del(),\
        ftri9.corrected_del()]), 'yes')
print('kb_enbw =', enbwm/(4*room_temp*10000), '+/-', denbwm/(4*room_temp*10000))

ndm,ndb,dndm,dndb, f11= linerrplt(11,\
    'Johnson Noise vs Effective Noise Bandwidth',\
    'Frequency [Hz]','$<V_j^2> [V^2]$', 'linear', 'linear',\
    np.array([tri1.resistance,tri2.resistance,tri3.resistance,\
        tri4.resistance]),\
    np.divide(np.subtract(np.array([ftri4_10.inferred,ftri4_100.inferred,\
        ftri4_1000.inferred,ftri4.inferred]), tri1.b) , ftri4.enbw),\
    np.divide(errpropaddsubtract(np.array([ftri4_10.error(),ftri4_100.error(),\
        ftri4_1000.error(),ftri4.error()]), tri1.db),ftri4.enbw), 'yes')


plt.close(f1)  # correction curve for noise vs r
plt.close(f2)  # linear scale noise vs r
plt.close(f3)  # Logarithmic scale noise vs r
plt.close(f4)  # correction curve 25 kHz band
plt.close(f5)  # correction curve 11 kHz band
plt.close(f6)  # correction curve 10 kHz band
plt.close(f7)  # noise vs high pass
plt.close(f8)  # noise vs low pass
plt.close(f9)  # noise vs f2-f1
plt.close(f10) # noise vs enbw
plt.close(f11) # noise density

plt.show()
