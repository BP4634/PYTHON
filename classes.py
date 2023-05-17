import triangle
from Functions import reverse_string




class mammal:
    def walk():
        print("walking")

class dog(mammal):
    def bark():
        print("hou hou")

class cat(mammal):
    def meow():
        print("meow meow")

dog.walk()
dog.bark()
cat.walk()
cat.meow()

triangle.triangle(5)

triangle.triangulo(9)


reverse_string("43210")