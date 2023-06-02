p1 = input()
p2 = input()
p3 = input()


points = [p1, p2, p3]

ExPts = []

for person in points:
    templist = person.split()
    numtemp = []
    for num in templist[1:]:
        numtemp.append(int(num))
    templist = [templist[0]] + [sum(numtemp)]
    ExPts.append(templist)


tempsort = [ExPts[0]]
for i in range(1, 3):
    if ExPts[i][1] > tempsort[0][1]:
        tempsort.insert(0, ExPts[i])
    elif len(tempsort) > 1:
        if ExPts[i][1] <= tempsort[0][1] and ExPts[i][1] > tempsort[1][1]:
            tempsort.insert(1, ExPts[i])
        else:
            tempsort.append(ExPts[i])
    else:
        tempsort.append(ExPts[i])
ExPts = tempsort

print(ExPts)
