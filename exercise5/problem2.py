#입력한 두수의 최대공약수


x = int(input())
y = int(input())
temp = 0
if x<y:
    temp = x
    x = y
    y = temp

while y !=0:
    temp = x
    x = y
    y = temp%y

print(x)