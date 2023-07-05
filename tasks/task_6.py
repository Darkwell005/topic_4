num_1: int = int(input('Введите первое положительное число: '))
num_2: int = int(input('Введите второе положительное число: '))

is_divisible: bool = (num_1 % num_2) == 0
print(is_divisible)

# # Ошибочный результат при остатке 1
# is_divisible: int = num_1 % num_2
# print(bool(is_divisible) == is_divisible)
