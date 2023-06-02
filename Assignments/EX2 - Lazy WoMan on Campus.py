import math

def distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def compare(_class,dorm,e):
    
    if _class * e > dorm:
        print("Dorm") 
    else:
        print('Class')

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())
e = float(input())
point1 = x1, y1
point2 = x2, y2
point3 = x3, y3

d1 = distance(point1, point2)

d2 = distance(point1, point3)
compare(d1, d2, e)

