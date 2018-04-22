def depositProfit(deposit, rate, threshold):

    years = 0
    while deposit < threshold:
        years += 1
        deposit *= 1 + rate/100
    return years