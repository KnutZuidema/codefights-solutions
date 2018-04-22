def lineEncoding(s):
    ss = []
    prev = 0
    for i in range(1, len(s)):
        if s[i-1] != s[i]:
            ss.append(s[prev:i])
            prev = i
    else:
        ss.append(s[prev:])
    print(ss)
    return ''.join([str(len(x))+x[0] if len(x)>1 else x[0] for x in ss])