# See Problem 7.txt for grid

def format(size):
    f = open('C:\Users\Tony\Documents\Programs\ProjectEuler\Problem 11.txt', 'r')
    unformatted = []
    grid = []
    v = 0
    flag = 0
    for line in f:
        unformatted.append(line)
        grid.append([])
        for c in unformatted[-1]:
            flag -= 1
            if c == '0' and v == 0:
                v = 0
                continue
            if c == ' ' or c == '\n':
                grid[-1].append(v)
                flag = 2
                v = 0
            else:
                v = v*10 + int(c)
            if len(grid) == size and len(grid[-1]) == size -1 and flag == 0:
                grid[-1].append(v)
    f.close()
    return grid

def expand(grid):
    updown = grid
    leftright = []
    x1 = []
    x2 = []

    for f in range(0, len(grid[0])):
        leftright.append([])
        x1.append([])
        x2.append([])
        x1.append([])
        x2.append([])
    x1.pop()
    x2.pop()

    for e in range(0, len(grid)):
        for f in range(0, len(grid[0])):
            leftright[e].append(updown[f][e])

    for e in range(0, len(grid)):
        for f in range(0, e+1):
            x2[e].append(grid[f][e-f])
    for e in range(1, len(grid)):
        for f in range(len(grid)-1, e-1, -1):
            x2[len(grid) -1 + e].append(grid[len(grid)-1 -f + e][f])
    #ANSWER BELOW
    #print x2[18][12:16]
    #Sequence is found by making an up to down, right to left diagonal cut from the second last number (91) on the first row

    for e in range(len(grid)-1, -1, -1):
        for f in range(0, len(grid) - e):
            x1[len(grid)-1-e].append(grid[f][e+f])
    for e in range(1, len(grid)):
        for f in range(0, len(grid)-e):
            x1[len(grid) -1 + e].append(grid[e+f][f])
    return [updown, leftright, x2, x1, "updown", "leftright", "x2", "x1"]

def multiply(a, b):
    return a*b

def highprod(grid, gridname):
    highest, coord = 0, (0, 0)
    for index in range(0, len(grid)):
        e = grid[index]
        if len(e) < 4:
            continue
        for n in range(0, len(e)-3):
            product = reduce(multiply, e[n:n+4])
            if product > highest:
                highest, coord = product, (index, n)
    return highest, coord, gridname

def prob11():
    grids = expand(format(20))
    results = [highprod(grids[n], grids[n+4]) for n in range(0, 4)]
    return max([list(results)[o][0] for o in range(0, 4)])

print prob11()