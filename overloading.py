class calculator:
    def add(self,a=0, b=0, c=0):
        print("sum", a + b + c)

c = calculator() 

c.add(10)
c.add(10,20)
c.add(10,20,30)