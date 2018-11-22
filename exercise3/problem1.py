# 5개의 정수 표준 입력으로 입력, 이를 원소로 가지는 리스트를 생성 후 역정렬하여 표준 출력하기

x1 = int(input())
x2 = int(input())
x3 = int(input())
x4 = int(input())
x5 = int(input())
A = [x1,x2,x3,x4,x5]
A.sort(reverse=True)
print(A)