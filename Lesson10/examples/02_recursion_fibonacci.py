def fibonacci(n):
    """
    Вычисляет n-ое число Фибоначчи.

    Числа Фибоначчи - это последовательность, в которой каждое число является
    суммой двух предыдущих чисел.

    Например:
    0, 1, 1, 2, 3, 5, 8, 13, ...
    """

    # Базовый случай: первые два числа Фибоначчи
    if n <= 1:
        return n
    # Рекурсивный случай: n-ое число Фибоначчи - это сумма двух предыдущих чисел
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Пример использования
print(fibonacci(7))  # Вывод: 13