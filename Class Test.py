"""Created on Mon Apr 02 14:36:47 2018"""

"""@author: WeiJin"""

import numpy as np
import random
import math
import scipy
from scipy.optimize import minimize


"""Defining method functions"""
# Randomising from a range of integers
def Nested_Loop_Int(layer_1,layer_2,min_int,max_int):
    X = np.array([])
    loop_output = np.array([])
    i = 0
    while i < layer_1:
        j = 0
        while j < layer_2:
            X = np.append(X,random.randint(min_int,max_int))
            j += 1
        loop_output = np.append(loop_output,X)
        X = np.array([])
        i += 1
    return loop_output

# Randomising from a range between 0 amd 1
def Loop(layer,dp):
    loop_output = np.array([])
    i = 0
    while i < layer:
        loop_output = np.append(loop_output,round(random.random(),dp))
        i += 1
    return loop_output

# Randomising from a range between 0 amd 1
def Nested_Loop(layer_1,layer_2,dp):
    X = np.array([])
    loop_output = np.array([])
    i = 0
    while i < layer_1:
        j = 0
        while j < layer_2:
            X = np.append(X,round(random.random(),dp))
            j += 1
        loop_output = np.append(loop_output,X)
        X = np.array([])
        i += 1
    return loop_output

# Mathematical operations across certain elements in an array
def Loop_Slice(array,step):
    X = np.array([])
    loop_output = np.array([])
    i = 1
    while i <= step:
        X = np.sum(array[i - 1::step])
        loop_output = np.append(loop_output,X)
        i += 1
    return loop_output

"""Setting up the economy"""
# Obtain number of consumers in the economy
total_consumers = input("Please enter the number of consumers in the economy:")
# Obtain number of goods produced in the economy
total_goods = input("Please enter the number of types of goods produced in the economy:")
# Obtain number of factors available in the economy
total_factors = input("Please enter the number of types of factors available in the economy:")

"""Defining the agents in the economy"""
class Consumption():
    def __init__(self,min,max):
        c_list = Nested_Loop_Int(total_consumers,total_goods,min,max)
    def welfare_max(self,c_list,f_list):
        total_cons = Loop_Slice(c_list,total_goods)
        # Obtain parameters
        y = round(random.random(),2)
        s = round(random.random(),2)
        A = Nested_Loop(total_consumers,total_goods,2)
        B = Loop(total_consumers,2)
        T = Loop(total_factors,2)
        # Calculate utility
        weighted_utility_subc = np.multiply((c_list ** y) , A)
        utility_subc = np.array([])
        for i in range(len(weighted_utility_subc)):
            if i == 0:
                #Need to make sure y is non-zero
                utility_subc = np.append(utility_subc,(np.sum(weighted_utility_subc[i:i + total_goods])) ** ((1 - s) / y))
            elif i % total_goods == 0 and i < total_goods * total_consumers:
                utility_subc = np.append(utility_subc,(np.sum(weighted_utility_subc[i:i + total_goods])) ** ((1 - s) / y))
           
        tweighted_utility_subf = np.array([])
        i = 0
        while i < total_consumers:
            j = 0
            while j < total_factors:
                tweighted_utility_subf = np.append(tweighted_utility_subf,((f_list[(i * total_factors) + j] ** (1 + T[j])) / (1 + T[j])))
                j += 1
            i += 1
        
        weighted_utility_subf = np.array([])
        for i in range(len(tweighted_utility_subf)):
            if i == 0:
                weighted_utility_subf = np.append(weighted_utility_subf,((tweighted_utility_subf[i:i + total_factors]) * B[i]))
            elif i % total_factors == 0 and i < total_consumers * total_factors:
                weighted_utility_subf = np.append(weighted_utility_subf,(tweighted_utility_subf[i:i + total_factors]) * B[i / total_factors])
        
        utility_subf = np.array([])
        for i in range(len(weighted_utility_subf)):
            if i == 0:
                utility_subf = np.append(utility_subf,(np.sum(weighted_utility_subf[i:i + total_factors])))
            elif i % total_factors == 0 and i < total_consumers * total_factors:
                utility_subf = np.append(utility_subf,(np.sum(weighted_utility_subf[i:i + total_factors])))
        
        utility_list = np.array([])
        utility_list = np.round((utility_subc - utility_subf) , 2)
        
        # Overall weight for the welfare function
        overall_weight = 1 / (random.random())
        # Individual weights for the welfare function
        utility_weights = Loop(total_consumers,2)
        # Make utilities positive
        utility_list_square = utility_list ** 2
        # Maximize welfare
        welfare = (np.sum(np.power(utility_list_square , utility_weights))) ** overall_weight
        return welfare
    
class Production():
    def __init__(self,min,max):
        f_list = Nested_Loop_Int(total_goods,total_factors,min,max)
    def total_production(min,max):
        f_list = Nested_Loop_Int(total_goods,total_factors,min,max)
        total_factor = Loop_Slice(f_list,total_factors)
        # Obtain parameters
        X = Loop(total_goods,2)
        P = Nested_Loop(total_goods,total_factors,2)
        # Calculate production
        weighted_F_list = np.array([])
        weightedflist = np.array([])
        i = 0
        while i < total_goods:
            j = 0
            while j < total_factors:
                weightedflist = np.append(weightedflist,((f_list[(i * total_factors) + j] ** (1 - X[i])) / (1 - X[i])) * P[(i * total_factors) + j])
                j += 1
            weighted_F_list = np.append(weighted_F_list,weightedflist)
            weightedflist = np.array([])
            i += 1
        
        total_prod = np.array([])
        for i in range(len(weighted_F_list)):
            if i == 0:
                total_prod = np.append(total_prod,round(np.sum(weighted_F_list[i:i + total_factors]),0))
            elif i % total_factors == 0 and i < total_factors * total_goods:
                total_prod = np.append(total_prod,round(np.sum(weighted_F_list[i:i + total_factors]),0))
        return total_prod
    
c_list = Nested_Loop_Int(total_consumers,total_goods,0,10)
f_list = Nested_Loop_Int(total_consumers,total_factors,0,10)
consumption = Consumption(0,10)
production = Production(0,7)
length = len(c_list) + len(f_list)
max = scipy.optimize.minimize(consumption.welfare_max(),length)
print max

