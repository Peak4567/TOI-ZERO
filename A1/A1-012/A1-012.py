number = int(input())
mark = input()
reverse = str(number)[::-1]

if mark == "+":
    print(number,mark,reverse,"=",number+int(reverse))
elif mark == "*":
    print(number,mark,reverse,"=",number*int(reverse))

