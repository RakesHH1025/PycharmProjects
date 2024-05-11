mylist = ["apple", "banana", "cherry"]
print(mylist)

mylist = ["apple", "banana", "cherry"]
print(mylist[2])

mylist = ["apple", "banana", "cherry"]
print(mylist[-1])

mylist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(mylist[2:5])

mylist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(mylist[-4:-1])

mylist = ["apple", "banana", "cherry"]
mylist[1] = "blackcurrant"
print(mylist)

mylist = ["apple", "banana", "cherry"]
for i in mylist:
    print(i)

mylist = ["apple", "banana", "cherry"]
if "apple" in mylist:
    print("present")
else:
    print("Not present")

mylist = ["apple", "banana", "cherry"]
print(len(mylist))

mylist = ["apple", "banana", "cherry"]
mylist.append("orange")
print(mylist)

mylist = ["apple", "banana", "cherry"]
mylist.insert(1, "orange")
print(mylist)

mylist = ["apple", "banana", "cherry"]
mylist.remove("banana")
print(mylist)

mylist = ["apple", "banana", "cherry"]
mylist.pop()
print(mylist)

mylist = ["apple", "banana", "cherry"]
del mylist[0]
print(mylist)

mylist = ["apple", "banana", "cherry"]
del mylist

mylist = ["apple", "banana", "cherry"]
mylist.clear()
print(mylist)

mylist = ["apple", "banana", "cherry"]
mylist = mylist.copy()
print(mylist)

mylist = ["apple", "banana", "cherry"]
mylist = list(mylist)
print(mylist)

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
for x in list2:
    list1.append(x)
print(list1)

list1.append(list2)
print(list1)

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)