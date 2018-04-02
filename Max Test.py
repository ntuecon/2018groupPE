# -*- coding: utf-8 -*-
"""
Created on Mon Apr 02 16:34:45 2018

@author: WeiJin
"""

import numpy as np
import random
import scipy
from scipy.optimize import minimize

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

"""Setting up the economy"""
# Obtain number of consumers in the economy
total_consumers = int(input("Please enter the number of consumers in the economy:"))
# Obtain number of goods produced in the economy
total_goods = int(input("Please enter the number of types of goods produced in the economy:"))
# Obtain number of factors available in the economy
total_factors = int(input("Please enter the number of types of factors available in the economy:"))

class Consumption():
    def __init__(self):
        print ""
    def welfare_max(self,output_list):
        # lengths of output list
        consumption_length = total_consumers * total_goods
        factor_length = total_consumers * total_goods
        total_length = consumption_length + factor_length
        # Consumption list
        c_list = np.array(output_list[0:consumption_length])
        print c_list
        f_list = np.array(output_list[consumption_length:total_length])
        print f_list
        # Obtain parameters
        y = random.randint(1,5)
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
        neg_welfare = welfare * -1
        return neg_welfare
    
consumption = Consumption()
output_list_length = total_consumers * (total_goods + total_factors)
output_list = []
i = 0
for i in range(output_list_length):
    output_list.append(1)
max = scipy.optimize.minimize(consumption.welfare_max,output_list)
