# for i in range(4):
#     print("*"  *  4)
#
#
# for i in range(1, 6):  # Outer loop for rows from 1 to 5
#     print(" * "  *  i)  # Print '*' character i times for each row

n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print('*', end=' ')
    print()