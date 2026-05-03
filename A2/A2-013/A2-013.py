pearl_type, pearl_weight = input().split()
pearl_weight = int(pearl_weight)

tea_type, sweetness_level, tea_volume = input().split()
sweetness_level = int(sweetness_level)
tea_volume = int(tea_volume)

pearl_cal = {'H': 5, 'O': 3, 'J': 2}

tea_cal = {
    'R': [12, 18, 25],
    'T': [15, 20, 30],
    'M': [10, 15, 20]
}

total_cal = pearl_cal[pearl_type] * pearl_weight + tea_cal[tea_type][sweetness_level - 1] * tea_volume
print(total_cal)
