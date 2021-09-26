# main
import numpy as np
from numpy.core.numeric import correlate
from Trial_Data import Trial_Data
from Frequency_Trial_Data import Frequency_Trial_Data
from Plotting_Fitting_Macros import linerrplt

# Data for Noise vs Resistance
tri1 = Trial_Data(np.array([0.979, 0.980, 0.978, 0.977, 0.977]),1,2000) # raw_data, resistance, gain
tri2 = Trial_Data(np.array([0.981, 0.980, 0.982, 0.980, 0.981]),10,2000)
tri3 = Trial_Data(np.array([1.003, 1.004, 1.005, 1.003, 1.004]),100,2000)
tri4 = Trial_Data(np.array([0.702, 0.702, 0.703, 0.701, 0.702]),100,1500)
tri5 = Trial_Data(np.array([0.924, 0.923, 0.923, 0.925, 0.926]),10000,1000)
tri6 = Trial_Data(np.array([0.874, 0.873, 0.872, 0.872, 0.871]),100000,400)
tri7 = Trial_Data(np.array([0.949, 0.952, 0.948, 0.949, 0.950]),1000000,300)

# Data for Noise vs Frequency
ftri1 = Frequency_Trial_Data(np.array([0.926, 0.926,0.925, 0.924, 0.925]),10000,1000, np.array([100, 100000, 110961])) # raw_data, resistance, gain, high pass, low pass, ENBW
ftri2 = Frequency_Trial_Data(np.array([0.923, 0.924, 0.926, 0.924, 0.925]),10000,1000,np.array([300, 100000, 110739]))
ftri3 = Frequency_Trial_Data(np.array([0.920, 0.918, 0.918, 0.919, 0.917]),10000,1000,np.array([1000, 100000, 109961]))
ftri4 = Frequency_Trial_Data(np.array([0.660, 0.658, 0.659, 0.661, 0.662]),10000,1500,np.array([1000, 33000, 35543]))
ftri5 = Frequency_Trial_Data(np.array([0.679, 0.676, 0.675, 0.676, 0.674]),10000,1500,np.array([100, 33000, 36543]))

# Data Used to correct the Frequency Trials
ftri1_1 = Trial_Data(np.array([0.712, 0.712, 0.713, 0.711, 0.713]),1,3000)
ftri1_10 = Trial_Data(np.array([0.713, 0.714, 0.713, 0.712, 0.713]),10,3000)
ftri1_100 = Trial_Data(np.array([0.728, 0.729, 0.732, 0.731, 0.730]),100,3000)
ftri6_1 = Trial_Data(np.array([0.861, 0.851, 0.861, 0.863, 0.856]),1,6000)
ftri6_10 = Trial_Data(np.array([0.864, 0.857, 0.856, 0.857, 0.858]),10,6000)
ftri6_100 = Trial_Data(np.array([0.881, 0.877, 0.8800, 0.884, 0.888]),100,6000)
ftri9_1 = Trial_Data(np.array([0.795, 0.798, 0.798, 0.800, 0.795]),1,10000)
ftri9_10 = Trial_Data(np.array([0.809, 0.802, 0.806, 0.803, 0.804]),10,10000)
ftri9_100 = Trial_Data(np.array([0.811, 0.827, 0.811, 0.825, 0.814]),100,10000)


m1, b1, dm1, db1 = linerrplt(1,'Correction Curve $\Delta$ f = 11kHz', 'Resistance $\Omega$', '$<V_J^2 + V_N^2>$', 'linear', 'linear',\
    np.array([1,10,100]), np.array([tri1.inferred(), tri2.inferred(), tri3.inferred()]), np.array([tri1.error(), tri2.error(), tri3.error()]), 'c', 'orange')
