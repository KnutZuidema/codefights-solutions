def arrayMaxConsecutiveSum(input, k):
    max_sum = sum(input[:k])
    window = max_sum
    for i in range(len(input)-k):
        window = window - input[i] + input[i+k]
        max_sum = max(max_sum, window)
    return max_sum