n = int(input())
cnt = 0
a = [int(i) for i in input().split()]
for i in range(1, len(a) - 1):
    if a[i] > 0 & a[i - 1] > 0:
        print('YES')
        break
    else:
        print('NO')
        break