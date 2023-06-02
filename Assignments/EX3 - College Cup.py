m1 = input()
m2 = input()
m3 = input()
MS = [m1, m2, m3]
CS = 0
AM = 0
ST = 0
L = []
for match in MS:
    L += match.split('-')

for score in L:
    team = score[:2]
    if team == 'CS':
        CS += int(score[2])
    elif team == 'AM':
        AM += int(score[2])
    elif team == 'ST':
        ST += int(score[2])

if AM >= ST and AM >= CS:
    print('AM')
elif CS > AM and CS >= ST:
    print('CS')
elif ST > AM and ST > CS:
    print('ST')
