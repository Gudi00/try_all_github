def extract_variable(line):
    # Извлекаем имя переменной для строк вида:
    # "let x = new();" – возвращает "x"
    # "drop(x);"   – возвращает "x"
    if line.startswith("let"):
        # Предполагается, что слово с именем переменной идет вторым
        parts = line.split()
        return parts[1]
    elif line.startswith("drop"):
        start = line.find("(")
        end = line.find(")")
        return line[start + 1:end]
    return ""


def main():
    n = int(input().strip())
    input_lines = [input().rstrip() for _ in range(n)]

    # Результирующий список строк (будем выводить их в конце)
    result = []
    # Стек для команд let; элементы – кортеж (имя переменной, позиция в result)
    stack = []
    # Список авто-групп, где каждый элемент — кортеж (индекс открытия блока, индекс закрытия блока)
    auto_groups = []

    i = 0
    while i < n:
        line = input_lines[i]
        if line.startswith("let"):
            # Добавляем строку let в результат и в стек
            var = extract_variable(line)
            result.append(line)
            stack.append((var, len(result) - 1))
            i += 1
        elif line.startswith("drop"):
            var = extract_variable(line)
            # Если drop соответствует вершине стека — начинаем проверку последовательных автоосвобождений
            if stack and stack[-1][0] == var:
                # Сохраним индексы команд let, для которых выполняется автоосвобождение
                group_let_indices = []
                # Группируем все подряд идущие команды drop, которые соответствуют текущему стеку
                while i < n and input_lines[i].startswith("drop") and stack:
                    curr_var = extract_variable(input_lines[i])
                    if stack and stack[-1][0] == curr_var:
                        # Сохраняем индекс соответствующей команды let
                        _, let_index = stack.pop()
                        group_let_indices.append(let_index)
                        i += 1
                    else:
                        break
                # Если группа не пустая, определяем, где надо вставить открывающую фигурную скобку.
                # Берем минимальный индекс из group_let_indices (то есть, первую команду let, вошедшую в группу)
                first_let_index = min(group_let_indices)
                # Вставляем отдельную строку "{" перед этой let-командой
                # Для этого сдвигаем команды: вставляем "{" в result на позиции first_let_index.
                result.insert(first_let_index, "{")
                # Из-за вставки сдвигаем индексы всех последующих строк, поэтому пересчитываем:
                # Если в auto_groups уже есть группа, чьи индексы >= first_let_index, их нужно увеличить на 1.
                for idx in range(len(auto_groups)):
                    open_idx, close_idx = auto_groups[idx]
                    if open_idx >= first_let_index:
                        open_idx += 1
                    if close_idx >= first_let_index:
                        close_idx += 1
                    auto_groups[idx] = (open_idx, close_idx)
                # Теперь добавляем закрывающую фигурную скобку в конец результата
                result.append("}")
                # Запоминаем индексы открывающей и закрывающей скобки для этой группы
                open_index = first_let_index  # только что вставленная "{"
                close_index = len(result) - 1  # только что добавленная "}"
                auto_groups.append((open_index, close_index))
            else:
                # Если drop не соответствует вершине стека, оставляем строку без изменений
                result.append(line)
                # Если переменная присутствует в стеке, удаляем её (она уже освобождена)
                for idx, (v, pos) in enumerate(stack):
                    if v == var:
                        del stack[idx]
                        break
                i += 1
        else:
            # На всякий случай (по условию таких строк быть не должно)
            result.append(line)
            i += 1

    # Если последняя авто-группа является последней областью видимости в программе,
    # то её не следует выводить. То есть, если последняя строка результата — это закрывающая скобка,
    # которая была вставлена автоматически, удаляем её и соответствующую открывающую скобку.
    if auto_groups:
        last_open, last_close = auto_groups[-1]
        if last_close == len(result) - 1:
            # Удаляем закрывающую скобку (последнюю строку)
            del result[last_close]
            # Удаляем открывающую скобку по индексу last_open
            del result[last_open]

    # Вывод результата
    for line in result:
        print(line)


if __name__ == "__main__":
    main()
