def sudoku2(grid):
    return (sum([row.count(c)>1
                 for row in grid
                 for c in row if c != '.']) +
            sum([col.count(c)>1
                 for col in list(zip(*grid))
                 for c in col if c != '.']) +
            sum([block.count(c)>1
                 for block in [grid[i][j:j+3]+grid[i+1][j:j+3]+grid[i+2][j:j+3]
                               for i in range(0,9,3)
                               for j in range(0,9,3)]
                 for c in block if c != '.']))\
            == 0