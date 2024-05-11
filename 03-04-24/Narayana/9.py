str="Python Narayana Tech House Hyd oud"
str1=str.split()

for i in str1:
    if i[0].lower() in 'aeiou':
        print(i)
