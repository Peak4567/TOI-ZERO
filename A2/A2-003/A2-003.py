N = int(input())
H = list(map(int, input().split()))

count = 0
for i in range(N):
    left = H[i-1] if i > 0 else -1
    right = H[i+1] if i < N-1 else -1

    if H[i] > left and H[i] > right:
        count += 1

print(count)
