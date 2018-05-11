"""
Created on Mon Apr 02 16:34:45 2018
"""
"""
@author: WeiJin,PoHan
"""

"""
Set up the basic environment for the economy
"""

import random
import numpy as np
from scipy.optimize import minimize
from Government import SP
from Consumer import Consumer
from Producer import Producer
from function import Loop
from function import Total



class Economy(object):
    """
    'c'=number of consumers in the economy
    'g'=number of goods produced in the economy
    'f'=number of factors used in the production
    'e1'=a good that uses a factor that creates a type of negative externality
    """
    def __init__(self,c,g,f,e1=False):
        self.c = c
        self.g = g
        self.f = f
        self.e1 = e1
    """
    Calculate the equilibrium based on the consumers' preferences and technology
    """
    def Equilibrium(self):
        """
        Construct the initial value of optimization
        """
        output_list_length = self.c * (self.g + self.f) + self.g * self.f
        output_list = []
        for i in range(output_list_length):
            output_list.append(random.randint(1,10))

        """
        Solve the optimization problem
        """
        G = SP(self.c,self.g,self.f)
        res = minimize(G.Welfare,output_list,method = 'SLSQP',constraints = G.Constraints())
        print res

"""Test case"""
E1 = Economy(2,2,2)
print E1.Equilibrium()