# main
import numpy as np
from Trial_Data import Trial_Data
from scipy.optimize import curve_fit
import math
import matplotlib.pyplot as plt
from Plotting_Fitting_Macros import linerrplt,errpropaddsubtract

room_temp = 293 #Kelvin
kb_true = 1.38064852E-23 # m^2 * kg * s^-2 * K^-1
# figures = []

# Data for Noise vs Resistance
tri1 = Trial_Data(np.array([0.979, 0.980, 0.978, 0.977, 0.977]),1,2000,np.array([100,100000,110961])) # raw_data, resistance, gain
tri2 = Trial_Data(np.array([0.981, 0.980, 0.982, 0.980, 0.981]),10,2000,np.array([100,100000,110961]))
tri3 = Trial_Data(np.array([1.003, 1.004, 1.005, 1.003, 1.004]),100,2000,np.array([100,100000,110961]))
tri4 = Trial_Data(np.array([0.702, 0.702, 0.703, 0.701, 0.702]),1000,1500,np.array([100,100000,110961]))
tri5 = Trial_Data(np.array([0.924, 0.923, 0.923, 0.925, 0.926]),10000,1000,np.array([100,100000,110961]))
tri6 = Trial_Data(np.array([0.874, 0.873, 0.872, 0.872, 0.871]),100000,400,np.array([100,100000,110961]))
tri7 = Trial_Data(np.array([0.949, 0.952, 0.948, 0.949, 0.950]),1000000,300,np.array([100,100000,110961]))

# Data for Noise vs Frequency
ftri1 = Trial_Data(np.array([0.926, 0.926,0.925, 0.924, 0.925]),10000,1000, np.array([100, 100000, 110961])) # raw_data, resistance, gain, high pass, low pass, ENBW
ftri2 = Trial_Data(np.array([0.923, 0.924, 0.926, 0.924, 0.925]),10000,1000,np.array([300, 100000, 110739]))
ftri3 = Trial_Data(np.array([0.920, 0.918, 0.918, 0.919, 0.917]),10000,1000,np.array([1000, 100000, 109961]))
ftri4 = Trial_Data(np.array([0.660, 0.658, 0.659, 0.661, 0.662]),10000,1500,np.array([1000, 33000, 35543]))
ftri5 = Trial_Data(np.array([0.679, 0.676, 0.675, 0.676, 0.674]),10000,1500,np.array([100, 33000, 36543]))
ftri6 = Trial_Data(np.array([0.804, 0.807, 0.801, 0.803, 0.805]),10000,3000,np.array([100, 10000, 10996]))
ftri7 = Trial_Data(np.array([0.729, 0.727, 0.730, 0.731, 0.729]),10000,3000,np.array([1000, 10000, 9997]))
ftri8 = Trial_Data(np.array([0.729, 0.727, 0.730, 0.731, 0.729]),10000,6000,np.array([1000, 3300, 2576]))
ftri9 = Trial_Data(np.array([1.06, 1.07, 1.06, 1.05, 1.05]),10000,6000,np.array([100, 3300, 3554]))

# Data Used to correct the Frequency Trials
ftri4_1 = Trial_Data(np.array([0.712, 0.712, 0.713, 0.711, 0.713]),1,3000,np.array([100, 100000, 110961]))
ftri4_10 = Trial_Data(np.array([0.713, 0.714, 0.713, 0.712, 0.713]),10,3000,np.array([100, 100000, 110961]))
ftri4_100 = Trial_Data(np.array([0.728, 0.729, 0.732, 0.731, 0.730]),100,3000,np.array([100, 100000, 110961]))
ftri6_1 = Trial_Data(np.array([0.861, 0.851, 0.861, 0.863, 0.856]),1,6000,np.array([100, 10000, 10996]))
ftri6_10 = Trial_Data(np.array([0.864, 0.857, 0.856, 0.857, 0.858]),10,6000,np.array([100, 10000, 10996]))
ftri6_100 = Trial_Data(np.array([0.881, 0.877, 0.8800, 0.884, 0.888]),100,6000,np.array([100, 10000, 10996]))
ftri9_1 = Trial_Data(np.array([0.795, 0.798, 0.798, 0.800, 0.795]),1,10000,np.array([100, 3300, 3554]))
ftri9_10 = Trial_Data(np.array([0.809, 0.802, 0.806, 0.803, 0.804]),10,10000,np.array([100, 3300, 3554]))
ftri9_100 = Trial_Data(np.array([0.811, 0.827, 0.811, 0.825, 0.814]),100,10000,np.array([100, 3300, 3554]))

# x = np.array([1,10,100])
# y = np.array([tri1.inferred(), tri2.inferred(), tri3.inferred()])
# dy = np.array([tri1.error(), tri2.error(), tri3.error()])
tri1.m, tri1.b, tri1.dm, tri1.db, f1 = linerrplt(1,'Correction Curve $\Delta$ f = 11kHz', 'Resistance $\Omega$', '$<V_J^2 + V_N^2>$','linear','linear',\
    np.array([1,10,100]), np.array([tri1.inferred, tri2.inferred, tri3.inferred]), np.array([tri1.error(), tri2.error(), tri3.error()]),'yes')
