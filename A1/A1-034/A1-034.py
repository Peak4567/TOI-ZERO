n = int(input())
min_val = int(input())

for _ in range(n - 1):
    num = int(input())
    if num < min_val:
        min_val = num

print(min_val)
