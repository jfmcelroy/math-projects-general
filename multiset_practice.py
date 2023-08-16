# #multiset_practice.py
#
# practicing the multiset package
from multiset import *
 
# print empty multiset
print(Multiset())
 
# print multiset from iterable
print(Multiset('abcde'))
 
# print multiset from mapping
print(Multiset({(1,-1,0,0): 2, {(1,0,0,-1): 1, (0,1,-1,0): 2, (0,0,1,-1): 2}))
