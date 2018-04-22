def evenDigitsOnly(n):

    return sum([int(c)%2 == 1 for c in str(n)]) == 0