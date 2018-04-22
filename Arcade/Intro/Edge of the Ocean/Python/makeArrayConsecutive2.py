def makeArrayConsecutive2(statues):
    extra = 0
    for i in range (min(statues)+1, max(statues)):
        if i not in statues:
            extra += 1
    return extra