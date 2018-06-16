"""
Created on Mon Apr 02 16:34:45 2018

@author: WeiJin,PoHan
"""

# Import tools
import numpy as np
import random


# Define some useful functions for list iterations, or to generate function parameters

# Generate function parameters using loop. Returns an array with length = number of parameters 
def Loop(layer):
    loop_output = np.array([])
    i = 0
    while i < layer:
        loop_output = np.append(loop_output,0.95)
        i += 1
    return loop_output

# Generate function parameters using nested loop. Returns an array with length = number of parameters
# For consumer utility functions
def Nested_Loop_C(layer_1,layer_2):
    X = np.array([])
    loop_output = np.array([])
    i = 0
    while i < layer_1:
        j = 0
        while j < layer_2:
            X = np.append(X,random.uniform(0.5,0.52))
            j += 1
        loop_output = np.append(loop_output,X)
        X = np.array([])
        i += 1
    return loop_output

# For producer production functions without externality
def Nested_Loop_P(layer_1,layer_2):
    X = np.array([])
    loop_output = np.array([])
    i = 0
    while i < layer_1:
        j = 0
        while j < layer_2:
            # Differentiating the efficiency of the last factor by each firm (at most 3 types of firms)
            # Coefficient of the production function for non-last factor is between 0.6 and 0.7
            if j < layer_2 - 1:
                X = np.append(X,round(random.uniform(0.6,0.7)))
            # Coefficient of the production function for last factor is differentiated
            else:
                # Last firm has lowest efficiency level
                if i == layer_1 - 1:
                    X = np.append(X,0)
                # First firm has highest efficiency level
                elif i == 0:
                    X = np.append(X,round(random.uniform(0.9,0.92)))
                # The rest of the firms have middle efficiency level
                else:
                    X = np.append(X,round(random.uniform(0.5,0.52)))
            j += 1
        loop_output = np.append(loop_output,X)
        X = np.array([])
        i += 1
    return loop_output


# Mathematical operations across certain elements in an array (to obtain parameters)
# Starts with the first element of the first group
def Loop_Slice(array,step):
    X = np.array([])
    loop_output = np.array([])
    i = 1
    # Determine the step to skip elements within an array
    while i <= step:
        # Add up selected elements, while skipping the other elements
        X = np.sum(array[i - 1::step])
        loop_output = np.append(loop_output,X)
        i += 1
    return loop_output

# Mathematical operations across certain elements in an array (to obtain parameters)
# For reduction of efficiency when there is an externality
# Starts with the last element of the first group
def Loop_Slice_Ex(array,step,goods,tf):
    X = np.array([])
    loop_output = np.array([])
    i = 1
    while i <= step * goods:
        # Assumes that the last factor is the one causing the externality
        # Therefore, the last factor of all goods suffer from reduced efficiency
        if i % step == 0:
            X = array[i - 1] * tf
            loop_output = np.append(loop_output,X)
        else:
            loop_output = np.append(loop_output,array[i - 1])
        i += 1
    return loop_output

# Functions that are used to construct the optimization constraints
class Total(object):
    def __init__(self,c,g,f):
        # c: Number of consumers in the economy
        # g: Number of goods produced in the economy
        # f: Number of factors used in the production
        self.c = c
        self.f = f
        self.g = g
    
    # Used in first constraint: Total consumption = Total production of each good
    # Obtain total consumption of each good
    def total_consumption(self,output_list):
        # Obtain the length of the consumption segment of the output list
        consumption_length = self.c * self.g
        # Define the consumption segnment of the output list as c_list
        # The c_list contains the consumption quantity of each good by each consumer
        c_list = np.array(output_list[0:consumption_length])
        # Add up total consumption of each good 
        total_cons = Loop_Slice(c_list,self.g)
        return total_cons   
    
    # Used in second constraint: Total factor supplied = Total factor demanded of each factor
    # Obtain total factor supplied of each factor
    def total_factor_ss(self,output_list):
        # Obtain the length of the factor supply segment of the output list
        consumption_length = self.c * self.g
        factor_ss_length = self.c * self.f
        # Define the factor supply segment of the output list as f_list
        # The f_list contains the factor supply quantity of each factor by each consumer
        f_list = np.array(output_list[consumption_length:consumption_length + factor_ss_length])
        # Add up the total factor supplied of each factor
        factor_ss = Loop_Slice(f_list,self.f)
        return factor_ss
    
    # Used in second constraint: Total factor supplied = Total factor demanded of each factor
    # Obtain total factor demanded of each factor
    def total_factor_dd(self,output_list):
        # Obtain the length of the factor demand segment of the output list
        consumption_length = self.c * self.g
        factor_ss_length = self.c * self.f
        consumer_length = consumption_length + factor_ss_length
        # The f_list contains the factor demand quantity of each factor by each producer
        f_list = np.array(output_list[consumer_length:consumer_length + self.g * self.f])
        # Add up the total factor demanded of each factor
        factor_dd = Loop_Slice(f_list,self.f)
        return factor_dd   