# figures.append(f1)
tri2.m, tri2.b, tri2.dm, tri2.db = tri1.m, tri1.b, tri1.dm, tri1.db
tri3.m, tri3.b, tri3.dm, tri3.db = tri1.m, tri1.b, tri1.dm, tri1.db

m1, d1, dm1, db1, f2 = linerrplt(2, 'Johnson Noise vs Resistance: Linear Scale', 'Resistance [$\Omega$]', '<$V_j^2$> [$v^2$]', 'linear', 'linear', \
    np.array([tri1.resistance, tri2.resistance, tri3.resistance]), np.array([tri1.corrected_data(),tri2.corrected_data(), tri3.corrected_data()]),\
    np.array([tri1.corrected_del(),tri2.corrected_del(), tri3.corrected_del()]), 'yes')
# figures.append(f2)
print('kb_noise_vs_r',(m1 / 4/room_temp/tri1.enbw))

ml1, bl1, dml1, dbl1, f3 = linerrplt(3, 'Johnson Noise vs Resistance: Logarithmic Scale', 'Resistance [$\Omega$]', '<$V_j^2$> [$v^2$]', 'log', 'log', \
    np.array([tri1.resistance, tri2.resistance, tri3.resistance]), np.array([tri1.corrected_data(),tri2.corrected_data(), tri3.corrected_data()]),\
    np.array([tri1.corrected_del(),tri2.corrected_del(), tri3.corrected_del()]), 'yes')
# figures.append(f3)
print('kb_noise_vs_r_log', (ml1/4/room_temp/tri1.enbw))

ftri4.m, ftri4.b, ftri4.dm, ftri4.db, f4 = linerrplt(4, 'Correction for frequency band = 25kHz', 'Resistance [$\Omega$]', '$<V_j^2$ + $V_N^2> [V^2]$', 'linear', 'linear', \
    np.array([ftri4_1.resistance, ftri4_10.resistance, ftri4_100.resistance]), np.array([ftri4_1.inferred,ftri4_10.inferred, ftri4_10.inferred]),\
    np.array([ftri4_1.error(),ftri4_10.error(), ftri4_100.error()]), 'yes')
ftri5.m, ftri5.b, ftri5.dm, ftri5.db = ftri4.m, ftri4.b, ftri4.dm, ftri4.db

ftri6.m, ftri6.b, ftri6.dm, ftri6.db, f5 = linerrplt(5, 'Correction for frequency band = 11kHz', 'Resistance [$\Omega$]', '$<V_j^2$ + $V_N^2> [V^2]$', 'linear', 'linear', \
    np.array([ftri6_1.resistance, ftri6_10.resistance, ftri6_100.resistance]), np.array([ftri6_1.inferred,ftri6_10.inferred, ftri6_10.inferred]),\
    np.array([ftri6_1.error(),ftri6_10.error(), ftri6_10.error()]), 'yes')
ftri7.m, ftri7.b, ftri7.dm, ftri7.db = ftri6.m, ftri6.b, ftri6.dm, ftri6.db

ftri9.m, ftri9.b, ftri9.dm, ftri9.db, f6 = linerrplt(6, 'Correction for frequency band = 10kHz', 'Resistance [$\Omega$]', '$<V_j^2$ + $V_N^2> [V^2]$', 'linear', 'linear', \
    np.array([ftri9_1.resistance, ftri9_10.resistance, ftri9_100.resistance]), np.array([ftri9_1.inferred,ftri9_10.inferred, ftri9_10.inferred]),\
    np.array([ftri9_1.error(),ftri9_10.error(), ftri9_10.error()]), 'yes')
ftri8.m, ftri8.b, ftri8.dm, ftri8.db = ftri9.m, ftri9.b, ftri9.dm, ftri9.db

correct_freq_data = np.array([ftri1.corrected_data(), ftri2.corrected_data(),ftri3.corrected_data(),ftri4.corrected_data(),ftri5.corrected_data(),ftri6.corrected_data(),\
    ftri7.corrected_data(),ftri8.corrected_data(),ftri9.corrected_data()])

correct_freq_del = np.array([ftri1.corrected_del(),ftri2.corrected_del(),ftri3.corrected_del(),ftri4.corrected_del(),ftri5.corrected_del(),ftri6.corrected_del(),\
    ftri7.corrected_del(),ftri8.corrected_del(),ftri9.corrected_del()])

lpm, lpb, dlpm, dlpb, f7 = linerrplt(7, 'Correction for frequency band = 10kHz', 'Resistance [$\Omega$]', '$<V_j^2$ + $V_N^2> [V^2]$', 'linear', 'linear', \
    np.array([ftri9_1.resistance, ftri9_10.resistance, ftri9_100.resistance]), np.array([ftri9_1.inferred,ftri9_10.inferred, ftri9_10.inferred]),\
    np.array([ftri9_1.error(),ftri9_10.error(), ftri9_10.error()]), 'no')

# plt.show()
