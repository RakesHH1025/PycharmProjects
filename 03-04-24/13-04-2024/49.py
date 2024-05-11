input_str = "PYnative29@#8496"
total=0
count=0
for i in input_str:
    if i.isdigit():
        total=total+int(i)
        count=count+1
op=total/count
print(op)