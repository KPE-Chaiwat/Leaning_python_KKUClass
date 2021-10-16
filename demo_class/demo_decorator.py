class Student:
    def __init__(self,id,fName,lName):
        self.id = id
        self.fName = fName
        self.lName = lName
        #self.full_name = "{} {}".format(self.fName, self.lName)
    
    def full_name(self):
        return "{} {}".format(self.fName, self.lName)
    @property
    def full_name2(self):
        return "{} {} {}".format(self.fName, self.lName ,self.id)
    @property
    def join_yy(self):
        year_id = self.id[:2]
        return year_id
    @property
    def name_degrees(self):
        code_degree=self.id[3:7]
        Name_degrees= "name:"+self.fName+" ,code_degree: "+code_degree
        return Name_degrees
        
 # func1 --> func2(func1): =>return func1+upgrad 


def capsule(function):

    def new_function():
        print("critical=+2 ,speed=+333,str=+20")
        function()
        print("speed=+333,")
    return new_function


@capsule
def dota_charlector():
    print("sniper")






if __name__ == "__main__":
    obj = Student("643040664-6","tong","chaiwat")
    print(obj.full_name())
    # obj.full_name = "parin simak"
    # print(obj.full_name)
    print(obj.full_name2)# ไม่ต้องมีวงเล็บเพราะว่าใส่  @propertyไปแล้ว
    print(obj.join_yy)
    print(obj.name_degrees)

    dota_charlector()
#----------------------------------------------------------------
    