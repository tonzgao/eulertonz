def palindromes(nums):
    palindromes = []
    flag = 0
    for e in nums:
        for f in range(0, len(str(e))/2):
            item = str(e)
            if item[f] != item[-1 - f]:
                flag = 1
                break
        if flag == 0:
            palindromes.append(e)
        else:
            flag = 0
    return palindromes

def products():
    products = set()
    for e in range(100, 1000):
        for f in range(e, 1000):
            products.add(e*f)
    return list(products)

def prob4():
    return max(palindromes(products()))

print prob4()