#두개의 좌표(3차원)를 입력 받고 두 점이 같은 점인지 다른 점인지 구분하여 출력


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
first = eq(x1,y1,z1)
second =eq(x2, y2,z2)
first.eqq(second)