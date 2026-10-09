c1 = int(input('1 столбец: '))
r1 = int(input('1 строка: '))

c2 = int(input('2 строка: '))
r2 = int(input('2 столбец: '))

if c1 == c2 or r1 == r2 or abs(c1 - c2) == abs(r1 - r2):
    print("YES")
else:
    print("NO")
