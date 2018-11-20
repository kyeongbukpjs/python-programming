#임의로 입력 받은 문자열에서 각 문자의 구분기호를 사용하여 join과 split을 이용하여 출력해보기

x = input()
x = ":".join(x)
print(x.split(":"))