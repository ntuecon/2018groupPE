
"""
Created on Thu Mar 22 20:00:19 2018

@author: WeiJin, PoHan
"""

"""This CES production function was built according to Tresch, R. W. (2008). Public sector economics. Palgrave Macmillan."""



import math
import numpy as np

"""Continuation from UtilityFunction. Refer above for more definitions."""

def CESpf(f):
  """Obtain all the attributes needed to calculate the production level"""
  x = 0.4
  f = np.array(f)
  p = []
  for i in range(len(f)):
    p.append(1)
  """The production level given certain list of factors"""
  production = np.dot(((f ** (1 - x)) / (1 - x)) , p)
  return production
  
"""Enters the attributes"""
f = input("please enter the list of factors used to produced goods:")
print CESpf(f)

"""An example"""
f = [10,20,2]
print CESpf(f)
