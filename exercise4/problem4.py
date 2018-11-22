#1명당 국,영,수 성적을 입력받는데, 총 3명을 입력받는다. 특정학생의 번호를 입력하면
#국, 영, 수학의 성적을 올림차순으로 출력하고 최고점과 최하점을 출력한다.


x1 = int(input())
x2= int(input())
x3 = int(input())
x4 = int(input())
x5 = int(input())
x6 = int(input())
x7 = int(input())
x8 = int(input())
x9 = int(input())
y = int(input())
d  = {}
d[1] = [x1,x2,x3]
d[2] = [x4,x5,x6]
d[3] = [x7,x8,x9]
d[y].sort()
print(d[y],d[y][2],d[y][0])