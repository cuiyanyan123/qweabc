row = 9
while row >= 1:
    col = 9
    while row <= col:
        print('%d*%d=%d'%(col,row,row*col),end = '\t')
        col -= 1
    print('')
    

    row -= 1
