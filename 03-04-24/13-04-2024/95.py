class myclass:
    a,b=100,200
    def myfun(self):
        x,y=10,20
        print(self.a+self.b)
        print(x+y)
obj=myclass()
obj.myfun()
print()