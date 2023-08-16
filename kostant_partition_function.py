# kostant_partition_function.py
#
# goal: compute values for kostant partition function
#
# input: n: length, S: multiset of type A_(n-1) roots, a: length n integer vector
# output: nonnegative integer (representing the number of nonnegative integer linear combinations of S_G that equate to a)

from multiset import *
import numpy as np

# '''Compute the Kostant partition function K_G(a) for a multiset S of type A_{n-1} roots'''

# Edge set
e1 = np.array([1,-1,0,0])
e2 = np.array([1,-1,0,0])
e3 = np.array([1,0,0,-1])
e4 = np.array([0,1,-1,0])
e5 = np.array([0,1,-1,0])
e6 = np.array([0,0,1,-1])
e7 = np.array([0,0,1,-1])

# Computing nonnegative integer linear combinations 
for i in range(6):
  print(i*e1)
  print(i*e2)
  print(i*e3)
  print(i*e4)
  print(i*e5)
  print(i*e6)
  print(i*e7)
