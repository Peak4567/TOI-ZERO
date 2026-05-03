money = int(input())
money_type = [10, 5, 2, 1]

for x in money_type:
    count = money // x  # จำนวนเหรียญชนิด x
    print("{} = {}".format(x, count))
    money = money % x