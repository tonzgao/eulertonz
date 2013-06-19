import time

def av(list):
    return sum(list)/float(len(list))

def timeit(fn, *args):
    t1 = time.clock()
    output = fn(*args)
    t2 = time.clock()
    return t2-t1, output

def timetest(fn, n, *args):
    if isinstance(n, int):
        times = [timeit(fn, *args)[0] for i in range(n)]
    else:
        times = []
        while sum(times) < n:
            times.append(timeit(fn, *args)[0])
    return min(times), av(times), max(times)
