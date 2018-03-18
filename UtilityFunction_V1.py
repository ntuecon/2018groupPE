"""Created on Sat Mar 17 16:09:42 2018"""

"""@author: WeiJin, PoHan"""


import math
import numpy as np

"""def CES utility function"""
def CESuf(c,f,a,b,s,t):
  """get all the attributes needed to compute utility"""
  y = np.array(0.8)
  """Define the consumption bundle of an individual consumer"""
  c  = np.array(c)
   """Define the factor bundle of an individual consumer"""
  f = np.array(f)
  """Define the weighting parameters for conumption"""
  a = np.array(a)
  """Define the parameter that represents how the consumer's aversion to supply factors"""
  b = np.array(b)
  """Define the elasticity parameters for consumption"""
  s = np.array(s)
  """Define the elasticity parameters for factors"""
  t = np.array(t)
  """Define utility function, combining the consumption part and the factor part"""
  utility_subc = (np.dot((c ** y) , a)) ** ((1 - s) / y)
  utility_subf = np.dot((np.power(f , (t + 1))) , (b / (t + 1)))
  utility = utility_subc - utility_subf
  return utility

"""Get the attributes of the CES utility function"""
c = input("Please enter the conumption bundel(a list of goods):")
f = input("Please enter the factors supplied(a list of factors):")
a = input("Please enter the weighting parameters for consumption goods(Notice that the length of this list should be the same as the length of consumption bundle):")
b = input("How do you think the consumer hates to work?(larger number means less willing to work):")
s = input("Please enter the elasticity parameter for consumption(a number):")
t = input("Please enter the elasticity parameters for factors(notice that the length of this list should be the same as the length of factor list):")

print CESuf(c,f,a,b,s,t)

  """Define utility function, combining the consumption part and the factor part"""
  utility_subc = (np.dot((cbundle_qty ** y) , a)) ** ((1 - s) / y)
  utility_subf = np.dot((np.power(fbundle_qty , (t + 1))) , (b / (t + 1)))
  utility = utility_subc - utility_subf
  return utility


"""An example"""

c =[2,5,10]
f= [3,8,2]
a = [2,4,1]
b = 4
s = 0.2
t = [0.1,0.4,0.9]
print CESuf(c,f,a,b,s,t)

