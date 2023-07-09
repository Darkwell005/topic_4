num_switches: int = int(input('Введите количество переключателей: '))

combinations = 2 ** num_switches
print('Количество возможных комбинаций:',combinations)
