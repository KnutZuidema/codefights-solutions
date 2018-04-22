def matrixElementsSum(matrix):

    cols = list(zip(*matrix))
    print(cols)
    res = 0
    for col in cols:
        for x in col:
            if x == 0:
                break
            res += x
    return res