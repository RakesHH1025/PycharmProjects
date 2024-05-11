n=5
for i in range(1,n+1):     #i= 1        2       3           4           5
    for j in range(1,i):    #j=0        1     1,2       1,2,3     1,2,3,4
        print(" ",end=" ")
    for k in range(1,n+2-i):    #k= 1,2,3,4,5   1,2,3,4     1,2,3   1,2,    1
        print("*",end=" ")
    print()
