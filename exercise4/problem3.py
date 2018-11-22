#문자열 강 문제, 각각 문자열의 확률 구하기

d = {"a":7 ,"b":9 ,"c":11 ,"d":13 ,"e":3 ,"f":20 ,"g":5 ,"h":30 ,"i":2 ,"j":5 }
x = input()
y = ",".join(x).split(",")
s = 0
i = 0
for Y in y:
    i+=1
    s += d[Y]


print(s//i + ((s%i)and 1))
