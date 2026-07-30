class student:  # public only . comes
    def __init__(self,name,marks):
        self.__name= name# protected add ._ and .__ for pivate

    def display(self):
        print("name:", self.__name)

s1 = student("niharika", 71)
s1.display()
print(s1.__name)