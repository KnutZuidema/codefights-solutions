def allLongestStrings(inputArray):
    max_length = max(len(x) for x in inputArray)
    return [x for x in inputArray if len(x) == max_length]