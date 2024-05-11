sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

keys=["name", "salary"]
res=dict()
for i in keys:
    res.update({i:sample_dict[i]})
print(res)