"""
Created on Mon Apr 02 16:34:45 2018
"""
"""
@author: WeiJin,PoHan
"""

import numpy as np
import random
import scipy
import Loop from function
import Nested_Loop from function
import Loop_Slice from fucntion

"""
Define the preferences of consumers
"""

class consumer(object):
    """
    'c'=number of consumers
    'g'=number of goods
    'f'=number of factors
    """
    def __init__(slef,c,g,f):
        self.c = c
        self.g = g
        self.f = f
    def Utility(self,output_list):
        """
        Getting ready for calculating utility
        """
        
        """
        Define variables that will be useful in interation of list
        """
        consumption_length = self.c * self.g
        factor_ss_length = self.c * self.f
        consumer_length = consumption_length +  factor_ss_length
        c_list = np.array(output_list[0:consumption_length])
        f_list = np.array(output_list[consumption_length:consumption_length + factor_ss_length])
        """
        Generate parameters for the utility function
        """
        y = random.randint(1,5)
        s = round(random.random(),2)
        A = Nested_Loop(self.c,self.g,2)
        B = Loop(self.c,2)
        T = Loop(self.f,2)
        """
        
        """
        Calculate the utility that comes from consuming goods
        """
        weighted_utility_subc = np.multiply((c_list ** y) , A)
        utility_subc = np.array([])
        for i in range(len(weighted_utility_subc)):
            if (i == 0) or (i % total_goods == 0 and i < total_goods * total_consumers):
                utility_subc = np.append(utility_subc,(np.sum(weighted_utility_subc[i:i + total_goods])) ** ((1 - s) / y))
        
        """
        Caluculate the utility that comes from supplying factors
        """
        tweighted_utility_subf = np.array([])
        i = 0
        while i < total_consumers:
            j = 0
            while j < total_factors:
                tweighted_utility_subf = np.append(tweighted_utility_subf,((f_list[(i * total_factors) + j] ** (1 + T[j])) / (1 + T[j])))
                j += 1
            i += 1
        
        weighted_utility_subf = np.array([])
        for i in range(len(tweighted_utility_subf)):
            if i == 0:
                weighted_utility_subf = np.append(weighted_utility_subf,((tweighted_utility_subf[i:i + total_factors]) * B[i]))
            if i % total_factors == 0 and i < total_consumers * total_factors:
                weighted_utility_subf = np.append(weighted_utility_subf,(tweighted_utility_subf[i:i + total_factors]) * B[i / total_factors])
        
        utility_subf = np.array([])
        for i in range(len(weighted_utility_subf)):
            if (i== 0) or (i % total_factors == 0 and i < total_consumers * total_factors):
                utility_subf = np.append(utility_subf,(np.sum(weighted_utility_subf[i:i + total_factors])))
                
        """
        Calculate the total utility for each consumer in the economy
        """
        utility_list = np.array([])
        utility_list = np.round((utility_subc - utility_subf) , 2)
        return utility_list
