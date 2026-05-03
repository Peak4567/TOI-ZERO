N, M = map(int, input().split())

image1 = [input() for _ in range(N)]

image2 = [input() for _ in range(N)]

def merge_symbols(a, b):
    if a == '-' and b == '-':
        return '-'
    elif a == '-' and b == '+':
        return '+'
    elif a == '-' and b == 'x':
        return 'x'
    elif a == '+' and b == 'x':
        return '*'
    return a

result = []
for i in range(N):
    row = []
    for j in range(M):
        row.append(merge_symbols(image1[i][j], image2[i][j]))
    result.append(''.join(row))

for row in result:
    print(row)
