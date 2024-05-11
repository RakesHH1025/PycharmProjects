mylist=[10,15,20,25,30,35]
ele=25
if ele in mylist:
    print("element found")
else:
    print("Element not found")

flag=0
for i in mylist:
    if (i==ele):
        print("element found")
        flag=1
        break
if flag==0:
    print("element not found")
