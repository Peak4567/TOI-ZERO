char = input()
number = int(input())
if char == "H" and number == 4567:
    print("safe unlocked")
elif char == "H" and number != 4567:
    print("safe locked - change digit")
elif char != "H" and number == 4567:
    print("safe locked - change char")
else:
    print("safe locked")