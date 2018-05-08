
"""
Created on Mon Apr 02 16:34:45 2018
"""
"""
@author: WeiJin,PoHan
"""

import numpy as np
import random

"""
Define some useful functions for iteration through different lists
"""

"""
Randomising from a range between 0 amd 1(to obtain parameters)
"""

def Loop(layer,dp):
    loop_output = np.array([])
    i = 0
    while i < layer:
        loop_output = np.append(loop_output,round(random.uniform(0.2,0.9),dp))
        i += 1
    return loop_output

"""
Randomising from a range between 0 amd 1 (to obtain parameters)
"""

def Nested_Loop_C(layer_1,layer_2,dp):
    X = np.array([])
    loop_output = np.array([])
    i = 0
    while i < layer_1:
        j = 0
        while j < layer_2:
            X = np.append(X,round(random.uniform(0.2,0.9),dp))
            j += 1
        loop_output = np.append(loop_output,X)
        X = np.array([])
        i += 1
    return loop_output

def Nested_Loop_P(layer_1,layer_2,dp):
    X = np.array([])
    loop_output = np.array([])
    i = 0
    while i < layer_1:
        j = 0
        while j < layer_2:
            X = np.append(X,round(random.uniform(0.5,0.9),dp))
            j += 1
        loop_output = np.append(loop_output,X)
        X = np.array([])
        i += 1
    return loop_output

def Nested_Loop_Ex(layer_1,layer_2,dp):
    X = np.array([])
    loop_output = np.array([])
    i = 0
    while i < layer_1:
        j = 0
        while j < layer_2:
            X = np.append(X,round(random.uniform(0.2,0.49),dp))
            j += 1
        loop_output = np.append(loop_output,X)
        X = np.array([])
        i += 1
    return loop_output
"""
Mathematical operations across certain elements in an array (to obtain parameters)
"""
def Loop_Slice(array,step):
    X = np.array([])
    loop_output = np.array([])
    i = 1
    while i <= step:
        X = np.sum(array[i - 1::step])
        loop_output = np.append(loop_output,X)
        i += 1
    return loop_output

"""
Here are some functions that are used to construct the constraints
"""
class Total(object):
    def __init__(self,c,g,f):
        self.c = c
        self.f = f
        self.g = g
    def total_consumption(self,output_list):
        # Used in first constraint
        consumption_length = self.c * self.g
        factor_ss_length = self.c * self.f
        consumer_length = consumption_length + factor_ss_length
        c_list = np.array(output_list[0:consumption_length])
        total_cons = Loop_Slice(c_list,self.g)
        return total_cons   
    
    def total_factor_ss(self,output_list):
        # Used in second constraint
        consumption_length = self.c * self.g
        factor_ss_length = self.c * self.f
        consumer_length = consumption_length + factor_ss_length
        f_list = np.array(output_list[consumption_length:consumption_length + factor_ss_length])
        factor_ss = Loop_Slice(f_list,self.f)
        return factor_ss
    
    def total_factor_dd(self,output_list):
        # Used in second constraint
        consumption_length = self.c * self.g
        factor_ss_length = self.c * self.f
        consumer_length = consumption_length + factor_ss_length
        f_list = np.array(output_list[consumer_length:consumer_length + self.g * self.f])
        factor_dd = Loop_Slice(f_list,self.f)
        return factor_dd
    