import random

def insertion_sort_range(arr, left, right):
  """Сортирует подмассив arr[left:right+1] вставками."""
  for i in range(left + 1, right + 1):
    key = arr[i]
    j = i - 1
    while j >= left and arr[j] > key:
      arr[j + 1] = arr[j]
      j -= 1
    arr[j + 1] = key

def _median_of_three(arr, low, high):
    """Находит медиану трех элементов (первого, среднего, последнего)
       и помещает ее в arr[low]. Возвращает индекс исходного пивота."""
    mid = (low + high) // 2
    # Сортируем low, mid, high, чтобы найти медиану
    if arr[low] > arr[mid]:
        arr[low], arr[mid] = arr[mid], arr[low]
    if arr[low] > arr[high]:
        arr[low], arr[high] = arr[high], arr[low]
    if arr[mid] > arr[high]:
        arr[mid], arr[high] = arr[high], arr[mid]
    # Теперь arr[mid] - это медиана. Поменяем ее с arr[low] для удобства
    # или оставим для некоторых схем разделения.
    # В данной реализации вернем индекс среднего элемента как пивот.
    # Либо, как вариант, поместим медиану в arr[high-1] (если используется
    # схема, где пивот сравнивается с arr[high-1]) или в arr[low].
    # Давайте поместим медиану в arr[low] для совместимости с
    # некоторыми вариантами разделения.
    arr[low], arr[mid] = arr[mid], arr[low]
    return low # Возвращаем индекс, где теперь находится медиана (пивот)

def quick_sort_improved(arr):
    """
    Улучшенная итеративная быстрая сортировка массива arr на месте.

    Args:
        arr: Список (list) чисел для сортировки.

    Returns:
        Отсортированный список (тот же объект arr).
    """
    # Константа для перехода на сортировку вставками для маленьких подмассивов
    INSERTION_SORT_CUTOFF = 10

    if not arr:
        return arr # Обработка пустого списка

    # Используем список как стек для хранения пар (left, right)
    stack = [(0, len(arr) - 1)]

    while stack:
        low, high = stack.pop()

        # Проверка размера подмассива
        if high - low + 1 < INSERTION_SORT_CUTOFF:
            # Используем сортировку вставками для маленьких подмассивов
            if low < high: # Убедимся, что есть хотя бы 2 элемента для сортировки
                 insertion_sort_range(arr, low, high)
            continue # Переходим к следующей итерации основного цикла

        if low < high:
            # --- Улучшенный выбор опорного элемента (медиана трех) ---
            # Находим медиану первого, среднего и последнего элементов
            # и помещаем её в arr[low] (или другое удобное место).
            # Это делает QuickSort более устойчивым к частично отсортированным
            # или обратно отсортированным данным.
            # Вариант: Использовать случайный пивот (более простой и часто эффективный):
            # pivot_index = random.randint(low, high)
            # arr[low], arr[pivot_index] = arr[pivot_index], arr[low]
            # pivot = arr[low]

            # Вариант с медианой трех (немного сложнее, но может быть лучше):
            pivot_index = _median_of_three(arr, low, high)
            pivot = arr[pivot_index] # Пивот теперь в arr[low]

            # --- Разделение (Partitioning) - Вариант Хоара ---
            # (Схема из оригинального кода, но с улучшенным пивотом)
            # Переменные для сохранения исходных границ для добавления в стек
            original_low, original_high = low, high

            # Начинаем указатели сразу после/перед пивотом (если пивот в arr[low])
            i = low + 1
            j = high

            while True:
                # Двигаем левый указатель (i), пока не найдем элемент >= pivot
                while i <= j and arr[i] < pivot:
                    i += 1
                # Двигаем правый указатель (j), пока не найдем элемент <= pivot
                while i <= j and arr[j] > pivot:
                    j -= 1

                # Если указатели пересеклись или сошлись
                if i >= j:
                    break

                # Меняем местами элементы, на которые указывают i и j
                arr[i], arr[j] = arr[j], arr[i]
                # Сдвигаем указатели после обмена
                i += 1
                j -= 1

            # Ставим пивот (который был в arr[low]) на его финальную позицию (arr[j])
            arr[low], arr[j] = arr[j], arr[low]
            pivot_final_index = j # Индекс, где теперь стоит пивот

            # --- Добавление подзадач в стек (с оптимизацией) ---
            # Добавляем в стек сначала БОЛЬШИЙ подмассив, чтобы глубина стека
            # была логарифмической в среднем и в худшем случае (для этой оптимизации).
            left_size = pivot_final_index - original_low
            right_size = original_high - pivot_final_index

            if left_size > right_size:
                # Левый больше, добавляем его первым
                if original_low < pivot_final_index - 1: # Проверка на непустой диапазон
                    stack.append((original_low, pivot_final_index - 1))
                if pivot_final_index + 1 < original_high: # Проверка на непустой диапазон
                    stack.append((pivot_final_index + 1, original_high))
            else:
                # Правый больше или равен, добавляем его первым
                if pivot_final_index + 1 < original_high: # Проверка на непустой диапазон
                    stack.append((pivot_final_index + 1, original_high))
                if original_low < pivot_final_index - 1: # Проверка на непустой диапазон
                     stack.append((original_low, pivot_final_index - 1))

    return arr # Возвращаем отсортированный массив