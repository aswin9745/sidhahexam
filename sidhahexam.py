li1 = [4,3,5,8,1]
li2 = []
v = 11
for i in li1:
    for j in li1:
        if i + j == v:
            li2.append(li1.index(i))
            li2.append(li1.index(j))
print (list(set(li2)))