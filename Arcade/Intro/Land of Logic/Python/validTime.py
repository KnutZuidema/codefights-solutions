def validTime(time):
    return True if re.match(r'([0-1][0-9]|2[0-3]):[0-5][0-9]$', time) else False