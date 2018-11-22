
x= input()
v2 = ""
v1 = 0
for letter in x:
    if letter.isalpha():
        if letter in ["a","e","i","o","u"]:
            v2 += "M"+letter
        else:
            v2 += letter + "J"
    else:
        v1 +=int(letter)        
print('%7d,%s'%(v1, v2))