#1번 문제의 이차원 점을 상속 받고 3차원 의 두점을 입력 받아서 합을 출력


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

    
first = plus3(x1,y1,z1)
second = plus3(x2, y2,z2)
first + second
print(first.x, first.y, first.z)