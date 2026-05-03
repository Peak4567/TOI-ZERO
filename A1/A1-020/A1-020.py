n1 = int(input())
n2 = int(input())
n3 = int(input())

if n1 < n2 and n2 < n3 and n1 < n3:
    print("increasing")
elif n1 > n2 and n2 > n3 and n1 > n3:
    print("decreasing")
else:
    print("neither")
