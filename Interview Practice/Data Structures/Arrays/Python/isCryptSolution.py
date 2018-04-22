def isCryptSolution(crypt, solution):
    solution = dict(zip(*list(zip(*solution))))
    if (solution[crypt[0][0]] != '0' or len(crypt[0]) == 1) and (solution[crypt[1][0]] != '0' or len(crypt[1]) == 1) and (solution[crypt[2][0]] != '0' or len(crypt[2]) == 1):
        for i in range(len(crypt)):
            crypt[i] = ''.join([solution[c] for c in crypt[i]])
        return int(crypt[0]) + int(crypt[1]) == int(crypt[2])
    return False