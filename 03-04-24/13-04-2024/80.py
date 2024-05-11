numbers=[1,2,3,4,5,6,7,8,10]
n=len(numbers)+1
total=n*(n+1)//2
print(total)
sum=0
for i in numbers:
    sum=sum+i
print(sum)

res=total-sum
print(res)