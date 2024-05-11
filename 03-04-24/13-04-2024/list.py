mylist = ["apple", "banana", "cherry"]
print(mylist)

print(mylist[1])
print(mylist[-1])
mylist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(mylist[2:5])
mylist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(mylist[-4:-1])

mylist = ["apple", "banana", "cherry"]
mylist[1]="RakesH"
print(mylist)

mylist = ["apple", "banana", "cherry"]
for x in mylist:
    print(x)

if "apple" in mylist:
    print("Yes, 'apple' is in the fruits list")

mylist = ["apple", "banana", "cherry"]
print(len(mylist))

mylist.append("HRushitha")
print(mylist)

mylist.insert(1,"Green")
print(mylist)

mylist.remove("Green")
print(mylist)

mylist.pop()
print(mylist)

mylist = ["apple", "banana", "cherry"]
del mylist[0]
print(mylist)

mylist = ["apple", "banana", "cherry"]
mylist.clear()
print(mylist)

mylist = ["apple", "banana", "cherry"]
mylist = mylist.copy()
print(mylist)

mylist = ["apple", "banana", "cherry"]
mylist = list(mylist)
print(mylist)

mytuple = ("apple", "banana", "cherry")
print(mytuple)

mytuple = ("apple", "banana", "cherry")
print(mytuple[1])

mytuple = ("apple", "banana", "cherry")
print(mytuple[-1])

mytuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(mytuple[2:5])

print(mytuple[-4:-1])

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
