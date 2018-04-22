def stringsRearrangement(input):
    endpoints = 0
    for a in set(input):
        neighbors = 0
        for b in input:
            if sum([1 for i in range(len(b)) if a[i] != b[i]]) == 1:
                neighbors += 1
        if neighbors < input.count(a): return False
        if neighbors == input.count(a):
            endpoints += 1
            if endpoints > 2: return False
    return True