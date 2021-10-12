class card:
    def __init__(self,color,number):
        self.color=color
        self.number=number
    def isCard(self):
        print( "you have color of card",self.color)
        print("number of card ",self.number)


class myCard(card):
    def isCard(self): #! overrinding classลูกเอาฟังก์ชันของ  classแม่ มาเขียนใหม่
        print("this is card have color ",self.color)
        print("number in card",self.number)


#inheritance
class ClassOne:
    def func1(self):
        print('We are in Base class')

class ClassTwo(ClassOne):
    def func2(self):
        print('We are in child class')

obj = ClassTwo()
obj.func1()
obj.func2()
if __name__ == "__main__":
    user1 = myCard("pink",5)
    user1.isCard()
    user2 = card("red",20)
    user2.isCard()
    obj1 = ClassTwo()
    obj1.func2()
    obj1.func1()
