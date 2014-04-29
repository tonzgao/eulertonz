
# coding: utf-8

# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
# 
# http://projecteuler.net/project/images/p_015.gif
# 
# How many such routes are there through a 20×20 grid?

# In[26]:

from functools import wraps

def memo(func):
    cache = {}
    @wraps(func)
    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrap


# In[27]:

@memo
def find_routes(rows, cols, downs, rights):
    if downs > rows or rights > cols:
        return 0
    if (downs, rights) == (rows, cols):
        return 1
    return find_routes(rows, cols, downs+1, rights) + find_routes(rows, cols, downs, rights+1)


# In[31]:

find_routes(20, 20, 0, 0)


# In[ ]:



