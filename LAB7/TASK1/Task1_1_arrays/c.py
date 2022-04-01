n = int(input())
cnt = 0
a = [int(i) for i in input().split()]
for i in a:
    if i > 0:
        cnt += 1
print(cnt)