def boxBlur(image):
    out = [[0 for x in range(len(image[0])-2)] for y in range(len(image)-2)]
    for y in range(1, len(image)-1):
        for x in range(1, len(image[0])-1):
            new_pixel = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    new_pixel += image[y+i][x+j]
            out[y-1][x-1] = new_pixel//9
    return out
            