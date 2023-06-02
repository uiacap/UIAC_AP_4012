num = int(input())
total = 0
totcredit = 0
for i in range(num):
    course = float(input())
    credit = int(input())
    totcredit = totcredit + credit
    total += course * credit
    
answer = float(total / totcredit) 
print(answer)
