a, b = int(input()), int(input())
for i in range(b + 1):
    if i**2 in range(a, b + 1):
        print(i**2)