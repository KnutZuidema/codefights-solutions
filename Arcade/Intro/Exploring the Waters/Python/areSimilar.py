def areSimilar(a, b):

    if a == b:
        return True
    for i in range(len(a)):
        if a[i] == b[i]:
            continue
        for j in range(len(a)):
            if i != j:
                a[i], a[j] = a[j], a[i]
                if a == b:
                    return True
                a[i], a[j] = a[j], a[i]
    return False