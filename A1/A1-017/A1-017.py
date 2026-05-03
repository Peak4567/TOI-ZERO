y1 = int(input())
m1 = int(input())
d1 = int(input())

y2 = int(input())
m2 = int(input())
d2 = int(input())

date1 = (y1,m1,d1)
date2 = (y2,m2,d2)

if date1 < date2:
    print(1)
elif date1 > date2:
    print(2)
else:
    print(0)