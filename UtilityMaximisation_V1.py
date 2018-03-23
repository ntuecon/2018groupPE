"""Created on Tue Mar 20 11:16:21 2018"""

"""@author: WeiJin"""


import numpy as np
import math
import random


"""Obtain number of consumers in the economy"""
totalconsumers = input("Please enter the number of consumers in the economy:")
"""Obtain number of goods produced in the economy"""
totalgoods = input("Please enter the number of types of goods produced in the economy:")
totalfactors = input("Please enter the number of types of factors available in the economy:")

"""Construct market clearing constraints"""

"""Consolidate the consumption quantities of each good of each consumer"""
C = np.array([])
Clist = np.array([])
i = 0
while i < totalconsumers:
    j = 0
    while j < totalgoods:
        c = random.randint(0,10)
        C = np.append(C,c)
        j += 1
    Clist = np.append(Clist,C)
    C = np.array([])
    i += 1
print "The list of consumption quantities of each good of each consumer is:",Clist

"""Obtain total consumption of each good"""
total_cons = np.array([])
eachtotal = np.array([])
i = 1
while i <= totalgoods:
    eachtotal = np.sum(Clist[i - 1::totalgoods])
    total_cons = np.append(total_cons,eachtotal)
    i += 1
print "The total consumption quantity of each good is:",total_cons

"""Consolidate the factor quantities used to produce each type of good"""
F = np.array([])
Flist = np.array([])
i = 0
while i < totalgoods:
    j = 0
    while j < totalfactors:
        f = random.randint(0,5)
        F = np.append(F,f)
        j += 1
    Flist = np.append(Flist,F)
    F = np.array([])
    i += 1
print "The list of factor quantities of each factor used to produce each good is:",Flist

"""Define the CES production function"""

"""Compile list of attributes that enter the production function"""
X = np.array([])
x = np.array([])
i = 0
while i < totalgoods:
    x = round(random.random(),2)
    X = np.append(X,x)
    i += 1
print "The corresponding parameter X for each good is:",X
P = np.array([])
p = np.array([])
pp = np.array([])
i = 0
while i < totalgoods:
    j = 0
    while j < totalfactors:
        """not sure what kind of numbers this should take"""
        p = round(random.random(),2)
        pp = np.append(pp,p)
        j += 1
    P = np.append(P,pp)
    pp = np.array([])
    i += 1
print "The corresponding parameter P for each factor for each good is:",P

"""Obtain the total production quantity of each good"""
weightedFlist = np.array([])
weightedflist = np.array([])
i = 0
while i < totalgoods:
    j = 0
    while j < totalfactors:
        weightedflist = np.append(weightedflist,((Flist[(i * totalfactors) + j] ** (1 - X[i])) / (1 - X[i])) * P[(i * totalfactors) + j])
        j += 1
    weightedFlist = np.append(weightedFlist,weightedflist)
    weightedflist = np.array([])
    i += 1

total_prod = np.array([])
for i in range(len(weightedFlist)):
    if i == 0:
        total_prod = np.append(total_prod,round(np.sum(weightedFlist[i:i + totalfactors]),0))
    elif i % totalfactors == 0 and i < totalfactors * totalgoods:
        total_prod = np.append(total_prod,round(np.sum(weightedFlist[i:i + totalfactors]),0))
print "The total production quantity of each good is:",total_prod

"""First market constraint is that the total consumption of each good is equal to the total
production of each good given CES production function. Hence total_cons == total_prod"""

"""Obtain total factor quantity of each factor demanded"""
total_factor_dd = np.array([])
eachtotal = np.array([])
i = 1
while i <= totalfactors:
    eachtotal = np.sum(Flist[i - 1::totalfactors])
    total_factor_dd = np.append(total_factor_dd,eachtotal)
    i += 1
print "The total factor quantity of each factor demanded is:",total_factor_dd

"""Obtain factor quantities of each factor supplied from each consumer"""
F = np.array([])
factor_list = np.array([])
i = 0
while i < totalconsumers:
    j = 0
    while j < totalfactors:
        f = random.randint(0,10)
        F = np.append(F,f)
        j += 1
    factor_list = np.append(factor_list,F)
    F = np.array([])
    i += 1
print "The list of factor quantities of each factor supplied by each consumer is:",factor_list

