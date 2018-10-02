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
from function import Nested_Loop_B
from Producer import Producer

# Create a class called Economy to observe the interaction between consumers, producers and government
class Economy(object):
    def __init__(self,c,g,f,e1):
        # c: Number of consumers in the economy
        # g: Number of goods produced in the economy
        # f: Number of factors used in the production
        # e1: The degree of aggregate production externality
        self.c = c
        self.g = g
        self.f = f
        self.e1 = 0.1
        
        # Generate parameters alpha, beta, theta for consumers' utility functions
        self.A = Nested_Loop_C(self.c,self.g)
        self.B = Nested_Loop_B(self.c,self.f)
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
        for i in range(100):
            compare = minimize(G.Welfare,output_list,method = 'SLSQP',constraints = G.Constraints(output_list))
            if res.fun > compare.fun:
                res = compare
        return res.fun
    def Equilibrium_Ind(self):
        # Obtain the output list with the correct list length
        # Format of output list: [C1G1 C1G2 C2G1 C2G2 C1F1 C1F2 C2F1 C2F2 P1F1 P1F2 P2F1 P2F2]
        output_list_length = self.c * (self.g + self.f) + self.g * self.f
        output_list = []
        # Generate initial output list values for the optimization
        for i in range(output_list_length):
            output_list.append(random.uniform(0.3,5))
            
        # Solve the optimization problem
        # G: An instance of the social planner, who determines the welfare function and constraints
        G = SP(self.c,self.g,self.f,self.A,self.B,self.T,self.e1)
        # res: Results of optimization problem
        res = minimize(G.Welfare,output_list,method = 'SLSQP',constraints = G.Constraints_Ind(output_list))
        for i in range(100):
            output_list = []
            for i in range(output_list_length):
                output_list.append(random.uniform(0.3,5))
            compare = minimize(G.Welfare,output_list,method = 'SLSQP',constraints = G.Constraints_Ind(output_list))
            if res.fun > compare.fun:
                res = compare
        
        P = Producer(self.c,self.g,self.f,self.e1)
        real = P.Production(res.x)
        for i in range(self.g*self.c):
            if i == 0 or (i % self.g == 0 and i < self.g*self.c):
                res.x[i:i+self.g] = real/self.c
        welfare = G.Welfare(res.x)
        return welfare

    


# TEST CASE
# E1: An instance of Economy
E1 = Economy(2,3,2,e1=0.1)
# Obtain equilibrium results
'''
Two types of social planner:
Ind: the social planner that could only observe the individual production externality 
Sp: the "smarter" social planner that could observe the aggregate production externality
'''
Ind = -E1.Equilibrium_Ind()
Sp = -E1.Equilibrium()
dif = Sp - Ind
print "The welfare obtain by the smarter social planner is %6.4f" %Sp
print "It is %6.4f greater than the welfare obtain by the other SP" %dif