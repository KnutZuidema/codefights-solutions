import re
def isIPv4Address(inputString):

    if re.match(r'((\d|1?\d\d|2[0-4]\d|25[0-5])\.){3}(\d|1?\d\d|2[0-4]\d|25[0-5])$', inputString):
        return True
    return False