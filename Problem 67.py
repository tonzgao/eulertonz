
# coding: utf-8

# In[5]:

def process(f):
    f = open(f, 'r')
    lines = f.readlines()
    rows = []
    for i in range(len(lines)):
        rows.append([])
    for j in range(len(lines)):
        for i in range(j+1):
            num = lines[j][i*3:i*3+2]
            if num[0] is '0':
                num = num[1:]
            rows[j].append(int(num))
    f.close()
    return rows, j

rows, size = process("triangle.txt")
len(rows[size])


# In[6]:

from functools import wraps

def memo(func):
    cache = {}
    @wraps(func)
    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrap


# In[7]:

@memo
def max_path(a, b, size):
    if a == size:
        return rows[a][b]
    else:
        for e in rows[a]:
            return max(rows[a][b] + max_path(a+1, b, size), rows[a][b] + max_path(a+1, b+1, size))
print max_path(0, 0, size)


# In[ ]:



