def deleteDigit(n):
    n = str(n)
    m = int(n[:-1])
    for i in range(len(n)):
        m = max(m, int(n[:i]+n[i+1:]))
    return m