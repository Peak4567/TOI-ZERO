n, m = map(int, input().split())

rules = []
for _ in range(m):
    line = list(map(int, input().split()))
    k = line[0]
    conditions = line[1:k+1]
    result = line[k+1]
    rules.append((conditions, result))

lights = [False] * (n + 1)
lights[1] = True

changed = True
while changed:
    changed = False
    for conditions, result in rules:
        if not lights[result]:
            all_on = True
            for bulb in conditions:
                if not lights[bulb]:
                    all_on = False
                    break
            if all_on:
                lights[result] = True
                changed = True

count = sum(lights[1:])
print(count)