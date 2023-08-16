# #multiset_practice.py
#
# practicing the multiset package
from multiset import *
import numpy as np
 
# print empty multiset
# print(Multiset())
 
# print multiset from iterable
# print(Multiset('abcde'))
 
# print multiset from mapping
# print(Multiset({(1,-1,0,0): 2, (1,0,0,-1): 1, (0,1,-1,0): 2, (0,0,1,-1): 2}))

# vector algebra
e1 = np.array([1,0,0,0])
e2 = np.array([0,1,0,0])
e3 = np.array([0,0,1,0])
e4 = np.array([0,0,0,1])
print(e1,e2,e3,e4)
