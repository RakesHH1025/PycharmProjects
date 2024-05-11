myset = {"apple", "banana", "cherry"}
print(myset)

myset = {"apple", "banana", "cherry"}
for x in myset:
    print(x)

myset = {"apple", "banana", "cherry"}
print("banana" in myset)

myset = {"apple", "banana", "cherry"}
myset.add("orange")
print(myset)

myset = {"apple", "banana", "cherry"}
myset.update(["orange", "mango", "grapes"])
print(myset)

myset = {"apple", "banana", "cherry"}
print(len(myset))

myset = {"apple", "banana", "cherry"}
myset.remove("banana")
print(myset)

myset = {"apple", "banana", "cherry"}
myset.discard("banana")
print(myset)

myset = {"apple", "banana", "cherry"}
myset.clear()
print(myset)

myset = {"apple", "banana", "cherry"}
del myset
# print(myset)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)

mydict = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
print(mydict)

x = mydict["model"]


x = mydict.get("model")
print(x)

mydict = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
mydict["year"] = 2018

for x in mydict:
    print(x)

for x in mydict:
    print(mydict[x])

for x in mydict.values():
    print(x)

for x, y in mydict.items():
    print(x, y)

mydict = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
if "model" in mydict:
    print("Yes, 'model' is one of the keys in the mydict dictionary")

mydict = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

mydict["color"] = "red"
print(mydict)

mydict = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
mydict.pop("model")
print(mydict)

Mydict1 = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
# mydict2 = mydict1.copy()
# print(mydict2)

