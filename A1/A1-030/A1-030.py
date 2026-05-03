n = int(input())

pairs_input = input().split()

numbers = []
for i in range(len(pairs_input)):
    numbers.append(int(pairs_input[i]))

sum_result = 0
max_values = []

for i in range(n):
    first_num = numbers[2 * i]
    second_num = numbers[2 * i + 1]
    
    if first_num > second_num:
        max_val = first_num
    else:
        max_val = second_num
    
    max_values.append(max_val)
    sum_result = sum_result + max_val

if n == 1:
    print(max_values[0])
else:
    equation = ""
    for i in range(n):
        if i == 0:
            equation = str(max_values[i])
        else:
            equation = equation + " + " + str(max_values[i])
    equation = equation + " = " + str(sum_result)
    print(equation)