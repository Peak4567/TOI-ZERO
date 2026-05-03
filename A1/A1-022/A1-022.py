day = int(input())
month = int(input())
if month == 12 and day >= 22 or month == 1 and day <= 19:
    print("capricorn")
elif month == 1 and day >= 20 or month == 2 and day <= 18:
    print("aquarius")
elif month == 2 and day >= 19 or month == 3 and day <= 20:
    print("pisces")
elif month == 3 and day >= 21 or month == 4 and day <= 19:
    print("aries")
elif month == 4 and day >= 20 or month == 5 and day <= 20:
    print("taurus")
elif month == 5 and day >= 21 or month == 6 and day <= 21:
    print("gemini")
elif month == 6 and day >= 22 or month == 7 and day <= 22:
    print("cancer")
elif month == 7 and day >= 23 or month == 8 and day <= 22:
    print("leo")
elif month == 8 and day >= 23 or month == 9 and day <= 22:
    print("virgo")
elif month == 9 and day >= 23 or month == 10 and day <= 23:
    print("libra")
elif month == 10 and day >= 24 or month == 11 and day <= 21:
    print("scorpio")
elif month == 11 and day >= 22 or month == 12 and day <= 21:
    print("sagittarius")