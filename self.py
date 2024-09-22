class emplyee:

    language = "PYthon" # this is a class attribute
    salary = 1200000    # this is a class attribute
    
    def getInfo(self):
        print(f"The language is {self.language} and salary is {self.salary}")

    @staticmethod    # Sometimes we need a function that does not use the self-parameter. We can define it as static method
    def greet():
        print("Good Evening")
obj1 = emplyee()  # this is a object attribute
# obj1.language = "Java"  # Instance attributes, take preference over class attributes during assignment & retrieval.

obj1.getInfo()
# we can also this statement to run this method "getInfo"
# emplyee.getInfo(obj1)

obj1.greet()