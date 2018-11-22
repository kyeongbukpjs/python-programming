
x0 = int(input())
x1 = int(input())
x2 = int(input())
x3 = int(input())
x4 = int(input())

time = int(input())

x = [x0,x1,x2,x3,x4]
add_water = [90,80,91,99,70]
for step in range(time):
    for i in range(len(x)):
        if x[i] + add_water[i] <= 2000:
            x[i] += add_water[i]
        else:
            x[i] = add_water[i]
print('%2d,%5d'%(x.index(max(x))+1,max(x)))