import random
class train:
    def __init__(slf,trainNo) -> None:
        slf.trainNO = trainNo

    def bookTicket(self,fro,to):
        print(f"Ticket is booked in train no {self.trainNO} from {fro} to {to}")

    def getStatus(harry):
        print(f"Train no {harry.trainNO} is running on time")

    def getFareInfo(jack,fro,to):
        print(f"Ticket fare in train no {jack.trainNO} from {fro} to {to} is {random.randint(100,6000)}")

object1 = train(98707)
object1.bookTicket("Lahore","Multan")
object1.getStatus()
object1.getFareInfo("Karachi","Sukkur")

# Nothing happened after change "self" to "slf" , "harry" or "jack"