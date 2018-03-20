"""Created on Sun Mar 18 19:06:27 2018"""
"""This CES production function was built according to Tresch, R. W. (2008). Public sector economics. Palgrave Macmillan."""

"""@author: WeiJin, PoHan"""


import math
import numpy as np

"""Continuation from UtilityFunction. Refer above for more definitions."""

def CESpf(f,p):
  """Obtain all the attributes needed to calculate the production level"""
  x = 0.4
  f = np.array(f)
  p = np.arrary(p)
  """The production level given certain list of factors"""
  production = np.dot(((f ** (1 - x)) / (1 - x)) , p)
  retrun production
  
"""Enters the attributes"""
f = input("please enter the list of foactors used to produced goods:")
p = input("Please enter the list of weighting parameters for all the factors(the length of this list should be the same as the length of the factors):")
print CESpf(f,p)

"""An example"""
f = [10,20,2]
p = [1,0.5,1.5]
print CESpf(f,p)
