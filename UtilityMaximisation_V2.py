"""Created on Fri Mar 23 15:26:13 2018"""

"""@author: WeiJin"""


import numpy as np
import random
import math

"""Randomising from a range of integers"""
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

"""Randomising from a range between 0 amd 1"""
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

"""Mathematical operations across certain elements in an array"""
def Loop_Slice(array,step):
    X = np.array([])
    loop_output = np.array([])
    i = 1
    while i <= step:
        X = np.sum(array[i - 1::step])
        loop_output = np.append(loop_output,X)
        i += 1
    return loop_output

"""Randomising from a range between 0 amd 1"""
def Loop(layer,dp):
    loop_output = np.array([])
    i = 0
    while i < layer:
        loop_output = np.append(loop_output,round(random.random(),dp))
        i += 1
    return loop_output


"""Obtain number of consumers in the economy"""
total_consumers = input("Please enter the number of consumers in the economy:")
"""Obtain number of goods produced in the economy"""
total_goods = input("Please enter the number of types of goods produced in the economy:")
total_factors = input("Please enter the number of types of factors available in the economy:")

"""Construct market clearing constraints"""
print ""
"""Consolidate the consumption quantities of each good of each consumer"""
C_list = np.array([])
C_list = Nested_Loop_Int(total_consumers,total_goods,0,10)
print "The list of consumption quantities of each good of each consumer is:",C_list
print ""

"""Obtain total consumption of each good"""
total_cons = np.array([])
total_cons = Loop_Slice(C_list,total_goods)
print "The total consumption quantity of each good is:",total_cons
print ""

"""Consolidate the factor quantities used to produce each type of good"""
F_list = np.array([])
F_list = Nested_Loop_Int(total_goods,total_factors,0,5)
print "The list of factor quantities of each factor used to produce each good is:",F_list
print ""

"""Define the CES production function"""

"""Compile list of attributes that enter the production function"""
X = np.array([])
X = Loop(total_goods,2)
print "The corresponding parameter X for each good is:",X
print ""

P = np.array([])
P = Nested_Loop(total_goods,total_factors,2)
print "The corresponding parameter P for each factor for each good is:",P
print ""

"""Obtain the total production quantity of each good"""
weighted_F_list = np.array([])
weightedflist = np.array([])
i = 0
while i < total_goods:
    j = 0
    while j < total_factors:
        weightedflist = np.append(weightedflist,((F_list[(i * total_factors) + j] ** (1 - X[i])) / (1 - X[i])) * P[(i * total_factors) + j])
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
print "The total production quantity of each good is:",total_prod
print ""
"""First market constraint is that the total consumption of each good is equal to the total
production of each good given CES production function. Hence total_cons == total_prod"""

"""Obtain total factor quantity of each factor demanded"""
total_factor_dd = np.array([])
total_factor_dd = Loop_Slice(F_list,total_factors)
print "The total factor quantity of each factor demanded is:",total_factor_dd
print ""

"""Obtain factor quantities of each factor supplied from each consumer"""
factor_list = np.array([])
factor_list = Nested_Loop_Int(total_consumers,total_factors,0,10)
print "The list of factor quantities of each factor supplied by each consumer is:",factor_list
print ""

"""Obtain total factor supplied for each factor"""
total_factor_ss = np.array([])
total_factor_ss = Loop_Slice(factor_list,total_factors)
print "The total factor quantity supplied for each factor is:",total_factor_ss
print ""
"""Second market constraint is that the total factor quantity supplied for each factor is equal
to the total factor quantity demanded for each factor. Hence, total_factor_ss == total_factor_dd"""


"""Define social welfare maximisation function"""
"""Assume different weights attached to the utility of different consumers"""
utility_weights = np.array([])
utility_weights = Loop(total_consumers,2)
print "The corresponding weights on utilities of each consumer is:",utility_weights
print ""

"""Define the CES utility function"""
"""Compile list of attributes that enter the utility function"""
y = round(random.random(),2)
print "Parameter y is:",y
print ""

s = round(random.random(),2)
print "Parameter s is:",s
print ""

A = np.array([])
A = Nested_Loop(total_consumers,total_goods,2)
print "The corresponding parameter A for each good for each consumer is:",A
print ""

B = np.array([])
B = Loop(total_consumers,2)
print "The corresponding parameter B for each consumer is:",B
print ""

T = np.array([])
T = Loop(total_factors,2)
print "The corresponding parameter T for each factor is:",T
print ""

"""Obtain the total utility of each consumer"""
weighted_utility_subc = np.multiply((C_list ** y) , A)

utility_subc = np.array([])

for i in range(len(weighted_utility_subc)):
    if i == 0:
        """Need to make sure y is non-zero"""
        utility_subc = np.append(utility_subc,(np.sum(weighted_utility_subc[i:i + total_goods])) ** ((1 - s) / y))
    elif i % total_goods == 0 and i < total_goods * total_consumers:
        utility_subc = np.append(utility_subc,(np.sum(weighted_utility_subc[i:i + total_goods])) ** ((1 - s) / y))
       
tweighted_utility_subf = np.array([])
i = 0
while i < total_consumers:
    j = 0
    while j < total_factors:
        tweighted_utility_subf = np.append(tweighted_utility_subf,((factor_list[(i * total_factors) + j] ** (1 + T[j])) / (1 + T[j])))
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
print "The utility list is:",utility_list
print ""

"""Obtain the welfare maximisation function"""
"""Welfare maximisation function used here is (sum of (utility^2)^utilityweights)^overall_weight"""
"""Obtain overall weight for the welfare maximisation function"""
overall_weight = 1 / (random.random())
print "The overall weight attached to the welfare maximisation function is:",overall_weight
print ""
"""Make the utilities positive"""
utility_list_square = utility_list ** 2
welfare_max = (np.sum(np.power(utility_list_square , utility_weights))) ** overall_weight
print "The welfare maximisation function is:",welfare_max