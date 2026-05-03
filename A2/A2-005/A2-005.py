W, H, M, N = map(int, input().split())
x_cuts = list(map(int, input().split()))
y_cuts = list(map(int, input().split()))

x_positions = [0] + x_cuts + [W]
y_positions = [0] + y_cuts + [H]

widths = []
for i in range(1, len(x_positions)):
    widths.append(x_positions[i] - x_positions[i - 1])

heights = []
for i in range(1, len(y_positions)):
    heights.append(y_positions[i] - y_positions[i - 1])

areas = []
for w in widths:
    for h in heights:
        areas.append(w * h)

areas.sort(reverse=True)
print(areas[0], areas[1])
