import math
class calculator:

    def __init__(self,n) -> None:
        self.n = n

    @staticmethod
    def greet():
        print("Hello there,")

    def square(self):
        print(f"The square of {self.n} is {self.n * self.n}")
    
    def cube(self):
        print(f"The cube of {self.n} is {self.n * self.n * self.n}")
    
    def squareRoot(self):
        print(f"The square root of {self.n} is {math.sqrt(self.n)}")

object1 = calculator(16)
object1.greet()
object1.square()
object1.cube()
object1.squareRoot()