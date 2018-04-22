def chessBoardCellColor(cell1, cell2):

    cell1_color = (ord(cell1[0])-ord('A')+1 + int(cell1[1])) % 2
    cell2_color = (ord(cell2[0])-ord('A')+1 + int(cell2[1])) % 2
    print(cell1_color, cell2_color)
    return cell1_color == cell2_color