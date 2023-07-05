number: int = int(input('Введите четырехзначное число: '))

thousands = number // 1000
hundreds = (number // 100) % 10
tens = (number // 10) % 10
units = number % 10

print('Цифра в позиции тысяч:', thousands)
print('Цифра в позиции сотен:', hundreds)
print('Цифра в позиции десятков:', tens)
print('Цифра в позиции единиц:', units)
