# 이중 반복문 사용하여 주어진 빌딩 출력하기


for a in range(9,0,-1):
    for b in range(1,8):
        
        if (a in range(5,9)) and(b in range(6,8)):
            continue

        else:
            print("",100*a+b, end="")

    print()