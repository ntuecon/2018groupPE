"""
Created on Mon Apr 02 16:34:45 2018
"""
"""
@author: WeiJin,PoHan
"""

import numpy as np
from Consumer import Consumer
from Producer import Producer
from function import Loop
from function import Total

"""
Define the objective function and the constraints for the social planner
"""

class SP(object):
    def __init__(self,c,g,f,A,B,T,e1=False):
        self.c = c
        self.g = g
        self.f = f
        self.A = A
        self.B = B
        self.T = T
        self.e1 = e1

    """
    Define the objective function for the social planner: the social welfare function
    """
    def Welfare(self,output_list):
        """
        Call the utility function from Class:consumer
        """
        C = Consumer(self.c,self.g,self.f,self.A,self.B,self.T)
        utility_list = C.Utility(output_list)
        """
        Obtain parameters of the social welfare function
        """
        overall_weight = 1 / float(100)
        utility_weights = Loop(self.c)
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
    def Constraints(self,output_list):
        P = Producer(self.c,self.g,self.f,self.e1)
        T = Total(self.c,self.g,self.f)
        if self.e1 == True:
            Cons = ({'type': 'eq','fun' : lambda x:(T.total_consumption(x)-P.Production(x))},
            {'type': 'eq','fun' : lambda x:(T.total_factor_dd(x)-T.total_factor_ss(x))},
            {'type': 'ineq','fun': lambda x:x})
            return Cons
        else:
            Cons = ({'type': 'eq','fun' : lambda x:(T.total_consumption(x)-P.Production(x))},
            {'type': 'eq','fun' : lambda x:(T.total_factor_dd(x)-T.total_factor_ss(x))},
            {'type': 'ineq','fun': lambda x:x})
            return Cons