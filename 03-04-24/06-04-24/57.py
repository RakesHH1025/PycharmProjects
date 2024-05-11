n=5

for i in range(1,n+1):     #  i= 1            2       3       4       5
    for i in range(1,n+2-i): # j=1,2,3,4,5   1,2,3,4   1,2,3   1,2    1
        print("*",end=" ")
    print()