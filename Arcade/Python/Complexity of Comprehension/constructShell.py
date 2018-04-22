def constructShell(n):
    return [[0 for _ in range(x+1)] for x in range(n)] + [[0 for _ in range(n-(x+1))] for x in range(n-1)]