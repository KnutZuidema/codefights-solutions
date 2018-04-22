def findEmailDomain(address):

    return re.sub(r'^.*@', '', address)