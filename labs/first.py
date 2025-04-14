import numpy as np
from sklearn.datasets import fetch_california_housing, load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Загружаем данные
data = fetch_california_housing()  # Например, используем California House Pricing
X, y = data.data, data.target

# Нормализуем данные
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Разделяем данные на тренировочные и тестовые
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Функция для вычисления стоимости (MSE)
def compute_cost(X, y, theta):
    m = len(y)
    J = (1/(2*m)) * np.sum((X.dot(theta) - y) ** 2)
    return J

# Полный градиентный спуск
def gradient_descent(X, y, theta, alpha, num_iters):
    m = len(y)
    J_history = []

    for i in range(num_iters):
        gradients = (1/m) * X.T.dot(X.dot(theta) - y)
        theta = theta - alpha * gradients
        J_history.append(compute_cost(X, y, theta))

    return theta, J_history

# Стохастический градиентный спуск
def stochastic_gradient_descent(X, y, theta, alpha, num_iters):
    m = len(y)
    J_history = []

    for i in range(num_iters):
        for j in range(m):
            rand_index = np.random.randint(m)
            x_i = X[rand_index, :].reshape(1, X.shape[1])
            y_i = y[rand_index].reshape(1)
            gradients = x_i.T.dot(x_i.dot(theta) - y_i)
            theta = theta - alpha * gradients
        J_history.append(compute_cost(X, y, theta))

    return theta, J_history

# Батчевый градиентный спуск
def batch_gradient_descent(X, y, theta, alpha, num_iters, batch_size):
    m = len(y)
    J_history = []

    for i in range(num_iters):
        indices = np.random.permutation(m)
        X_shuffled = X[indices]
        y_shuffled = y[indices]

        for j in range(0, m, batch_size):
            X_batch = X_shuffled[j:j+batch_size]
            y_batch = y_shuffled[j:j+batch_size]
            gradients = (1/batch_size) * X_batch.T.dot(X_batch.dot(theta) - y_batch)
            theta = theta - alpha * gradients
        J_history.append(compute_cost(X, y, theta))

    return theta, J_history

# Начальные параметры
alpha = 0.01
num_iters = 1000
theta = np.random.randn(X_train.shape[1])

# Применяем алгоритмы
theta_gd, J_history_gd = gradient_descent(X_train, y_train, theta, alpha, num_iters)
theta_sgd, J_history_sgd = stochastic_gradient_descent(X_train, y_train, theta, alpha, num_iters)
theta_bgd, J_history_bgd = batch_gradient_descent(X_train, y_train, theta, alpha, num_iters, batch_size=32)

# Визуализируем результаты
plt.figure(figsize=(12, 8))
plt.plot(J_history_gd, label='Полный Градиентный Спуск')
plt.plot(J_history_sgd, label='Стохастический Градиентный Спуск')
plt.plot(J_history_bgd, label='Батчевый Градиентный Спуск')
plt.xlabel('Количество итераций')
plt.ylabel('Значение функции потерь (MSE)')
plt.legend()
plt.show()
