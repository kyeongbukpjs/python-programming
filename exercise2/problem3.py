#5자리 정수 입력받고 914를 더한 후 결과를 자릿수별 분리해서 출력

x = int(input())
y = str(x+914)
for i in range(5):
    print(y[i])