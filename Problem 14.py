
# coding: utf-8

# https://projecteuler.net/problem=14
# 
# The following iterative sequence is defined for the set of positive integers:
# 
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
# 
# Using the rule above and starting with 13, we generate the following sequence:
# 
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
# 
# Which starting number, under one million, produces the longest chain?
# 
# NOTE: Once the chain starts the terms are allowed to go above one million.

# In[7]:

def collatz(n):
    if n is 1:
        return n
    elif n%2 is 0:
        return n/2
    elif n%2 is 1:
        return 3*n + 1
    return 0


# In[8]:

print collatz(13), collatz(40), collatz(0), collatz(1)


# In[42]:

numbers = {1:1}
numbers[1]


# In[45]:

def len_collatz(n):
    if numbers.has_key(n) is True:
        return numbers[n]
    else:
        numbers[n] = len_collatz(collatz(n)) + 1
        return numbers[n]


# In[46]:

print len_collatz(13), len_collatz(40)
print numbers


# In[70]:

def longest_collatz(ceil):
    sizes = {1:[1]}
    for i in range(ceil-1, 0, -1):
        size = len_collatz(i)
        if sizes.has_key(size) is True:
            sizes[size].append(i)
        else:
            sizes[size] = [i]
    return sizes[max(sizes)], max(sizes)  


# In[74]:

longest_collatz(1000000)


# In[ ]:



