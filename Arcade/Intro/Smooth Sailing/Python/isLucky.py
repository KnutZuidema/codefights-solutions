def isLucky(n):
    first = [int(x) for x in str(n)[:len(str(n))//2]]
    second = [int(x) for x in str(n)[len(str(n))//2:]]
    return sum(first) == sum(second)