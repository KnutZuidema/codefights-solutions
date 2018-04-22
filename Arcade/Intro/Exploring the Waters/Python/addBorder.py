def addBorder(picture):

    return ['*'*(len(picture[0]) + 2)] + ['*'+x+'*' for x in picture] + ['*'*(len(picture[0]) + 2)]