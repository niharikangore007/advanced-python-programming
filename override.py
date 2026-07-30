class animal:
    def sound (self):
     return "some generic sound"

class dogoverride(animal):
    def sound (self):
        return "bark!"
    
animal1 = animal()
dog = dogoverride()

print("animal sound:", animal1.sound())
print("dog sound:", dog.sound())


# shapes
class shape:
   def draw(self):
      print("drawing shape")
    
class circle(shape):
   def draw(self):
      print("drawing a circle")


class rectangle(shape):
   def draw(self):
      print("drawing rectangle")


s = circle()
s.draw()

s = rectangle()
s.draw()
   
   


      