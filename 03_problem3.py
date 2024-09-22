class problem3:
 a = 8    # this is a class attribute
 
object1 = problem3()
print(object1.a)  # print the class attribute because instance attribute is not present
object1.a = 0  # instance attribute is set

print(object1.a)   # print the instance attribute because instance attribute is present
print(problem3.a)   # print the class attribute

# The class attribute does not change