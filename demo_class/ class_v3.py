class Base1:
    l = 12
    def length(self):
        return self.l

class Base2:
    b =20
    def breadth(self):
        return self.b

class DerivedClass(Base1,Base2):
    def area(self):
        return self.l * self.b

reg = DerivedClass()
#print(reg.area())
print(issubclass(Base1,Base2))#!issubclass=>
print(issubclass(Base2,DerivedClass))
print(issubclass(DerivedClass,Base2))