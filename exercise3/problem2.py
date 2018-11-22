# 표준 입력한 3개의 문자열을 원소로 가지는 리스트 2개를 생성
# 이 두 리스트의 각 인덱스의 원소를 합친 문자열을 표준 출력하기

x1 = input()
x2 = input()
x3 = input()
x4 = input()
x5 = input()
x6 = input()
A = [x1,x2,x3]
B = [x4,x5,x6]
C = [A[0]+B[0],A[1]+B[1],A[2]+B[2]]
print(C)