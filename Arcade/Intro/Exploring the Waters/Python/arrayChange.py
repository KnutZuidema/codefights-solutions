def arrayChange(inputArray):
    steps = 0
    min = inputArray[0]+1
    for i in range(1,len(inputArray)):
        if inputArray[i] < min:
            steps += abs(min - inputArray[i])
            inputArray[i] += abs(min - inputArray[i])
        min = inputArray[i]+1
    return steps