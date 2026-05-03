n = int(input())
cars = [tuple(map(int, input().split())) for _ in range(n)]

max_v = 0
unsellable = 0

for p, v in reversed(cars):
    if v < max_v:
        unsellable += 1
    else:
        max_v = v

print(unsellable)
