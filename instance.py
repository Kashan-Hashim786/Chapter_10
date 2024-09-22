class emplyee:
    name = "Asad Abrar" # this is a class attribute
    language = "PYthon" # this is a class attribute
    salary = 1200000    # this is a class attribute

obj1 = emplyee()  # this is a object attribute
obj1.language = "Java"  # Instance attributes, take preference over class attributes during assignment & retrieval.
print(obj1.name)
print(obj1.language)
print(obj1.salary)

