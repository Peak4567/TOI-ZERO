first_name = input()
last_name = input()
age = int(input())

first_list = list(first_name)
last_list = list(last_name)
age_list = list(str(age))
if len(first_name) > 5 and len(last_name) > 5:
    print(first_list[0]+first_list[1]+last_list[-1]+age_list[-1])
else:
    print(first_list[0]+''.join(age_list)+last_list[-1])
    