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
    def __init__(self,c,g,f,A,B,T,e1=False,t=0):
        # c: Number of consumers in the economy
        # g: Number of goods produced in the economy
        # f: Number of factors used in the production
        # A, B, T: Parameters alpha, beta, theta from the consumer's utility function
        # e1: A good that uses a factor that creates a type of negative externality
        self.c = c
        self.g = g
        self.f = f
        self.A = A
        self.B = B
        self.T = T
        self.e1 = e1
        self.t = t
    # Define the welfare function to be optimized
    def Welfare(self,output_list):
        # Initiate an instance of Consumer
        C = Consumer(self.c,self.g,self.f,self.A,self.B,self.T)
        # Generate the utility list of the consumer instance
        utility_list = C.Utility(output_list)
        
        # Generate the parameters for the welfare function
        # Obtain overall weight for the welfare function
        overall_weight = 1 / float(2)
        # Obtain individual utility weights for each consumer for the welfare function
        utility_weights = Loop(self.c)
        
        # Calculate the welfare
        # The welfare function is defined as the (sum of U^(2x)) ^ y, where x are individual weights and y is the overall weight
        utility_list_square = utility_list ** 2
        welfare = (np.sum(np.power(utility_list_square , utility_weights))) ** overall_weight
        # Obtain the negative of the welfare for minimization
        neg_welfare = welfare * -1
        return neg_welfare
    
    # Define the contraints that enter the optimization function
    def Constraints(self,output_list):
        # Generate an instance of Producer
        P = Producer(self.c,self.g,self.f,self.e1,self.t)
        # Generate an instance of Total
        T = Total(self.c,self.g,self.f)
        # Construct the constraints function
        # First constraint: Total Production = Total Consumption
        # Second constraint: Total factor supplied = Total factor demanded
        # Third constraint: All result values are non-negative
        Cons = ({'type': 'eq','fun' : lambda x:(T.total_consumption(x)-P.Production(x))},
        {'type': 'eq','fun' : lambda x:(T.total_factor_dd(x)-T.total_factor_ss(x))},
        {'type': 'ineq','fun': lambda x:x})
        return Cons