n = int(input())

result = []
for i in range(n, -1, -1):
    if i % 10 == 0:
        result.append(str(i))

print(" ".join(result))
