list=['geeks','for','geeks']
word='geeks'
n=2
count=0

for i in range(0,len(list)):
    if list[i]==word:
        count=count+1
        if count==n:
            del list[i]
print(list)



