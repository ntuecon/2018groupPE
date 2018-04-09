"""Created on Mon Apr 02 16:34:45 2018"""
"""@author: WeiJin,PoHan"""

import numpy as np
import random
import scipy
from scipy.optimize import minimize


# Randomising from a range between 0 amd 1(to obtain parameters)
def Loop(layer,dp):
    loop_output = np.array([])
    i = 0
    while i < layer:
        loop_output = np.append(loop_output,round(random.random(),dp))
        i += 1
    return loop_output

# Randomising from a range between 0 amd 1(to obtain parameters)
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

#Mathematical operations across certain elements in an array(to obtain parameters)
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
total_consumers = int(input("Please enter the number of consumers in the economy:"))

# Obtain number of goods produced in the economy
total_goods = int(input("Please enter the number of types of goods produced in the economy:"))

# Obtain number of factors available in the economy
total_factors = int(input("Please enter the number of types of factors available in the economy:"))

# Obtain output list lengths. 
#These numbers would be useful when manipulating the long list that consists of goods/factors demanded/supplied by each consumer
consumption_length = total_consumers * total_goods
factor_ss_length = total_consumers * total_factors
consumer_length = consumption_length + factor_ss_length

# Randomizing parameters
# Utility Function
y = random.randint(1,5)
s = round(random.random(),2)
A = Nested_Loop(total_consumers,total_goods,2)
B = Loop(total_consumers,2)
T = Loop(total_factors,2)
# Welfare function
overall_weight = 1 / (random.random())
utility_weights = Loop(total_consumers,2)
# Production function
X = Loop(total_goods,2)
P = Nested_Loop(total_goods,total_factors,2)


class Consumption():
    def __init__(self):
        print ""
    
    def welfare_max(self,output_list):
        # THIS FUNCTION RETURNS A NUMBER (FOR OPTIMIZATION)
        # Construct the consumption list
        c_list = np.array(output_list[0:consumption_length])
        f_list = np.array(output_list[consumption_length:consumption_length + factor_ss_length])
        # Calculate utility
        #The part from consuming goods
        weighted_utility_subc = np.multiply((c_list ** y) , A)
        utility_subc = np.array([])
        for i in range(len(weighted_utility_subc)):
            if (i == 0) or (i % total_goods == 0 and i < total_goods * total_consumers):
                utility_subc = np.append(utility_subc,(np.sum(weighted_utility_subc[i:i + total_goods])) ** ((1 - s) / y))
        #The part from supplying factors  
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
            if i % total_factors == 0 and i < total_consumers * total_factors:
                weighted_utility_subf = np.append(weighted_utility_subf,(tweighted_utility_subf[i:i + total_factors]) * B[i / total_factors])
        
        utility_subf = np.array([])
        for i in range(len(weighted_utility_subf)):
            if (i== 0) or (i % total_factors == 0 and i < total_consumers * total_factors):
                utility_subf = np.append(utility_subf,(np.sum(weighted_utility_subf[i:i + total_factors])))
                
        #combinding the goods part and the factors part of the utility function
        utility_list = np.array([])
        utility_list = np.round((utility_subc - utility_subf) , 2)
        
        # Make utilities positive
        utility_list_square = utility_list ** 2
        # Define the welfare function
        welfare = (np.sum(np.power(utility_list_square , utility_weights))) ** overall_weight
        neg_welfare = welfare * -1
        return neg_welfare
    
    def total_production(self,output_list):
        #This function retrun total production for each goods given the factors used to produce them
        # Used in first constraint
        # Factor list
        f_list = np.array(output_list[consumer_length:consumer_length + total_goods * total_factors])
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
            if (i == 0) or (i % total_factors == 0 and i < total_factors * total_goods):
                total_prod = np.append(total_prod,round(np.sum(weighted_F_list[i:i + total_factors]),0))
        return total_prod
    
    #The following functions just serve for constructing the constraints 
    def total_consumption(self,output_list):
        # Used in first constraint
        c_list = np.array(output_list[0:consumption_length])
        total_cons = Loop_Slice(c_list,total_goods)
        return total_cons
    
    def total_factor_ss(self,output_list):
        # Used in second constraint
        f_list = np.array(output_list[consumption_length:consumption_length + factor_ss_length])
        factor_ss = Loop_Slice(f_list,total_factors)
        return factor_ss
    
    def total_factor_dd(self,output_list):
        # Used in second constraint
        f_list = np.array(output_list[consumer_length:consumer_length + total_goods * total_factors])
        factor_dd = Loop_Slice(f_list,total_factors)
        return factor_dd
    
       
consumption = Consumption()
output_list_length = total_consumers * (total_goods + total_factors) + total_goods * total_factors
output_list = []
i = 0
for i in range(output_list_length):
    output_list.append(random.random())


Cons = ({'type': 'eq','fun' : lambda x:(consumption.total_consumption(x)-consumption.total_production(x))},
        {'type': 'eq','fun' : lambda x:(consumption.total_factor_dd(x)-consumption.total_factor_ss(x))},
        {'type': 'ineq','fun': lambda x:x[0]},
        {'type': 'ineq','fun': lambda x:x[1]},
        {'type': 'ineq','fun': lambda x:x[2]},
        {'type': 'ineq','fun': lambda x:x[3]},
        {'type': 'ineq','fun': lambda x:x[4]},
        {'type': 'ineq','fun': lambda x:x[5]},
        {'type': 'ineq','fun': lambda x:x[6]},
        {'type': 'ineq','fun': lambda x:x[7]},
        {'type': 'ineq','fun': lambda x:x[8]},
        {'type': 'ineq','fun': lambda x:x[9]},
        {'type': 'ineq','fun': lambda x:x[10]},
        {'type': 'ineq','fun': lambda x:x[11]})

res = minimize(consumption.welfare_max,output_list,method = 'SLSQP',constraints = Cons)
print res