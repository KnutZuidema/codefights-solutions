def isMAC48Address(input):
    return True if re.match(r'([0-9A-F]{2}-){5}[0-9A-F]{2}$', input) else False