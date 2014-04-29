
# coding: utf-8

# In[34]:

from functools import wraps

def memo(func):
    cache = {}
    @wraps(func)
    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrap

@memo
def fibo(n):
    if n < 3:
        return 1
    return fibo(n-1) + fibo(n-2)


# In[35]:

import itertools

count = itertools.count()
n = count.next()
while len(str(fibo(n))) < 1000:
    n = count.next()
print n, fibo(n)


# In[ ]:



