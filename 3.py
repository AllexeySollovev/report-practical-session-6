c1 = int(input('1 столбец: '))
r1 = int(input('1 строка: '))

c2 = int(input('2 строка: '))
r2 = int(input('2 столбец: '))

if (c1 + r1) % 2 == (c2 + r2) % 2:
    print("YES")
else:
    print("NO")
