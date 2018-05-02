"""
Created on Mon Apr 02 16:34:45 2018
"""
"""
@author: WeiJin,PoHan
"""

import numpy as np
import random
from function import Loop
from function import Nested_Loop

"""
Define the production technoloy used by the economy
"""

class Producer(object):
   def __init__(self,c,g,f):
       self.c = c
       self.g = g
       self.f = f 
   def Production(self):
       """
       Setting up the calculation of total production
       """
       
       """
       Define variables that will be useful for list iterations
       """
       consumption_length = c * g
       factor_ss_length = c * f
       consumer_length = consumption_length + factor_ss_length
       f_list = np.array(output_list[consumer_length:consumer_length + g * f])
       """
       Generate parameters for the production function
       """
       X = Loop(g,2)
       P = Nested_Loop(g,f,2)
       
       """
       Calculate the total production
       """
       weighted_F_list = np.array([])
       weightedflist = np.array([])
       i = 0
       while i < g:
           j = 0
           while j < f:
               weightedflist = np.append(weightedflist,((f_list[(i * f) + j] ** (1 - X[i])) / (1 - X[i])) * P[(i * f) + j])
               j += 1
           weighted_F_list = np.append(weighted_F_list,weightedflist)
           weightedflist = np.array([])
           i += 1
       total_prod = np.array([])
       for i in range(len(weighted_F_list)):
           if (i == 0) or (i % f == 0 and i < f * g):
               total_prod = np.append(total_prod,round(np.sum(weighted_F_list[i:i + f]),0))
       return total_prod