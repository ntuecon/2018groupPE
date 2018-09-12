"""
Created on Mon Apr 02 16:34:45 2018
@author: WeiJin,PoHan
"""

# Import tools
import random
from scipy.optimize import minimize
# Import modules
from Government import SP
from function import Loop
from function import Nested_Loop_C


# Create a class called Economy to observe the interaction between consumers, producers and government
class Economy(object):
    def __init__(self,c,g,f,e1=False):
        # c: Number of consumers in the economy
        # g: Number of goods produced in the economy
        # f: Number of factors used in the production
        # e1: A good that uses a factor that creates a type of negative externality
        self.c = c
        self.g = g
        self.f = f
        self.e1 = e1
        # Generate parameters alpha, beta, theta for consumers' utility functions
        self.A = Nested_Loop_C(self.c,self.g)
        self.B = Loop(self.c)
        self.T = Loop(self.f)
    
    # Calculate the equilibrium based on the consumers' preferences and technology
    def Equilibrium(self):
        # Obtain the output list with the correct list length
        # Format of output list: [C1G1 C1G2 C2G1 C2G2 C1F1 C1F2 C2F1 C2F2 P1F1 P1F2 P2F1 P2F2]
        output_list_length = self.c * (self.g + self.f) + self.g * self.f
        output_list = []
        # Generate initial output list values for the optimization
        for i in range(output_list_length):
            output_list.append(1)
            
        # Solve the optimization problem
        # G: An instance of the social planner, who determines the welfare function and constraints
        G = SP(self.c,self.g,self.f,self.A,self.B,self.T,self.e1)
        # res: Results of optimization problem
        res = minimize(G.Welfare,output_list,method = 'SLSQP',constraints = G.Constraints(output_list))
        return res


# TEST CASE
# E1: An instance of Economy
E1 = Economy(3,3,3,e1=True)
# Obtain equilibrium results
E = E1.Equilibrium()
print E