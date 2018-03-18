"""Created on Sun Mar 18 19:06:27 2018"""

"""@author: WeiJin"""


import math
import numpy as np

"""Continuation from UtilityFunction. Refer above for more definitions."""

"""Define factor inputs required to produce a particular good"""
factor_inputs = np.array([])

"""Define factor input quantities required to produce one unit of a particular good"""
factor_input_qty = np.array([10,20,2])

"""Define production function parameters"""
p = np.array([1,0.5,1.5])
x = 0.4

"""Define production function of a particular good"""
production = np.dot(((factor_input_qty ** (1 - x)) / (1 - x)) , p)
print production