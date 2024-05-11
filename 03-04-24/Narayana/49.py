str='python narayana and python developer and python tester'
str1=str.split()
print(str1)
print(list({i for i in str1 if str1.count(i)>1}))