def sudoku(grid):
    cols = list(zip(*grid))
    boxes = [[grid[x+i][y+j] for i in range(3) for j in range(3)] for x in [0,3,6] for y in [0,3,6]]
    return all([c.count(i)==1 for x in [grid,cols,boxes] for c in x for i in c])