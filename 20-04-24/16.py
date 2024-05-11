str="madam"
rev=""
for i in str:
    rev=i+rev
print(rev)

if str==rev:
    print("Palindrome")
else:
    print("Not palindrome")