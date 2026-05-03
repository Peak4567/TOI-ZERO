num1 = int(input())
num2 = int(input())
num3 = int(input())

even_count = 0
odd_count = 0

if num1 % 2 == 0:
    even_count = even_count + 1
else:
    odd_count = odd_count + 1

if num2 % 2 == 0:
    even_count = even_count + 1
else:
    odd_count = odd_count + 1

if num3 % 2 == 0:
    even_count = even_count + 1
else:
    odd_count = odd_count + 1

print("even", even_count)
print("odd", odd_count)