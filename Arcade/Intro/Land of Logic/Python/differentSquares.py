def differentSquares(matrix):
    if len(matrix) < 2 or len(matrix[0]) < 2: return 0
    l = []
    for i in range(len(matrix)-1):
        for j in range(len(matrix[0])-1):
            x = [matrix[i][j:j+2],matrix[i+1][j:j+2]]
            if x not in l:
                l.append(x)
    return len(l)