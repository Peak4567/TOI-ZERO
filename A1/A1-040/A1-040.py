calories = {1: 100, 2: 120, 3: 200, 4: 60}
total_cal = 0

order = 0
while order != 5:
    order = int(input())
    if order in calories:
        total_cal += calories[order]

print("Bye Bye")
print("Total Calories:",total_cal)
