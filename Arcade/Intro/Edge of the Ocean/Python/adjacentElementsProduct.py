def adjacentElementsProduct(inputArray):

    res = inputArray[0] * inputArray[1]
    for i in range(1, len(inputArray)-1):
        res = max(inputArray[i] * inputArray[i+1], res)
    return res
            