def commonCharacterCount(s1, s2):
    out = 0
    for c in set(s1):
        out += min(s1.count(c), s2.count(c))
    return out