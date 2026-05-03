N, L = map(int, input().split())

intervals = []
for _ in range(N):
    Si, Ti = map(int, input().split())
    intervals.append((Si, Ti))

intervals.sort(key=lambda x: x[1])

count = 0
last_toll = -1

for Si, Ti in intervals:

    if Si > last_toll:
        count += 1
        last_toll = Ti

print(count)