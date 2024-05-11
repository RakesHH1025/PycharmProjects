my_list=[1,2,2,3,4,5,4,3,4]
# print([list({i for i in list if list.count(i)>=2})])

# my_list = [1, 2, 2, 3, 4, 5, 4, 3, 4]
result = [i for i in set(my_list) if my_list.count(i) >= 2]
print(result)
