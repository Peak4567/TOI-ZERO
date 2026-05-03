t = int(input())
s = input()

s= s.upper()

if t <= 0 and t < 100 and s == "C" or t <= 32 and t < 212 and s == "F":
    print("solid")
elif t > 0 and t < 100 and s == "C" or t > 32 and t < 212 and s == "F":
    print("liquid")
else:
    print("gas")

