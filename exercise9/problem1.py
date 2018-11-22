#이차원을 구현하고자 한다. 두점(이차원, x와y과 존재)을 입력으로 처리하고 두 점을 더해서 출력


x1 =  int(input())
y1=  int(input())
x2=  int(input())
y2=  int(input())

class plus:
    def __init__(self, x,y):
        self.x = x
        self.y = y
    def __add__(self, other):
        self.x  =self.x + other.x
        self.y = self.y + other.y

first = plus(x1,y1)
second = plus(x2, y2)
first + second
print(first.x, first.y)