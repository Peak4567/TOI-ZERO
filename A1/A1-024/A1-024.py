y = int(input())
n = int(input())
if y <= 1990 and n <= 1500:
    print("1250")
elif y <= 1990 and n >= 1500 and n <= 2000:
    print("1400")
elif y <= 1990 and n > 2000:
    print("2000")
elif y >= 1991 and y <= 1999 and n <= 1500:
    print("1100")
elif y >= 1991 and y <= 1999 and n > 1500 and n <= 2000:
    print("1300")
elif y >= 1991 and y <= 1999 and n > 2000:
    print("1700")
elif y >= 2000 and n <= 1500:
    print("1000")
elif y >= 2000 and n > 1500 and n <= 2000:
    print("1200")
else:
    print("2000")