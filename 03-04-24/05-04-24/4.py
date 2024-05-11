str="na@!%&*ra()yana"

import string
lower=string.ascii_lowercase
count=0
for i in str:
    if i not in lower:
        count=count+1
print(count)