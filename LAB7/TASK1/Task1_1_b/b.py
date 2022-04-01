god = int(input())
print('YES') if((god % 4 == 0) and (god % 100 != 0)) or (god % 400 == 0) else print('NO')