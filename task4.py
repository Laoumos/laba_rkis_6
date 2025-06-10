# Задание 4. Дана целочисленная последовательность, содержащая как положительные, так
# и отрицательные числа. Вывести ее первый положительный элемент и последний
# отрицательный элемент;

import random

line = [random.randint(-10, 10) for i in range(1, 10)]
first_positive = line[0]
last_negative = line[0]

for i in range(len(line)):
    if line[i] < 0:
        last_negative = line[i]

for i in range(len(line)):
    if line[i] > 0:
        first_positive = line[i]
        break

print(line)
print(first_positive)
print(last_negative)
