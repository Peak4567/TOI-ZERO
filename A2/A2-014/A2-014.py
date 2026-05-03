def extend_short(name, length):
    while len(name) < length:
        name += name[len(name) % len(name)]
    return name

name1 = input()
name2 = input()

if len(name1) > len(name2):
    longer = name1
    shorter = extend_short(name2, len(name1))
else:
    longer = name2
    shorter = extend_short(name1, len(name2))

if len(name1) > len(name2):
    name2 = shorter
else:
    name1 = shorter

yanta = ''
for c1, c2 in zip(name1, name2):
    if c1.lower() in 'love' or c2.lower() in 'love':
        yanta += 'w'
    else:
        yanta += '$'

w_count = yanta.count('w')
max_w = 0
count = 0
for ch in yanta:
    if ch == 'w':
        count += 1
        if count > max_w:
            max_w = count
    else:
        count = 0

if w_count % 2 == 1:
    yanta += str(max_w)
else:
    if max_w < 2:
        yanta += '#'

print(yanta)
