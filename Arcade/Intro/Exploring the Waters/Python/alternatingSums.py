def alternatingSums(a):

    team1 = [a[x] for x in range(len(a)) if x%2 == 0]
    team2 = [a[x] for x in range(len(a)) if x%2 == 1]
    return [sum(team1), sum(team2)]