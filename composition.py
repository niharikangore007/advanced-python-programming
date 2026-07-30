# composition is a reelationship  where one class contains an object of another class.



class engine:
    def start(self):
        print("engine started")



class car:
    def __init__(self):
        self.engine=engine() # composition

    def drive(self):
        self.engine.start()
        print("car is moving")
c = car()
c.drive()