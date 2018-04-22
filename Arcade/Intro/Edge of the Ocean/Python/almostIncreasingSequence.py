def almostIncreasingSequence(sequence):
    joker = True
    for i in range(1,len(sequence)):
        if sequence[i] <= sequence[i-1]:
            if not joker:
                return False
            joker = False
            
            if i == 1 or i == len(sequence)-1:
                continue
            elif sequence[i] > sequence[i-2]:
                sequence[i-1] = sequence[i-2]
            elif sequence[i+1] > sequence[i-1]:
                sequence[i] = sequence[i-1]
            else:
                return False
    return True