#row = 1
#while row <= 9:
   # col = 1
   # while col <= row:
       #print('%d*%d=%d'%(col,row,col*row),end='\t')
       #col += 1
   # print('')
   # row += 1
row = 1
for row in range(1,10):
    col = 1
    for col in range(1,row+1):
        print('%d*%d=%d'%(col,row,row*col),end='\t')
        col += 1
    print('')
    row += 1
