
# coding: utf-8

# In[119]:

import string 

def process(link):
    f = open(link, 'r')
    names = string.split(f.readline(), "\"")[1::2]
    scores = [map(lambda x: ord(x)-64, name) for name in names]
    return scores, names


# In[128]:

def problem_22(scores):
    scores.sort()
    return sum([(c+1) * sum(scores[c]) for c in range(len(scores))])


# In[129]:

problem_22(process('names.txt')[0])


# In[ ]:



