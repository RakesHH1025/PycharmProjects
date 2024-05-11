str="p!@$%^&at^&hon"

import string
# string.ascii_letters
# string.digits

# print([i for i in str if i not in string.ascii_letters and i not in string.digits and i!=''])
for i in str:
    if i not in string.ascii_letters:
        if i not in string.digits:
            print(i,end=" ")