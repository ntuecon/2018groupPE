"""
Created on Mon Apr 02 16:34:45 2018

@author: WeiJin,PoHan
"""

import numpy as np
import random
from function import Loop
from function import Nested_Loop_P
from function import Nested_Loop_Ex

"""
Define the production technoloy used by the economy
"""

class Producer(object):
   def __init__(self,c,g,f,e1=False):
       self.c = c
       self.g = g
       self.f = f
       self.e1 = e1
   def Production(self,output_list):
       """
       Setting up the calculation of total production
       """
       
       """
       Define variables that will be useful for list iterations
       """
       consumption_length = self.c * self.g
       factor_ss_length = self.c * self.f
       consumer_length = consumption_length + factor_ss_length
       f_list = np.array(output_list[consumer_length:consumer_length + self.g * self.f])
       """
       Generate parameters for the production function
       """
       X = Loop(self.g,2)
       if self.e1 == False:
           P = Nested_Loop_P(self.g,self.f,2)
       else:
           P = Nested_Loop_Ex(self.g,self.f,2)       
       """
       Calculate the total production
       """
       weighted_F_list = np.array([])
       weightedflist = np.array([])
       tax = (f_list[(self.f * self.g) - 1] ** 2) * 0.3
       i = 0
       while i < self.g:
           j = 0
           while j < self.f:
               weightedflist = np.append(weightedflist,((f_list[(i * self.f) + j] ** (1 - X[i])) / (1 - X[i])) * P[(i * self.f) + j])
               j += 1
           weighted_F_list = np.append(weighted_F_list,weightedflist)
           weightedflist = np.array([])
           i += 1
       total_prod = np.array([])
       if self.e1 == 1:
           for i in range(len(weighted_F_list)):
               if (i == 0) or (i % self.f == 0 and i < self.f * self.g):
                   total_prod = np.append(total_prod,round(np.sum(weighted_F_list[i:i + self.f]),0))
           total_prod[self.g - 1] = total_prod[self.g - 1] * (1 - tax)
           return total_prod
       else:
           for i in range(len(weighted_F_list)):
               if (i == 0) or (i % self.f == 0 and i < self.f * self.g):
                   total_prod = np.append(total_prod,round(np.sum(weighted_F_list[i:i + self.f]),0))
           return total_prod
   def ex(self,output_list):
       consumption_length = self.c * self.g
       factor_ss_length = self.c * self.f
       consumer_length = consumption_length + factor_ss_length
       f_list = np.array(output_list[consumer_length:consumer_length + self.g * self.f])
       if self.e1 == True:
           i = 0
           while i < self.f * self.g:
               if (i+1) % self.f == 1:
                   return f_list[i]
               i += 1
               