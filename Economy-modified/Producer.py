"""
Created on Mon Apr 02 16:34:45 2018
@author: WeiJin,PoHan
"""

# Import tools
import numpy as np
# Import modules
from function import Loop
from function import Nested_Loop_P
from function import Total
from function import Loop_Slice_Ex
from function import Loop_P
from functools import reduce

# Create a class called Producer to simulate the production of different goods in the economy
class Producer(object):
   def __init__(self,c,g,f,e1):
       # c: Number of consumers in the economy
       # g: Number of goods produced in the economy
       # f: Number of factors used in the production
       # e1: Degree of production externality(could be either positive or negative real numbers)
       self.c = c
       self.g = g
       self.f = f
       self.e1 = 0.1
       
   def Production(self,output_list):
       # Setting up the calculation of total production
       # Calculate the lengths of different segments in the output list
       consumption_length = self.c * self.g
       factor_ss_length = self.c * self.f
       consumer_length = consumption_length + factor_ss_length
       # Define f_list as the last segment of the output_list that contains quantity demanded of each factor
       f_list = np.array(output_list[consumer_length:consumer_length + self.g * self.f])
       
       # Generate production parameters
       alpha = []
       for i in range(self.g*self.f):
           if (i+1) % self.f == 0 and i < self.g*self.f:
               alpha = np.append(alpha,0.1)
           else:
               alpha = np.append(alpha,0.2)
               
       #Adding up the amount of last factor(the factor that produces aggregate externality)
       acum = np.sum(f_list[self.f-1::self.f])      
       '''
       Calculate the production of each good
       '''
       total_prod = np.array([])
       output = 0
       for i in range(len(f_list)):
           if i == 0 or (i % self.f == 0 and i < self.g*self.f):
               output = reduce(lambda x, y: x*y, np.power(f_list[i:i+self.f],alpha[i:i+self.f]))
               total_prod = np.append(total_prod,output * acum**self.e1)
       return total_prod
   def Production_Ind(self,output_list):
      '''
      The production function for social planner who can not observe the aggregate externality
      '''
      # Setting up the calculation of total production
      # Calculate the lengths of different segments in the output list
      consumption_length = self.c * self.g
      factor_ss_length = self.c * self.f
      consumer_length = consumption_length + factor_ss_length
      # Define f_list as the last segment of the output_list that contains quantity demanded of each factor
      f_list = np.array(output_list[consumer_length:consumer_length + self.g * self.f])
       
      # Generate production parameters
      alpha = []
      for i in range(self.g*self.f):
          if (i+1) % self.f == 0 and i < self.g*self.f:
              alpha = np.append(alpha,0.1)
          else:
              alpha = np.append(alpha,0.2)
                   
      '''
      Calculate the production of each good
      '''
      total_prod = np.array([])
      output = 0
      for i in range(len(f_list)):
          if i == 0 or (i % self.f == 0 and i < self.g*self.f):
              output = reduce(lambda x, y: x*y, np.power(f_list[i:i+self.f],alpha[i:i+self.f]))
              total_prod = np.append(total_prod,output * f_list[i + self.f -1]**self.e1)
      return total_prod
        