"""Obtain total factor supplied for each factor"""
total_factor_ss = np.array([])
eachtotal = np.array([])
i = 1
while i <= totalfactors:
    eachtotal = np.sum(factor_list[i - 1::totalfactors])
    total_factor_ss = np.append(total_factor_ss,eachtotal)
    i += 1
print "The total factor quantity supplied for each factor is:",total_factor_ss
"""Second market constraint is that the total factor quantity supplied for each factor is equal
to the total factor quantity demanded for each factor. Hence, total_factor_ss == total_factor_dd"""


"""Define social welfare maximisation function"""
"""Assume different weights attached to the utility of different consumers"""
utilityweights = np.array([])
i = 0
while i < totalconsumers:
    utilityweights = np.append(utilityweights,round(random.random(),2))
    i += 1
print "The corresponding weights on utilities of each consumer is:",utilityweights


"""Define the CES utility function"""
"""Compile list of attributes that enter the utility function"""
y = round(random.random(),2)
print "Parameter y is:",y
s = round(random.random(),2)
print "Parameter s is:",s
A = np.array([])
a = np.array([])
aa = np.array([])
i = 0
while i < totalconsumers:
    j = 0
    while j < totalgoods:
        """not sure what kind of numbers this should take"""
        a = round(random.random(),2)
        aa = np.append(aa,a)
        j += 1
    A = np.append(A,aa)
    aa = np.array([])
    i += 1
print "The corresponding parameter A for each good for each consumer is:",A

B = np.array([])
b = np.array([])
i = 0
while i < totalconsumers:
    b = round(random.random(),2)
    B = np.append(B,b)
    i += 1
print "The corresponding parameter B for each consumer is:",B

T = np.array([])
t = np.array([])
i = 0
while i < totalfactors:
    t = round(random.random(),2)
    T = np.append(T,t)
    i += 1
print "The corresponding parameter T for each factor is:",T

"""Obtain the total utility of each consumer"""
weighted_utility_subc = np.multiply((Clist ** y) , A)

utility_subc = np.array([])

for i in range(len(weighted_utility_subc)):
    if i == 0:
        """Need to make sure y is non-zero"""
        utility_subc = np.append(utility_subc,(np.sum(weighted_utility_subc[i:i + totalgoods])) ** ((1 - s) / y))
    elif i % totalgoods == 0 and i < totalgoods * totalconsumers:
        utility_subc = np.append(utility_subc,(np.sum(weighted_utility_subc[i:i + totalgoods])) ** ((1 - s) / y))
       
tweighted_utility_subf = np.array([])
i = 0
while i < totalconsumers:
    j = 0
    while j < totalfactors:
        tweighted_utility_subf = np.append(tweighted_utility_subf,((factor_list[(i * totalfactors) + j] ** (1 + T[j])) / (1 + T[j])))
        j += 1
    i += 1

weighted_utility_subf = np.array([])
for i in range(len(tweighted_utility_subf)):
    if i == 0:
        weighted_utility_subf = np.append(weighted_utility_subf,((tweighted_utility_subf[i:i + totalfactors]) * B[i]))
    elif i % totalfactors == 0 and i < totalconsumers * totalfactors:
        weighted_utility_subf = np.append(weighted_utility_subf,(tweighted_utility_subf[i:i + totalfactors]) * B[i / totalfactors])

utility_subf = np.array([])

for i in range(len(weighted_utility_subf)):
    if i == 0:
        utility_subf = np.append(utility_subf,(np.sum(weighted_utility_subf[i:i + totalfactors])))
    elif i % totalfactors == 0 and i < totalconsumers * totalfactors:
        utility_subf = np.append(utility_subf,(np.sum(weighted_utility_subf[i:i + totalfactors])))

utility_list = np.array([])
utility_list = np.round((utility_subc - utility_subf) , 2)
print "The utility list is:",utility_list

"""Obtain the welfare maximisation function"""
"""Welfare maximisation function used here is (sum of (utility^2)^utilityweights)^overall_weight"""
"""Obtain overall weight for the welfare maximisation function"""
overall_weight = 1 / (random.random())
print "The overall weight attached to the welfare maximisation function is:",overall_weight
"""Make the utilities positive"""
utility_list_square = utility_list ** 2
welfare_max = (np.sum(np.power(utility_list_square , utilityweights))) ** overall_weight
print "The welfare maximisation function is:",welfare_max



