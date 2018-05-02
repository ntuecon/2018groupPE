"""
Created on Mon Apr 02 16:34:45 2018
"""
"""
@author: WeiJin,PoHan
"""

import numpy as np
import random
from Consumer import Consumer
from Producer import Producer
from function import Loop
from function import total_consumption
from function import total_factor_ss
from function import total_factor_dd


"""
Define the objective function and the constraints for the social planner
"""

class SP(object):
    def __init__(self,c,g,f):
        self.c = c
        self.g = g
        self.f = f
    """
    Define the objective function for the social planner: the social welfare function
    """
    def Welfare(self,output_list):
        """
        Call the utility function from Class:consumer
        """
        C = Consumer(self.c,self.g,self.f)
        utility_list = Consumer.Utility(output_list)
        """
        Obtain parameters of the social welfare function
        """
        overall_weight = 1 / (random.random())
        utility_weights = Loop(self.c,2)
        """
        Calculate the social welfare
        """
        utility_list_square = utility_list ** 2
        welfare = (np.sum(np.power(utility_list_square , utility_weights))) ** overall_weight
        neg_welfare = welfare * -1
        return neg_welfare
    """
    Define the constraints for the maximization problem
    """
    def Constraints(self):
        P = Producer(self.c,self.g,self.f)
        F = np.array([])
        i = 0
        while i < self.f * self.g:
            if i % self.f == 1:
                F = np.append(F,f_list[i - 1])
            i += 1
        Cons = ({'type': 'eq','fun' : lambda x:(total_consumption(x)-P.Production(x))},
        {'type': 'eq','fun' : lambda x:(total_factor_dd(x)-total_factor_ss(x))},
        {'type': 'eq','fun' : lambda x:F[x]},
        {'type': 'ineq','fun': lambda x:x})
        return Cons