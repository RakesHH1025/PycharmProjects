rows=5
for i in range(1,rows+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print(" ")

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

rows=5
for i in range(rows+1):
    for j in range(i):
        print(i,end=" ")
    print(" ")

# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

rows = 5
num = rows
for i in range(rows, 0, -1):
    for j in range(0, i):
        print(num, end=" ")
    print(" ")

# 5 5 5 5 5
# 5 5 5 5
# 5 5 5
# 5 5
# 5