#4번 문제를 상속받아서 두점을 입력 받고 두 점의 거리를 출력


import math
x1 =  int(input())
y1=  int(input())
z1 =   int(input())
x2=  int(input())
y2=  int(input())
z2=  int(input())

class plus:
    def __init__(self, x,y):
        self.x = x
        self.y = y
    def __add__(self, other):
        self.x  =self.x + other.x
        self.y = self.y + other.y


class plus3(plus):
    def __init__(self, x,y,z):
        super(plus3,self).__init__(x,y)
        self.z = z
    def __add__(self, other):
        super(plus3,self).__add__(other)
        self.z = self.z + other.z

class maxx(plus3):
    def bigger(self, other):
        self.x = max(self.x,other.x)
        
        self.y = max(self.y,other.y)
        
        self.z = max(self.z,other.z)

class eq(plus3):
    def eqq(self,other):
        if (self.x == other.x) and (self.y == other.y) and (self.z == other.z):
            print("eq")
        else:
            print("not eq")

class dist(eq):
    def distance(self, other):
        return math.sqrt((self.x - other.x)**2 +(self.y - other.y)**2 +(self.z - other.z)**2)

first = dist(x1,y1,z1)
second =dist(x2, y2,z2)
print("%.2f"%first.distance(second))