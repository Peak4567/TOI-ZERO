size, ramen_type = input().split()

topping_data = input().split()

price_table = {
    'S': {'R': 60, 'T': 80},
    'M': {'R': 80, 'T': 100},
    'L': {'R': 100, 'T': 120}
}

base_price = price_table[size][ramen_type]

if topping_data[0] == 'N':
    total_price = base_price
else:
    topping_type = topping_data[0]
    topping_qty = int(topping_data[1])
    if topping_type == 'P':  # หมูชาชู ชิ้นละ 15 บาท
        topping_price = 15 * topping_qty
    elif topping_type == 'E':  # ไข่ ฟองละ 10 บาท
        topping_price = 10 * topping_qty
    else:
        topping_price = 0
    total_price = base_price + topping_price

print(total_price)
