def avoidObstacles(inputArray):
    jump = 2
    m = max(inputArray)+1
    while True:
        valid = True
        for i in range(0, m+1, jump):
            if i in inputArray:
                valid = False
                break
        if valid:
            return jump
        jump += 1