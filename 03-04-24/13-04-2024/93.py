s="a4b3c2"
op=''
for i in s:
    if i.isalpha():
        x=i
    if i.isdigit():
        d=int(i)
        op=op+x*d
print(op)