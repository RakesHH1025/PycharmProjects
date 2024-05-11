sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}
keys=['salary','city']

for i in keys:
    sample_dict.pop(i)
print(sample_dict)

sample_dict = {'a': 100, 'b': 200, 'c': 300}

if 200 in sample_dict.values():
    print("present")
else:
    print("Not present")