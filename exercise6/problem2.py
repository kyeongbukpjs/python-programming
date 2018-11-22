# 수1을 입력 받고 이 수가 prime인지 아닌지 판단하는 함수를 생성하고 prime이면 1을 출력하고 아니라면 0을 출력


x1 = int(input())


def prime(x):
    for i in range(2,x):
        if x%i == 0:
            return print(0)
    return print(1)


prime(x1)