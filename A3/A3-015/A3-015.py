n = int(input())
heights = []
for _ in range(n):
    heights.append(int(input()))

heights.sort()

total_distance = 0
cumulative_height = 0

for height in heights:
    cumulative_height += height
    total_distance += cumulative_height * 2

print(total_distance)