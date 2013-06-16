# Basically the same as problem 16

import math

def sumchars(ca, cb):
    return int(ca) + int(cb)

def prob20():
    nums = str(math.factorial(100))
    return reduce(sumchars, nums)

print prob20()