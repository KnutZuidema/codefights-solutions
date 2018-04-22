def digitsProduct(product):
    if product == 0:
        return 10
    for i in range(math.factorial(9)):
        r = 1
        for j in str(i):
            r *= int(j)
        if r == product:
            return i
    return -1