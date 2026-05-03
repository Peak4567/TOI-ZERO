W, L, M, N = map(int, input().split())

min_waste = W * L

for A in range(M, N + 1):
    rows_main = W
    cols_main = L // A
    used_main = rows_main * A * cols_main

    L_remain = L % A
    rows_rotated = L_remain
    cols_rotated = W // A
    used_rotated = cols_rotated * A * rows_rotated

    used_total = used_main + used_rotated
    waste = W * L - used_total

    if waste < min_waste:
        min_waste = waste

print(min_waste)