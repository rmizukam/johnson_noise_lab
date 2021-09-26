# main
import numpy as np
from Trial_Data import Trial_Data
from Frequency_Trial_Data import Frequency_Trial_Data

# Data for Noise vs Resistance
tri1 = Trial_Data(np.array([0.979, 0.980, 0.978, 0.977, 0.977]),1,2000) # raw_data, resistance, gain
tri2 = Trial_Data(np.array([0.981, 0.980, 0.982, 0.980, 0.981]),10,2000)
tri3 = Trial_Data(np.array([1.003, 1.004, 1.005, 1.003, 1.004]),100,2000)
tri4 = Trial_Data(np.array([0.702, 0.702, 0.703, 0.701, 0.702]),100,1500)
tri5 = Trial_Data(np.array([0.924, 0.923, 0.923, 0.925, 0.926]),10000,1000)
tri6 = Trial_Data(np.array([0.874, 0.873, 0.872, 0.872, 0.871]),100000,400)
tri7 = Trial_Data(np.array([0.949, 0.952, 0.948, 0.949, 0.950]),1000000,300)

# Data for Noise vs Frequency
freqtri1 = Frequency_Trial_Data(np.array([0.926, 0.926,0.925, 0.924, 0.925]),10000,1000, np.array([100, 100000, 110961])) # raw_data, resistance, gain, high pass, low pass, ENBW
freqtri2 = Frequency_Trial_Data(np.array([0.923, 0.924, 0.926, 0.924, 0.925]),10000,1000,np.array([300, 100000, 110739]))
freqtri3 = Frequency_Trial_Data(np.array([0.920, 0.918, 0.918, 0.919, 0.917]),10000,1000,np.array([1000, 100000, 109961]))
freqtri4 = Frequency_Trial_Data(np.array([0.660, 0.658, 0.659, 0.661, 0.662]),10000,1500,np.array([1000, 33000, 35543]))
freqtri5 = Frequency_Trial_Data(np.array([0.679, 0.676, 0.675, 0.676, 0.674]),10000,1500,np.array([100, 33000, 36543]))

# Data Used to correct the Frequency Trials
