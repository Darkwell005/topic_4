number = int(input('Введите положительное трехзначное число: '))

hundreds = number // 100
tens = number // 10 % 10
units = number % 10

sum_digits = hundreds + tens + units

product_digits = hundreds * tens * units

print('Сумма цифр:', sum_digits)
print('Произведение цифр:', product_digits)
