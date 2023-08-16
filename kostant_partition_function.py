# kostant_partition_function.py
#
# goal: compute values for Kostant partition function
#
# input: n: length, S: multiset of type A_(n-1) roots, a: length n integer vector
# output: nonnegative integer (representing the number of nonnegative integer linear combinations of S_G that equate to a)

# from multiset import * # this package may not be necessary
import numpy as np

# target vector
a = np.array([2,-1,-1,0])
print('target vector:', a)

# multiset of type A_n roots based on the edge set of G
# for now, enter this manually
e1 = np.array([1,-1,0,0])
e2 = np.array([1,-1,0,0])
e3 = np.array([1,0,-1,0])
e4 = np.array([0,1,-1,0])
e5 = np.array([0,1,0,-1])
e6 = np.array([0,0,1,-1])
e7 = np.array([0,0,1,-1])

# put edge set into a list/tuple to make loopable
l = [e1,e2,e3,e4,e5,e6,e7]
t = (e1,e2,e3,e4,e5,e6,e7)
print('multiset of roots:')
for i in range(7):
  print(l[i])
#  print(t[i])

# set upper bound for nonnegative integer coefficients
# for now, this can be set via observation
u = 2

# computing nonnegative integer linear combinations 
# for now, run some for loops and then count matches afterwords

# count matches 

# print matches?
