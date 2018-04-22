def fileNaming(names):
    used = {}
    for i in range(len(names)):
        if names[i] in used:
            used[names[i]] += 1
            while names[i] + '(' + str(used[names[i]]) + ')' in used:
                used[names[i]] += 1
            names[i] = names[i] + '(' + str(used[names[i]]) + ')'
            used[names[i]] = 0
        else:
            used[names[i]] = 0
    return names