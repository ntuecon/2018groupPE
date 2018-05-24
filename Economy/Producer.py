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


# Create a class called Producer to simulate the production of different goods in the economy
class Producer(object):
   def __init__(self,c,g,f,e1=False):
       # c: Number of consumers in the economy
       # g: Number of goods produced in the economy
       # f: Number of factors used in the production
       # e1: A good that uses a factor that creates a type of negative externality
       self.c = c
       self.g = g
       self.f = f
       self.e1 = e1
       
   def Production(self,output_list):
       # Setting up the calculation of total production
       # Calculate the lengths of different segments in the output list
       consumption_length = self.c * self.g
       factor_ss_length = self.c * self.f
       consumer_length = consumption_length + factor_ss_length
       # Define f_list as the last segment of the output_list that contains quantity demanded of each factor
       f_list = np.array(output_list[consumer_length:consumer_length + self.g * self.f])
       
       # Generate production parameters
       
       X = Loop(self.g)
       
       if self.e1 == False:
           # Production externality does not exist
           # Obtain production parameters
           P = Nested_Loop_P(self.g,self.f)
       else:
           # Production externality exists in the last factor
           # Calculate total quantity of last factor used
           total = Total(self.c,self.g,self.f)
           factor_dd = total.total_factor_dd(output_list)
           # Define tf as a function that is decreasing with total quantity of the last factor (externality) used, which has a range between 0 and 1
           # tf = 1 / (1 + x)
           tf = 1 / (10 * (1 + factor_dd[self.f - 1]))
           # Obtain production parameters
           p = Nested_Loop_P(self.g,self.f)
           # Due to the externality, the efficiency of the last factor for all goods are reduced
           P = Loop_Slice_Ex(p,self.f,self.g,tf)
           
       # Calculate total production quantity of each good
       # Define the intermediate variables weighted_F_list and weightedflist as arrays containing the un-summed elements of the production of each good
       weighted_F_list = np.array([])
       weightedflist = np.array([])
       
       # Calculate the tax function when there is an externality
       # Define f_ex_list as an array containing the quantity of the last factor used for each good
       f_ex_list = np.array([])
       i = 1
       while i <= len(f_list):
           if i % self.f == 0:
               # Extract the quantity of last factor used in each good
               f_ex_list = np.append(f_ex_list,f_list[i - 1])
           i += 1
       # Define tax as an array contaning the tax values on each good, based on quantity of last factor used
       tax = np.array([])
       tax = 1 / (1 + f_ex_list)
       
       # Construct the production function to obtain the weighted_F_list (un-summed elements of production)
       # Loop through the list to conduct mathematical operations on the elements according to the production function
       i = 0
       while i < self.g:
           j = 0
           while j < self.f:
               weightedflist = np.append(weightedflist,((f_list[(i * self.f) + j] ** (1 - X[i])) / (1 - X[i])) * P[(i * self.f) + j])
               j += 1
           weighted_F_list = np.append(weighted_F_list,weightedflist)
           weightedflist = np.array([])
           i += 1
       # Define total_prod as an array containing the total production quantity of each good
       total_prod = np.array([])
       # Obtain total production if the externality exists
       if self.e1 == True:
           for i in range(len(weighted_F_list)):
               if (i == 0) or (i % self.f == 0 and i < self.f * self.g):
                   total_prod = np.append(total_prod,round(np.sum(weighted_F_list[i:i + self.f]),0))
           # Total production is taxed
           total_prod = total_prod * (1 - tax)
           return total_prod
       # Obtain total production if the externality does not exist
       else:
           for i in range(len(weighted_F_list)):
               if (i == 0) or (i % self.f == 0 and i < self.f * self.g):
                   total_prod = np.append(total_prod,round(np.sum(weighted_F_list[i:i + self.f]),0))
           return total_prod