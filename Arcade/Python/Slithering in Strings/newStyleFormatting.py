def newStyleFormatting(s):
    def repl(x):
        if x.group() == '%%': return '%'
        if x.group()[1].isalpha(): return '{}'
        return x.group()
    return re.sub(r'%.', repl, s)