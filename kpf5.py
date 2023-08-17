# kpf5.py
#
# goal: compute values for Kostant partition function
#
# for n=5, 
# input: a multiset S_G of type A_5 roots, a list of length 6 integer vector targets (netflows)
# output: nonnegative integer (representing the number of nonnegative integer linear combinations of S_G that equate to a)

# from multiset import * # this package may not be necessary
import numpy as np

# multiset of type A_n roots based on the edge set of G
# for now, enter this manually
e0 = np.array([1,-1,0,0,0,0])
e1 = np.array([1,-1,0,0,0,0])
e2 = np.array([1,0,0,0,0,-1])
e3 = np.array([0,1,-1,0,0,0])
e4 = np.array([0,1,-1,0,0,0])
e5 = np.array([0,0,1,-1,0,0])
e6 = np.array([0,0,1,-1,0,0])
e7 = np.array([0,0,0,1,-1,0])
e8 = np.array([0,0,0,1,-1,0])
e9 = np.array([0,0,0,0,1,-1])
e10 = np.array([0,0,0,0,1,-1])

# put edge set into a list to make loopable
l = [e0,e1,e2,e3,e4,e5,e6,e7,e8,e9,e10]
print('multiset of roots:')
for i in range(11):
  print(l[i])

# target vector(s) aka netflows
# for now, enter these manually
# hopefully i'll get the composition generator program working evenutally
targets = [np.array([0,0,0,0,0,0]) ]

for a in targets:
  # print('target vector:', a) 
  u = 4 # upper bound for nonnegative integer coefficients | for now, set via observation (won't the largest entry in the target vector suffice?)
  # print('largest allowed coefficient:', u)
  combo = np.array([0,0,0,0,0,0]) # stores the result of the nonnegative integer linear combination 
  match = 0 # counter for matches
  for j0 in range(u+1):
    if j0*l[0][0]+j1*l[1][0] <= a[0]:
      for j1 in range(u+1):
        if j0*l[0][0] <= a[0]:
          for j2 in range(u+1):
            for j3 in range(u+1):
              for j4 in range(u+1):
                for j5 in range(u+1):
                  for j6 in range(u+1):
                    for j7 in range(u+1):
                      for j8 in range(u+1):
                        for j9 in range(u+1):
                          for j10 in range(u+1): 
                            combo = j0*l[0]+j1*l[1]+j2*l[2]+j3*l[3]+j4*l[4]+j5*l[5]+j6*l[6]+j7*l[7]+j8*l[8]+j9*l[9]+j10*l[10]
                            if np.array_equal(combo,a) == True:
                              # print(i,j,k,m,n,o,p) # takes up a lot of space
                              match += 1
  print('K_G(', a, ') =', match)
