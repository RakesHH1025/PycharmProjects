str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
str=[]
for i in str_list:
    if i:
        str.append(i)
print(str)