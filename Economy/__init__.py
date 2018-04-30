"""
Created on Mon Apr 02 16:34:45 2018
"""
"""
@author: WeiJin,PoHan
"""

"""
Set up the basic environment for the economy
"""

import numpy as np
import random
import scipy
from Consumer import Consumer
from Producer import Producer

class Economy(object):
    """
    'c'=number of consumers in the economy
    'g'=number of goods produced in the economy
    'f'=number of factors used in the production
    """
    def __init__(self,c,g,f):
        self.c = c
        self.g = g
        slef.f = f
    """
    Calculate the equilibria base on the consumers' preferences and technology
    """
    def Equilibrium(self):
        
