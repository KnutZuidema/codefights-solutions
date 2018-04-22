def isBeautifulString(input):
    prev = input.count('a')
    for i in range(1, 26):
        curr = input.count(chr(ord('a')+i))
        if curr > prev: return False
        prev = curr
    return True