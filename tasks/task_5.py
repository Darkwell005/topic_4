wins: int = int(input('Введите количество побед: '))
draws: int = int(input('Введите количество ничейных игр: '))
losses: int = int(input('Введите количество поражений: '))

total_points: int = (wins * 3) + (draws * 1) + (losses * 0)

print('Общее количество очков:', total_points)
