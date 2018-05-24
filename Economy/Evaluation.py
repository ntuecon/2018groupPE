"""
Created on Thu May 24 15:19:31 2018

@author: WeiJin
"""

# Import tools
import numpy as np
# Import modules
from __init__ import Economy


# Obtain the average welfare value of 30 iterations of optimization with externality, without tax
# Create an array to store the welfare value from each iteration
welfare_list = np.array([])
# Create an instance of the Economy class with externality but no tax
E0 = Economy(2,2,2,e1=True)
# Iterate maximization 30 times
i = 0
while i < 30:
    eqb = E0.Equilibrium()
    value = eqb.fun
    welfare_list = np.append(welfare_list,value)
    i += 1
# Obtain the average welfare from the 30 iterations using the welfare_list
res_avg = np.mean(welfare_list) * -1
print res_avg
# Obtain the average welfare value of 100 iterations of optimization with externality, with tax
# Create an instance of the Economy class with externality and tax
