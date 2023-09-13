# Emma's code

import math
# Delete the import statement if needed - it only is used in the optional comment block at the end


def factorial(x):
    if x:
        return x * factorial(x - 1)
    return 1


def grid_filler(n):
    if n <= 1:  # Change this 1 to a 0 to make this program count all solutions that do NOT work
        return 0  # No solutions on a 1x1 grid!
    else:
        return (factorial(n-1) + -1 * (factorial(n) * grid_filler(n-1))) / factorial(n-1)
    # Since the output of this function already flips from + to - to + etc., you don't have to include the -1^n


print(int(abs(grid_filler(int(input("Please input n: "))))))

# The block below provides some interesting insight into how the ratio of total combinations to solutions approaches e

for i in range(50):
    f = i + 2 
    solutions = int(abs(grid_filler(int(f))))
    print(factorial(f)/solutions, solutions, f, sep='-')

print(math.e)
