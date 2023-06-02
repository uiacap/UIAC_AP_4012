rain = int(input())
work = int(input())
boots = int(input())
umbrella = int(input())
car = int(input())
if rain == 0:
    print(True)
if rain == 1:
    if boots == 1 or umbrella == 1 or car == 1:
        print(True)
    elif work != 0:
        print(True)
    else:
        print(False)
if rain == 10:
    if umbrella == 1 or car == 1:
        print(True)
    elif work == 10 or work == 100:
        print(True)
    else:
        print(False)
if rain == 100:
    if car == 1:
        print(True)
    elif work == 100:
        print(True)
    else:
        print(False)
