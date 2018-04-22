def buildPalindrome(st):
    if st == st[::-1]: return st
    for i in range(len(st)+1):
        s = st + st[i::-1]
        if s == s[::-1]:
            return s