number: int = int(input('Введите положительное трехзначное число: '))

hundreds: int = number // 100
tens: int = number // 10 % 10
# tens: int = number % 100 // 10
units: int = number % 10

sum_digits: int = hundreds + tens + units

product_digits: int = hundreds * tens * units

print('Сумма цифр:', sum_digits)
print('Произведение цифр:', product_digits)
