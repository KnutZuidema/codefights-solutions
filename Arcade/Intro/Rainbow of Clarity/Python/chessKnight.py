def chessKnight(cell):
    num = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8}
    x = num[cell[0]]
    y = int(cell[1])
    moves = 0
    for i in [-2,2]:
        for j in [-1,1]:
            if 0<(x+i)<9 and 0<(y+j)<9:
                moves += 1
            if 0<(y+i)<9 and 0<(x+j)<9:
                moves += 1
    return moves