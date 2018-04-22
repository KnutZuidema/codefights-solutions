def sortByHeight(a):

    tree_index = [i for i in range(len(a)) if a[i] == -1]
    people = sorted([x for x in a if x != -1])
    print(people)
    out = [0 for _ in range(len(a))]
    for i in tree_index:
        out[i] = -1
    y = 0
    for i in range(len(out)):
        if out[i] == 0:
            out[i] = people[y]
            y += 1
    return out