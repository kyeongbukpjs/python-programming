#두수를 입력 받아 max_f(x, y)를 함수로 구현하시오. 큰값을 리턴받아서 출력


x1 = int(input())
x2 = int(input())

def max_f(x,y):
    if x < y:
        print(y)
    else:
        print(x)

max_f(x1,x2)