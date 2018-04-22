import re
def reverseParentheses(s):

    while re.search(r'\([^\(\)]*\)', s):
        s = re.sub(r'\([^\(\)]*\)', lambda x: x.group().replace('(', '').replace(')', '')[::-1], s)
    return s