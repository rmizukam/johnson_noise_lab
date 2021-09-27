import numpy as np
import math
# from scipy.optimize import curve_fit
# from scipy import integrate
# import matplotlib.pyplot as plt

class Trial_Data:
    def __init__(self,data,resistance,gain,frequncies):
        self.mean = np.mean(data)
        self.data = data
        self.resistance = resistance
        self.gain = gain
        self.b = 0
        self.db = 0
        self.m = 0
        self.dm = 0
        self.inferred = self.mean *10 / 600**2 / self.gain**2
        self.highpass = frequncies[0]
        self.lowpass = frequncies[1]
        self.enbw = frequncies[2]

    def error(self):
        return (np.amax(self.data - np.amin(self.data)) / 2*math.sqrt(len(self.data)))*10 / 600**2 / self.gain**2

    def corrected_data(self):
        return np.subtract(self.inferred, self.b)

    def corrected_del(self):
        return math.sqrt(self.db**2 + self.error()**2)
