def palindromeRearranging(inputString):

    return sum([inputString.count(c)%2 == 1 for c in set(inputString)]) < 2