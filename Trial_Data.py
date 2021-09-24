import numpy as np
# import matplotlib.pyplot as plt
# import math
# from scipy.optimize import curve_fit
# from scipy import integrate

class Trial_Data:
    def __init__(self,data,resistance,gain):
        self.data = data
        self.resistance = resistance
        self.gain = gain
        self.correction_factor
        self.corrected_data = self.correcting_data(self.correction_factor)   

    def error(self):
        return (np.amax(self.data) - np.amin(self.data))/(2*math.sqrt(len(self.data)))
    
    def correcting_data(self,correction_factor):
        self.correcting_data = np.subtract(self.data,correction_factor)
    