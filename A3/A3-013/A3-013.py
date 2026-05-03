n, s = map(int, input().split())
heights = []
for _ in range(n):
    heights.append(int(input()))

min_mountain_distance = 0
max_mountain_distance = 0

for height in heights:
    if height % 3 == 0 and height % 4 != 0:
        # แบบที่ 1 เท่านั้น
        h = height // 3
        distance = 2 * 5 * h
        min_mountain_distance += distance
        max_mountain_distance += distance
    elif height % 4 == 0 and height % 3 != 0:
        # แบบที่ 2 เท่านั้น
        h = height // 4
        distance = 2 * 5 * h
        min_mountain_distance += distance
        max_mountain_distance += distance
    else:
        # ทั้งแบบที่ 1 และแบบที่ 2 ได้
        # แบบที่ 1: height = 3*H -> distance = 2*5*H = 10*H
        h1 = height // 3
        distance1 = 2 * 5 * h1
        
        # แบบที่ 2: height = 4*H -> distance = 2*5*H = 10*H
        h2 = height // 4
        distance2 = 2 * 5 * h2
        
        min_mountain_distance += min(distance1, distance2)
        max_mountain_distance += max(distance1, distance2)

min_flat_distance = s - max_mountain_distance
max_flat_distance = s - min_mountain_distance

print(min_flat_distance, max_flat_distance)