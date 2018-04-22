def minesweeper(matrix):
    out = []
    for y in range(len(matrix)):
        r = []
        for x in range(len(matrix[0])):
            count = 0
            for i in range(-1,2):
                for j in range(-1,2):
                    if (y+i >= 0 and y+i < len(matrix) and
                        x+j >= 0 and x+j < len(matrix[0]) and
                        (i != 0 or j != 0)):
                        if matrix[y+i][x+j]:
                            count += 1
            r.append(count)
        out.append(r)
    return out