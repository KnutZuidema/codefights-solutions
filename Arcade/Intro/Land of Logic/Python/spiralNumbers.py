def spiralNumbers(n):
    LEFT, RIGHT, UP, DOWN = 0, 1, 2, 3
    max_x, min_x, max_y, min_y = n-1, 1, n-1, 0
    x, y = 0, 0
    toggle = RIGHT
    spiral = [[0 for i in range(n)] for j in range(n)]
    for num in range(n*n):
        spiral[x][y] = num+1
        if toggle == RIGHT:
            y += 1
            if y == max_y:
                max_y -= 1
                toggle = DOWN
        elif toggle == LEFT:
            y -= 1
            if y == min_y:
                min_y += 1
                toggle = UP
        elif toggle == DOWN:
            x += 1
            if x == max_x:
                max_x -= 1
                toggle = LEFT
        elif toggle == UP:
            x -= 1
            if x == min_x:
                min_x += 1
                toggle = RIGHT
    return spiral