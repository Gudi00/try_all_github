from itertools import permutations
from collections import Counter


def max_fishka_power(n, m, k, queue):
    max_power = 0

    # Перебираем возможные размещения фишек на поле
    for placement in permutations(queue, min(n, m)):
        field = list(placement)
        levels = Counter((t, 1) for t in field)  # Начальные уровни фишек
        remaining_moves = k

        # Выполняем слияния, пока есть ходы
        while remaining_moves > 0:
            merged = False
            for (t, l), count in sorted(levels.items(), reverse=True):
                if count > 1:  # Если есть возможность объединить
                    merges = count // 2
                    levels[(t, l)] -= merges * 2
                    levels[(t, l + 1)] += merges
                    remaining_moves -= merges
                    merged = True
                    if remaining_moves <= 0:
                        break
            if not merged:
                break  # Если не удалось совершить ни одно объединение, останавливаемся

        # Вычисляем силу
        total_power = sum(t * l * count for (t, l), count in levels.items())
        max_power = max(max_power, total_power)

    return max_power


# Чтение входных данных
n, m, k = map(int, input().split())
queue = list(map(int, input().split()))

# Вычисление результата
print(max_fishka_power(n, m, k, queue))
