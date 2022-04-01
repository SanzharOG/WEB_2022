n = int(input())
a = [int(i) for i in input().split()]
b = a[::2]
print(*b)