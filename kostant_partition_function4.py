# kostant_partition_function4.py
#
# goal: compute values for Kostant partition function
#
# for n=4, 
# input: a multiset S_G of type A_4 roots, a list of length 5 integer vector targets (netflows)
# output: nonnegative integer (representing the number of nonnegative integer linear combinations of S_G that equate to a)

# from multiset import * # this package may not be necessary
import numpy as np

# multiset of type A_n roots based on the edge set of G
# for now, enter this manually
e0 = np.array([1,-1,0,0,0])
e1 = np.array([1,-1,0,0,0])
e2 = np.array([1,0,0,-1,0])
e3 = np.array([0,1,-1,0,0])
e4 = np.array([0,1,-1,0,0])
e5 = np.array([0,0,1,-1,0])
e6 = np.array([0,0,1,0,-1])
e7 = np.array([0,0,0,1,-1])
e8 = np.array([0,0,0,1,-1])

# put edge set into a list to make loopable
l = [e0,e1,e2,e3,e4,e5,e6,e7,e8]
print('multiset of roots:')
for i in range(9):
  print(l[i])

# target vector(s) aka netflows
# for now, enter these manually
# hopefully i'll get the composition generator program working evenutally
targets = [np.array([3,-1,-1,-1,0]), np.array([2,0,-1,-1,0]), np.array([1,1,-1,-1,0]), np.array([0,2,-1,-1,0]), np.array([2,-1,0,-1,0]), np.array([1,0,0,-1,0]), np.array([0,1,0,-1,0]), np.array([1,-1,1,-1,0]), np.array([0,0,1,-1,0]), np.array([2,-1,-1,0,0]), np.array([1,0,-1,0,0]), np.array([0,1,-1,0,0]), np.array([1,-1,0,0,0]) ]

for a in targets:
  # print('target vector:', a) 
  u = 3 # upper bound for nonnegative integer coefficients | for now, set via observation (won't the largest entry in the target vector suffice?)
  # print('largest allowed coefficient:', u)
  combo = np.array([0,0,0,0,0]) # stores the result of the nonnegative integer linear combination 
  match = 0 # counter for matches
  for i in range(u+1):
    for j in range(u+1):
      for k in range(u+1):
        for m in range(u+1):
          for n in range(u+1):
            for o in range(u+1):
              for p in range(u+1):
                for q in range(u+1):
                  for r in range(u+1):
                    combo = i*l[0]+j*l[1]+k*l[2]+m*l[3]+n*l[4]+o*l[5]+p*l[6]+q*l[7]+r*l[8]
                    if np.array_equal(combo,a) == True:
                      # print(i,j,k,m,n,o,p) # takes up a lot of space
                      match += 1
  print('K_G(', a, ') =', match)
