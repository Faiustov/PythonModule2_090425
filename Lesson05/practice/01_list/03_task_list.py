# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -10 до 10.
# Вывести на экран сумму всех элементов.

numbers = [6, -4, 3, 8, 2, 0, 7]
# Вариант-1
total = 0
for number in numbers:
    total += number

# Вариант-2
total = sum(numbers)

print(total)