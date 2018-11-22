#두점을 입력받아 직선의 방정식을 구하시오. 


x1 = int(input())
y1 = int(input())
x2= int(input())
y2 = int(input())

def formular(x1,y1,x2,y2):
    if x1 == x2:
        print("x=%d"%x1)
    else:
        print("y=%8.2fx+%8.2f"%((y2-y1)/(x2-x1), y1 - (y2-y1)/(x2-x1)*x1))
formular(x1,y1,x2,y2)