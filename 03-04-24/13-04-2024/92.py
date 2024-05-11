r1="ravikiran"
r2='teja'
i,j=0,0
op=""
while i<len(r1) or i<len(r2):
    if i<len(r1):
        op=op+r1[i]
        i=i+1
    if j<len(r2):
        op=op+r2[j]
        j=j+1
print(op)
