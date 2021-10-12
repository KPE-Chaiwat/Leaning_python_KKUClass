import math
class Cartesian:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def distance(self):#distance แค่่ชื่อ เปลี่ยนได้
        dimension = self.x**2 + self.y**2 + self.z**2 #dimension แค่่ชื่อ เปลี่ยนได้
        radius = math.sqrt(dimension) #radius แค่่ชื่อ เปลี่ยนได้
        print("ระยะทาง คืิอ",radius)



axis_x = int(input("x:"))
axis_y = int(input("y:"))
axis_z = int(input("z:"))
isLong = Cartesian(axis_x, axis_y, axis_z) #isLong แค่่ชื่อ เปลี่ยนได้
isLong.distance()#distance แค่่ชื่อ เปลี่ยนได้
    
