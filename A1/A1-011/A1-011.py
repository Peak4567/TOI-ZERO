char = input()
list_char = list(char)
text_char = dict.fromkeys(list_char)
for x in text_char:
    count = list_char.count(x)
    print(str(count)+x,end="")

    






