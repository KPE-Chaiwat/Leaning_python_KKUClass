class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)
  def nNumber(self):
    print(2+3)

class Student(Person):
  pass

x = Student("Mike", "Olsen")
y = Student("parin","kku")
y.nNumber()



