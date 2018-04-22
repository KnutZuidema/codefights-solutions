def bishopAndPawn(bishop, pawn):
    return (abs((ord(bishop[0])-ord('a'))-(ord(pawn[0])-ord('a'))) ==
            abs(int(bishop[1])-int(pawn[1])))