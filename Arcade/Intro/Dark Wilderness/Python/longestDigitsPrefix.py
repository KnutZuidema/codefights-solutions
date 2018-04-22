def longestDigitsPrefix(inputString):
    return re.match(r'\d*', inputString).group()