n=5

for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")

for i in range(1,n+1):
    for j in range(1,n+2-i):
        print(j,end=" ")
    print(" ")