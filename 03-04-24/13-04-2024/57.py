sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
str=dict()
for i in sample_list:
    count=sample_list.count(i)
    str[i]=count
print(str)
