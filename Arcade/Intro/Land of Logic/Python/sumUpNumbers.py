def sumUpNumbers(input):
    return sum([int(x) for x in re.split(r'[^\d]', input) if x])