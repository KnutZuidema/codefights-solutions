def isTestSolvable(ids, k):
    digitSum = lambda x: sum([int(c) for c in str(x)])

    sm = 0
    for questionId in ids:
        sm += digitSum(questionId)
    return sm % k == 0
