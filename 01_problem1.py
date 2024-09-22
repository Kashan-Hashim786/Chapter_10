class programmer:
    company = "Microsoft"

    def __init__(self,name,salary,language,pinCode) -> None:
        self.name = name
        self.salary = salary
        self.language = language
        self.pinCode = pinCode

    def getInfo(self):
        print(f"Name : {self.name}")
        print(f"Salary : {self.salary}")
        print(f"Language : {self.language}")
        print(f"PIN Code : {self.pinCode}")
object1 = programmer("Atif Ali",250000,"Python","76541")
object1.getInfo()
print("")
object2 = programmer("Laksh Kumar",450000,"JavaScript","94321")
object2.getInfo()