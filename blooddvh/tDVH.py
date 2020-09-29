import numpy as np
import pandas as pd
import time
#from operator import itemgetter
from functools import reduce
from matplotlib.cbook import flatten

"""
Time-dependent DVH class consisting of dT and DVH
"""
class tDVH:
    __slots__ = ["dvh", "seed", "start_time"]

    def __init__(self, seed=0):
        """ 
        Initialize members, dvh, seed, and start_time

        dvh[0] : time, e.g., elapsed time (array) from start
        dvh[1] : dvh function (list), if no dose for time, None is recommended instead of 0 due to performance issue
        
        For example,
        dvh = [ np.array([1,3,6,7,10]), [lambda v:3, lambda v:0, v2d, v2d_const, None]]
        """
        self.dvh  = [np.array([]),[]]
        self.start_time = 0.0

    def add(self, beam_on_time, dvh_function):
        """
        Fill dvh functions as a function of time

        Parameters
        beam_on_time : delivery time of this dvh time. Time is relative to beam start
        dvh_function : DVH function (lambda or intpl1d)
        """
        stop_time = 0.0
        if self.dvh[0].size != 0:
            stop_time = self.dvh[0][-1]
            
        self.dvh[0] = np.append(self.dvh[0], stop_time + beam_on_time)
        self.dvh[1].append(dvh_function)
    
    def add_csv(self, beam_on_time, dvh_file):
        """
        Parameters
        beam_on_time : delivery time of this dvh
        dvh_file     : a CSV file with DVH curve or DataFrame ?
        """
        
        pass