interval: int = int(input('Введите величину временного интервала в минутах: '))

hours: int = interval // 60
minutes: int = interval % 60

print('	Результат:', hours, 'часа', minutes, 'минут')
