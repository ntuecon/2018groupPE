"""
Created on Mon Apr 02 16:34:45 2018
"""
"""
@author: WeiJin,PoHan
"""

import numpy as np
import random
from function import Loop
from function import Nested_Loop

"""
Define the preferences of consumers
"""

class Consumer(object):
    """
    'c'=number of consumers
    'g'=number of goods
    'f'=number of factors
    """
    def __init__(self,c,g,f):
        self.c = c
        self.g = g
        self.f = f
    def Utility(self,output_list):
        """
        Setting up the utility calculation
        """
        
        """
        Define variables that will be useful for list iterations
        """
        consumption_length = c * g
        factor_ss_length = c * f
        consumer_length = consumption_length +  factor_ss_length
        c_list = np.array(output_list[0:consumption_length])
        f_list = np.array(output_list[consumption_length:consumption_length + factor_ss_length])
        """
        Generate parameters for the utility function
        """
        y = random.randint(1,5)
        s = round(random.random(),2)
        A = Nested_Loop(c,g,2)
        B = Loop(c,2)
        T = Loop(f,2)
        
        
        """
        Calculate the utility that comes from consuming goods
        """
        weighted_utility_subc = np.multiply((c_list ** y) , A)
        utility_subc = np.array([])
        for i in range(len(weighted_utility_subc)):
            if (i == 0) or (i % g == 0 and i < g * c):
                utility_subc = np.append(utility_subc,(np.sum(weighted_utility_subc[i:i + g])) ** ((1 - s) / y))
        
        """
        Caluculate the utility that comes from supplying factors
        """
        tweighted_utility_subf = np.array([])
        i = 0
        while i < c:
            j = 0
            while j < f:
                tweighted_utility_subf = np.append(tweighted_utility_subf,((f_list[(i * f) + j] ** (1 + T[j])) / (1 + T[j])))
                j += 1
            i += 1
        
        weighted_utility_subf = np.array([])
        for i in range(len(tweighted_utility_subf)):
            if i == 0:
                weighted_utility_subf = np.append(weighted_utility_subf,((tweighted_utility_subf[i:i + f]) * B[i]))
            if i % total_factors == 0 and i < total_consumers * total_factors:
                weighted_utility_subf = np.append(weighted_utility_subf,(tweighted_utility_subf[i:i + f]) * B[i / f])
        
        utility_subf = np.array([])
        for i in range(len(weighted_utility_subf)):
            if (i== 0) or (i % f == 0 and i < c * f):
                utility_subf = np.append(utility_subf,(np.sum(weighted_utility_subf[i:i + f])))
                
        """
        Calculate the total utility for each consumer in the economy
        """
        utility_list = np.array([])
        utility_list = np.round((utility_subc - utility_subf) , 2)
        return utility_list