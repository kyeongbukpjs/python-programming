#암호문제
#입력된 두 문자열에서 겹치는 문자를 제외, 중복 x
#문자들의 순서를 내림차순으로 정렬하면 최종 사용 수 있는 키가됨


x1 = input()
x2 = input()
x1 = set(",".join(x1).split(","))
x2 = set(",".join(x2).split(","))
x3 = list(x1^x2)
x3.sort()
print(x3)