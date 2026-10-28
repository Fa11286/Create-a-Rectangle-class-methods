class Rectangler:
    def __init__(self) :
     self.area_tri = 0
     self.parimeter_tri = 0
     self.width = 0
     self.hight = 0

    
    def area(self):
        self.hight = float(input("enter the hight of rectangler: "))
        self.width = float(input("enter the width of rectangler: "))
        self.area_tri = self.width * self.hight
        print("your rectanger area is", self.area_tri)
        

    def perimeter(self):
        self.hight = float(input("enter the hight of perimeter: "))
        self.width = float(input("enter the width of perimeter: "))
        self.perimeter_tri = 2 * (self.width + self.hight)
        print("your rectanger perimeter is", self.perimeter_tri)
        


try: 
 r1 = Rectangler()
 r1.area()
 r1.perimeter()
except Exception as r1:
 print("error" ,r1)
 