def digitDegree(n):
    out = 0
    while len(str(n)) > 1:
        n = sum([int(c) for c in str(n)])
        out += 1
    return out