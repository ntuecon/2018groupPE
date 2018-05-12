"""
Created on Mon Apr 02 16:34:45 2018
"""
"""
@author: WeiJin,PoHan
"""

import numpy as np

"""
Define the preferences of consumers
"""

class Consumer(object):
    """
    'c'=number of consumers
    'g'=number of goods
    'f'=number of factors
    """
    def __init__(self,c,g,f,A,B,T):
        self.c = c
        self.g = g
        self.f = f
        self.A = A
        self.B = B
        self.T = T
    def Utility(self,output_list):
        """
        Setting up the utility calculation
        """
        
        """
        Define variables that will be useful for list iterations
        """
        consumption_length = self.c * self.g
        factor_ss_length = self.c * self.f
        c_list = np.array(output_list[0:consumption_length])
        f_list = np.array(output_list[consumption_length:consumption_length + factor_ss_length])
        """
        Generate parameters for the utility function
        """
        y = float(10)
        s = float(0.5)
        
        """
        Calculate the utility that comes from consuming goods
        """
        weighted_utility_subc = np.multiply((c_list ** y) , self.A)
        utility_subc = np.array([])
        for i in range(len(weighted_utility_subc)):
            if (i == 0) or (i % self.g == 0 and i < self.g * self.c):
                utility_subc = np.append(utility_subc,(np.sum(weighted_utility_subc[i:i + self.g])) ** ((1 - s) / y))
        
        """
        Caluculate the utility that comes from supplying factors
        """
        tweighted_utility_subf = np.array([])
        i = 0
        while i < self.c:
            j = 0
            while j < self.f:
                tweighted_utility_subf = np.append(tweighted_utility_subf,((f_list[(i * self.f) + j] ** (1 + self.T[j])) / (1 + self.T[j])))
                j += 1
            i += 1
        
        weighted_utility_subf = np.array([])
        for i in range(len(tweighted_utility_subf)):
            if i == 0:
                weighted_utility_subf = np.append(weighted_utility_subf,((tweighted_utility_subf[i:i + self.f]) * self.B[i]))
            if i % self.f == 0 and i < self.c * self.f:
                weighted_utility_subf = np.append(weighted_utility_subf,(tweighted_utility_subf[i:i + self.f]) * self.B[i / self.f])
        
        utility_subf = np.array([])
        for i in range(len(weighted_utility_subf)):
            if (i== 0) or (i % self.f == 0 and i < self.c * self.f):
                utility_subf = np.append(utility_subf,(np.sum(weighted_utility_subf[i:i + self.f])))
                
        """
        Calculate the total utility for each consumer in the economy
        """
        utility_list = np.array([])
        utility_list = np.round((utility_subc - utility_subf) , 2)
        return utility_list