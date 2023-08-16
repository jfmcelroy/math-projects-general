# kostant_partition_function.py
#
# goal: compute values for kostant partition function
#
# input: n: length, S: multiset of type A_(n-1) roots, a: length n integer vector
# output: nonnegative integer (representing the number of nonnegative integer linear combinations of S_G that equate to a)

# from multiset import * # this package may not be necessary
import numpy as np

# '''Compute the Kostant partition function K_G(a) for a multiset S of type A_{n-1} roots'''

# Edge set of type A_n roots
# for now, enter this manually
e1 = np.array([1,-1,0,0])
e2 = np.array([1,-1,0,0])
e3 = np.array([1,0,0,-1])
e4 = np.array([0,1,-1,0])
e5 = np.array([0,1,-1,0])
e6 = np.array([0,0,1,-1])
e7 = np.array([0,0,1,-1])

# put edge set into a list to make loopable
t = [e1,e2,e3,e4,e5,e6,e7]
print(t)

# Computing nonnegative integer linear combinations 
for i in range(2):
  print(i*e1)
  print(i*e2)
  print(i*e3)
  print(i*e4)
  print(i*e5)
  print(i*e6)
  print(i*e7)
