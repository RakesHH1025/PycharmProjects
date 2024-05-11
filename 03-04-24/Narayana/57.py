# for i in range(4, 0, -1):  # Outer loop for rows from 4 to 1 in reverse order
#     print(" * " * i)  # Print '*' character i times for each row

n=5
for i in range(1,n+1):
    for j in range(1,n+2-i):
        print('*',end=' ')
    print()