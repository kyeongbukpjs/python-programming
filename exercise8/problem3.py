#1부터 10까지, 11부터 20까지, 21부터 30까지의 3개의 라인을 줄변경하여 file2.txt에 저장


t = ""
for i in range(3):
    for j in range(1,11):
        t += "%3d"%(10*i+j)
    t += "\n"

fw=open("file2.txt","w")
fw.write(t)
fw.close()