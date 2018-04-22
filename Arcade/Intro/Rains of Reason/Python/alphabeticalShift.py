def alphabeticShift(inputString):

    return ''.join(chr(ord('a') + (ord(c)-ord('a')+1)%26) for c in inputString)