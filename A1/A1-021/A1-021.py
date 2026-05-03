year = int(input())

if year < 1582:
    if year == 1500:
        print("yes")
    else:
        print("no")
else:
    if year % 400 == 0:
        print("yes")
    elif year % 100 == 0:
        print("no")
    elif year % 4 == 0:
        print("yes")
    else:
        print("no")