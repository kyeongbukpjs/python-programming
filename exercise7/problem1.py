
x= int(input())
y = int(input())
for a in range(x,0,-1):
    for b in range(1, y+1):
        if a-1<b:
            print("%4d"%(100*a+b-a+1),end = "")
        else:
            print("    ",end="")
    print()