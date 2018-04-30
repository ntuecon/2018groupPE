"""
Created on Mon Apr 02 16:34:45 2018
"""
"""
@author: WeiJin,PoHan
"""

"""
Set up the basic environment for the economy
"""

import numpy as np
import random
import scipy
from Consumer import Consumer
from Producer import Producer
from fucntion import Loop
from function import Nested_Loop 
from fucntion import Loop_Slice 
from function import total_consumption
from function import total_factor_ss
from function import total_factor_dd
from Government import SP


class Economy(object):
    """
    'c'=number of consumers in the economy
    'g'=number of goods produced in the economy
    'f'=number of factors used in the production
    """
    def __init__(self,c,g,f):
        self.c = c
        self.g = g
        slef.f = f
    """
    Calculate the equilibria base on the consumers' preferences and technology
    """
    def Equilibrium(self):
        """
        Construct the initial value of optimization
        """
        output_list_length = self.c * (self.g + self.f) + self.g * self.f
        output_list = []
        i = 0
        for i in range(output_list_length):
        output_list.append(random.random())
        """
        Solve the optimization problem
        """
        G = SP(self.c,self.g,self.f)
        res = minimize(G.Welfare,output_list,method = 'SLSQP',constraints = G.Consraints())
        print res
        
