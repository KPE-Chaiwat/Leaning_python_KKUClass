import math
class Cartesian:
       def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
       def distance(self):
        dimension = self.x**2 + self.y**2 + self.z**2
        radius = math.sqrt(dimension)
        print("ระยะทางจากจุด (0,0,0) ไปยังจุด (",self.x,",",self.y,",",self.z,")คืิอ","%.2f"%(radius),"หน่วย")#!จัด format 2 ตน.

if __name__ == "__main__":
 while True:
    try:
       print("กรอกตัวเลขจุด x,y,z ")
       axis_x = int(input("ค่าแกนx:"))
       axis_y = int(input("ค่าแกนy:"))
       axis_z = int(input("ค่าแกนz:"))
       Obj = Cartesian(axis_x, axis_y, axis_z)
       Obj.distance()
       break
    except ValueError: 
       print("ใส่ตัวเลขซิครับ ปัดโถ่(เสียงลุงแถวบ้าน)")
    except :
       print("Something Wrong")
    

 


   
