"""
Created on Mon Apr 02 16:34:45 2018
@author: WeiJin,PoHan
"""

# Import tools
import numpy as np
# Import modules
from Consumer import Consumer
from Producer import Producer
from function import Loop
from function import Total


# Define a class SP to simulate a social planner who determines the welfare function and constraints of the economy
class SP(object):
    def __init__(self,c,g,f,A,B,T,e1):
        # c: Number of consumers in the economy
        # g: Number of goods produced in the economy
        # f: Number of factors used in the production
        # A, B, T: Parameters alpha, beta, theta from the consumer's utility function
        # e1: The degree of aggregate production externality
        self.c = c
        self.g = g
        self.f = f
        self.e1 = 0.1
        
        self.A = A
        self.B = B
        self.T = T

    # Define the welfare function to be optimized
    def Welfare(self,output_list):
        # Initiate an instance of Consumer
        C = Consumer(self.c,self.g,self.f,self.A,self.B,self.T)
        # Generate the utility list of the consumer instance
        utility_list = C.Utility(output_list)
        
        '''
        An utilitarian welfare function
        '''
        welfare = -1 * np.sum(utility_list)
        return welfare
    
    # Define the contraints that enter the optimization function
    def Constraints(self,output_list):
        # Generate an instance of Producer
        P = Producer(self.c,self.g,self.f,self.e1)
        # Generate an instance of Total
        T = Total(self.c,self.g,self.f)
        # Construct the constraints function
        # First constraint: Total Production = Total Consumption
        # Second constraint: Total factor supplied = Total factor demanded
        # Third constraint: All result values are non-negative
        Cons = ({'type': 'ineq','fun': lambda x:x - 0.0000001},
        {'type': 'eq','fun' : lambda x:(T.total_consumption(x)-P.Production(x))},
        {'type': 'eq','fun' : lambda x:(T.total_factor_dd(x)-T.total_factor_ss(x))},
        )
        return Cons
    def Constraints_Ind(self,output_list):
        # Generate an instance of Producer
        P = Producer(self.c,self.g,self.f,self.e1)
        # Generate an instance of Total
        T = Total(self.c,self.g,self.f)
        # Construct the constraints function
        # First constraint: Total Production = Total Consumption
        # Second constraint: Total factor supplied = Total factor demanded
        # Third constraint: All result values are non-negative
        Cons = ({'type': 'ineq','fun': lambda x:x - 0.0000001},
        {'type': 'eq','fun' : lambda x:(T.total_consumption(x)-P.Production_Ind(x))},
        {'type': 'eq','fun' : lambda x:(T.total_factor_dd(x)-T.total_factor_ss(x))},
        )
        return Cons
        