number = int(input())

if number >= 1000 and number <= 999999:
    number_str = str(number)
    
    length = len(number_str)
    
    if length == 4:
        result = number_str[0] + "," + number_str[1] + number_str[2] + number_str[3]
    elif length == 5:
        result = number_str[0] + number_str[1] + "," + number_str[2] + number_str[3] + number_str[4]
    elif length == 6:
        result = number_str[0] + number_str[1] + number_str[2] + "," + number_str[3] + number_str[4] + number_str[5]
    print(result)
else:
    print("กรุณาป้อนตัวเลขในช่วง 1000-999999")