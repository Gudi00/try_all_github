import math

# Пример данных (X: признаки, y: целевая переменная)
X = [[0.5, 1.5], [1.0, 1.0], [1.5, 0.5], [2.0, 2.0], [2.5, 1.5], [3.0, 3.0]]
y = [0, 0, 0, 1, 1, 1]

# Инициализация коэффициентов
b0 = 0.0
b1 = 0.0
b2 = 0.0
learning_rate = 0.1
epochs = 1000

# Сигмоидальная функция
def sigmoid(z):
    return 1 / (1 + math.exp(-z))

# Обучение модели
for epoch in range(epochs):
    for i in range(len(X)):
        # Линейная комбинация
        z = b0 + b1 * X[i][0] + b2 * X[i][1]
        # Предсказанная вероятность
        pred = sigmoid(z)
        # Ошибка
        error = y[i] - pred
        # Обновление коэффициентов
        b0 += learning_rate * error * pred * (1 - pred)
        b1 += learning_rate * error * pred * (1 - pred) * X[i][0]
        b2 += learning_rate * error * pred * (1 - pred) * X[i][1]

# Вывод коэффициентов
print(f'Коэффициенты: b0 = {b0}, b1 = {b1}, b2 = {b2}')

# Функция предсказания
def predict(x):
    z = b0 + b1 * x[0] + b2 * x[1]
    return sigmoid(z)

# Тестовые данные
X_test = [[1.0, 2.0], [2.0, 1.0]]
predictions = [predict(x) for x in X_test]

# Вывод предсказаний
for i, pred in enumerate(predictions):
    print(f'Предсказание для {X_test[i]}: {pred:.4f}')
