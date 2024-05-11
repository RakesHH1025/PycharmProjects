class Animal:
    def __init__(self,name):
        self.name=name

    def sound(self):
        print("Some generic sound")


class cat(Animal):
    def s