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
from scipy.optimize import minimize
from Government import SP
from function import Loop
from function import Nested_Loop_C



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
        self.A = Nested_Loop_C(self.c,self.g)
        self.B = Loop(self.c)
        self.T = Loop(self.f)
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
            output_list.append(random.randint(0,20))

        """
        Solve the optimization problem
        """
        G = SP(self.c,self.g,self.f,self.A,self.B,self.T,self.e1)
        res = minimize(G.Welfare,output_list,method = 'SLSQP',constraints = G.Constraints(output_list))
        print res

"""Test case"""
E1 = Economy(2,2,2,e1=True)
print E1.Equilibrium()