"""
Created on Mon Apr 02 16:34:45 2018

@author: WeiJin,PoHan
"""

# Import tools
import numpy as np


# Define a class called Consumer to simulate the consumption preferences and factor supply of each consumer in the economy
class Consumer(object):
    def __init__(self,c,g,f,A,B,T):
        # c: Number of consumers in the economy
        # g: Number of goods produced in the economy
        # f: Number of factors used in the production
        # A, B, T: Parameters alpha, beta, theta from the consumer's utility function
        self.c = c
        self.g = g
        self.f = f
        self.A = A
        self.B = B
        self.T = T
        
    def Utility(self,output_list):
        # Setting up the calculation of consumer utility
        
        # Calculate the lengths of different segments in the output list 
        consumption_length = self.c * self.g
        factor_ss_length = self.c * self.f
        # Define c_list as the first segment of the output list that contains the consumption quantity of each good by each consumer
        c_list = np.array(output_list[0:consumption_length])
        # Define f_list as the second segment of the output list that contains the factor supply quantities of each factor by each consumer
        f_list = np.array(output_list[consumption_length:consumption_length + factor_ss_length])
        
        # Generate consumption utility parameters
        # y: gamma; s: sigma
        y = float(5)
        s = float(0.5)
        
        # Calculate the utility that comes from consumption of goods
        # Define weighted_utility_subc an array containing the un-summed elements of the consumption part of the utility function for each consumer
        weighted_utility_subc = np.multiply((c_list ** y) , self.A)
        # Define utility_subc as an array containing the consumption part of the utility function for each consumer
        utility_subc = np.array([])
        # Sum up the elements in weighted_utility_subc 
        for i in range(len(weighted_utility_subc)):
            if (i == 0) or (i % self.g == 0 and i < self.g * self.c):
                utility_subc = np.append(utility_subc,(np.sum(weighted_utility_subc[i:i + self.g])) ** ((1 - s) / y))
        
        # Define twighted_utility_subf as an arra containing the un-summed elements of the factor supply part of the utility function for each consumer
        # tweighted_utility_subf is the initial stage of forming the factor supply part of the utility function
        tweighted_utility_subf = np.array([])
        i = 0
        while i < self.c:
            j = 0
            while j < self.f:
                tweighted_utility_subf = np.append(tweighted_utility_subf,((f_list[(i * self.f) + j] ** (1 + self.T[j])) / (1 + self.T[j])))
                j += 1
            i += 1
        
        # Define weighted_utility_subf as an array containing the un-summed elements of the factor supply part of the utility function for each consumer
        # weighted_utility_subf is the intermediate stage of forming the factor supply part of the utlity function
        weighted_utility_subf = np.array([])
        for i in range(len(tweighted_utility_subf)):
            if i == 0:
                weighted_utility_subf = np.append(weighted_utility_subf,((tweighted_utility_subf[i:i + self.f]) * self.B[i]))
            if i % self.f == 0 and i < self.c * self.f:
                weighted_utility_subf = np.append(weighted_utility_subf,(tweighted_utility_subf[i:i + self.f]) * self.B[i / self.f])
        
        # Define utility_subf as an array containing the factor supply part of the utility function for each consumer 
        utility_subf = np.array([])
        # Sum up elements in weighted_utility_subf
        for i in range(len(weighted_utility_subf)):
            if (i== 0) or (i % self.f == 0 and i < self.c * self.f):
                utility_subf = np.append(utility_subf,(np.sum(weighted_utility_subf[i:i + self.f])))
                
        # Combining consumption and factor supply parts of the utility function
        # Define utility list as an array containing the utility of each consumer
        utility_list = np.array([])
        # Utility is determined by the consumption of goods and supply of factors
        utility_list = np.round((utility_subc - utility_subf) , 2)
        return utility_list