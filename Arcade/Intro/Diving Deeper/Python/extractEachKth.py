def extractEachKth(input, k):

    return [input[i] for i in range(len(input)) if (i+1)%k != 0]