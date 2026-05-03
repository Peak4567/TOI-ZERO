n = int(input())

light = [0] * 360

for i in range(n):
    a, b = map(int, input().split())

    if a < b:
        for j in range(a, b):
            light[j] = 1
    else:
        for j in range(a, 360):
            light[j] = 1
        for j in range(0, b):
            light[j] = 1

full_coverage = True
for i in range(360):
    if light[i] == 0:
        full_coverage = False
        break

if full_coverage:
    print(360)
else:
    max_length = 0
    current_length = 0

    for i in range(720):
        pos = i % 360

        if light[pos] == 1:
            current_length += 1
            max_length = max(max_length, current_length)
        else:
            current_length = 0

    print(max_length)