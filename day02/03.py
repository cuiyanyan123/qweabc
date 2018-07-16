row=9
i=2
while row>=1:
    col=9
    while row<=col:
        i=i-1
        print('%d * %d = %d'%(col,i,col*i),end="\t")
        col-=1

    print('')
    i=12-row
    row-=1

