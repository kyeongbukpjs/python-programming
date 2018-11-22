#2번 문제를 상속받아서 3차원 두점을 입력 받고 각 좌표에서 큰값만을 취해서 출력


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
        
first = maxx(x1,y1,z1)
second =maxx(x2, y2,z2)
first.bigger(second)
print(first.x, first.y, first.z)