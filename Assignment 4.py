import math
class Triangle:
    def __init__(self,s1=1,s2=1,s3=1):
        self.s1= s1
        self.s2= s2
        self.s3= s3
    def GetSide(self):
        return self.s1,self.s2,self.s3
    def Perimeter(self):
        return self.s1 + self.s2 + self.s3
    def Area(self):
        s=(self.s1 + self.s2 + self.s3)/2
        return math.sqrt(s*(s-self.s1)*(s-self.s2)*(s-self.s3))
n1=float(input("Enter first side of the Triangle "))
n2=float(input("Enter second side of the Triangle "))
n3=float(input("Enter third side of the Triangle "))
if (n1<=0):
     print(n1," is not a valid number")
     if (n2<=0):
         print(n2," is not a valid number")
         if (n3<=0):
             print(n3," is not a valid number")
elif((n1+n2>=n3 and n1+n3>=n2) and (n2+n3>=n1)):
    t=Triangle(n1,n2,n3)
    print("The sides of Triangle are:",t.GetSide())
    print("The area of Triangle is",t.Area())
    print("The perimeter of Triangle is",t.Perimeter())

else:
     print(n1,n2,n3, " do not form a triangle")
    
