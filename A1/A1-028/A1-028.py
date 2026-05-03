number = int(input())

if number >= 1000 and number <= 9999:
    number_str = str(number)
    
    reversed_str = number_str[3] + number_str[2] + number_str[1] + number_str[0]
    
    reversed_number = int(reversed_str)
    
    print(reversed_number)
else:
    print("กรุณาป้อนจำนวนเต็ม 4 หลัก (1000-9999)")