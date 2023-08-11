import numpy as np
import time
import matplotlib.pyplot as plt


# функция для умножения матрицы на ее транспонированную
def multiply_matrix_by_transpose(matrix):
    # определяем количество строк и столбцов матрицы
    rows, cols = matrix.shape

    # создаем новую матрицу для результатов
    result = np.zeros((rows, rows))

    # перебираем все элементы новой матрицы
    for i in range(rows):
        for j in range(rows):
            # вычисляем соответствующий элемент произведения
            result[i, j] = sum(matrix[i, k] * matrix[j, k] for k in range(cols))

    return result


# задаем размеры матриц для проверки
sizes = range(200,201)
repeats = 10
# замеряем время умножения для каждой матрицы
times = []
for n in sizes:
    # генерируем матрицу случайных целых чисел в заданном диапазоне
    matrix = np.random.randint(0, 10, size=(n, n))

    print("Основная матрица:")
    print(matrix)

    # выводим транспонированную матрицу
    transpose_matrix = matrix.transpose()
    print("Транспонированная матрица:")
    print(transpose_matrix)


    # выполняем умножение матриц
    result = multiply_matrix_by_transpose(matrix)

    # выводим результат
    print("Результат умножения:")
    print(result)


    # замеряем время умножения
    start_time = time.time()
    result = multiply_matrix_by_transpose(matrix)
    end_time = time.time()
    times.append(end_time - start_time)

    # выводим информацию о размере матрицы и времени умножения
    if n > 20:
        print(f"Для матрицы размера {n}x{n} время умножения: {times[-1]:.6f} сек")
    else:
        print(f"Для матрицы размера {n}x{n}:\n{result}\n")

# строим график временных затрат через точки, соединенных линиями
plt.figure(figsize=(10, 6))

plt.plot(sizes, times, linestyle='-', marker='o')

# задаем параметры графика
plt.title('Время умножения матрицы на ее транспонированную')
plt.xlabel('Размер матрицы')
plt.ylabel('Время выполнения, сек')
plt.grid(True)

# устанавливаем размер шрифта для меток на осях
plt.tick_params(axis='both', which='major', labelsize=12)

plt.show()