"""Created on Sat Mar 17 16:09:42 2018"""

"""@author: WeiJin"""


import math
import numpy as np

"""Define an economy consisting of H individual consumers and consolidate them in a list"""
consumer_list = np.array([])

"""Define the consumption bundle of an individual consumer"""
consumption_bundle = np.array([])

"""Define the factor bundle of an individual consumer"""
factor_bundle = np.array([])

"""Define the consumption quantities of each good in an individual consumer's consumption bundle"""
cbundle_qty = np.array([2,5,10])

"""Define the factor input quantities of each factor of an individual consumer"""
fbundle_qty = np.array([3,8,2])

"""Define utility function parameters"""
a = np.array([2,4,1])
b = 4
y = 0.8
s = 0.2
t = np.array([0.1,0.4,0.9])

"""Define utility function, combining the consumption part and the factor part"""
utility_subc = (np.dot((cbundle_qty ** y) , a)) ** ((1 - s) / y)
utility_subf = np.dot((np.power(fbundle_qty , (t + 1))) , (b / (t + 1)))
utility = utility_subc - utility_subf
print utility

