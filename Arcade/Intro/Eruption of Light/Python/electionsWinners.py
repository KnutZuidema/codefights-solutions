def electionsWinners(votes, k):
    m = max(votes)
    mc = votes.count(m)
    return len([x for x in votes if x+k > m or (x == m and mc == 1)])