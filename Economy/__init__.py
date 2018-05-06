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
from Government import SP


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
        i = 0
        for i in range(output_list_length):
            output_list.append(random.randint(1,10))
        return output_list
        """
        Solve the optimization problem
        """
        G = SP(self.c,self.g,self.f)
        res = scipy.minimize(G.Welfare,output_list,method = 'SLSQP',constraints = G.Constraints())
        print res

"""Test case"""
E1 = Economy(3,3,3,e1=True)
print E1.Equilibrium()