"""
Created on Thu May 24 15:19:31 2018
@author: WeiJin
"""

# Import tools
import numpy as np
# Import modules
from __init__ import Economy


# Obtain the average welfare value of 100 iterations of optimization for the 2 scenarios below
# Create arrays to store the welfare value from each iteration for the 2 scenarios below
welfare_list1 = np.array([])
welfare_list2 = np.array([])

# Create an instance of the Economy class with externality,but no tax
E1 = Economy(3,3,3,e1=True)
# Create an instance of the Economy class with externality and with tax
E2 = Economy(3,3,3,e1=True)
# Iterate maximization 100 times
i = 0
while i < 100:
    # Maximization procedure
    eqb = E1.Equilibrium()
    # Obtain maximization value
    value = eqb.fun
    # Skip an iteration if it returns an invalid value
    if np.isnan(value):
        next
    else:
        welfare_list1 = np.append(welfare_list1,value)
    i += 1
i = 0
while i < 100:
    # Maximization procedure
    eqb = E2.Equilibrium()
    # Obtain maximization value
    value = eqb.fun
    # Skip an iteration if it returns an invalid value
    if np.isnan(value):
        next
    else:
        welfare_list2 = np.append(welfare_list2,value)
    i += 1
# Obtain the average welfare from the 100 iterations using the welfare_list
res_avg1 = np.mean(welfare_list1) * -1
res_avg2 = np.mean(welfare_list2) * -1
print "The average level of welfare with externality %s" %(res_avg1)
print "The average level of welfare with externality and 0.2 tax rate is %s" %(res_avg2)