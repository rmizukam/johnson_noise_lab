import numpy as np
# import matplotlib.pyplot as plt
import math
# from scipy.optimize import curve_fit
# from scipy import integrate

class Frequency_Trial_Data:
    def __init__(self,data,resistance,gain,frequncies):
        self.data = data
        self.resistance = resistance
        self.gain = gain
        self.highpass = frequncies[0]
        self.lowpass = frequncies[1]
        self.enbw = frequncies[2]
        # self.correction_factor
        # self.corrected_data = self.correcting_data(self.correction_factor)   

    def error(self):
        return (np.amax(self.data) - np.amin(self.data))/(2*math.sqrt(len(self.data)))

    def inferred(self):
        return self.data *10 /(600**2)/(self.gain**2)

    def mean(self):
        return np.mean(self.data)
    