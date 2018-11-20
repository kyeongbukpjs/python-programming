# 필요한 버스와 따라가는 선생님 인원 결정문제
# 버스 = 학생 23명 + 선생님 1명
# 버스 다 채우지 못한 학생은 선생님의 자가용 탐
# 자가용 = 선생님 한명 + 학생 3명
# 입력한 학생 수에 맞춰 필요한 버스의 댓수와 최소로 필요한 선생님의 인원 출력하기 문제


x = int(input())
busN = x//23
Remain = x%23
carN = Remain//3
plus = Remain%3 and 1
print(busN, busN+carN+plus)