# 1부터 입력한 수까지의 짝수의 합


x = int(input())
sum = 0
for i in range(0, x+1,2):
    sum += i
print(sum)