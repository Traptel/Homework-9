import random

n = int(input("Введіть розмір матриці n: "))
matrix = [[random.randint(1, 100) for _ in range(n)] for _ in range(n)]

for row in matrix:
    print(row)

sum_diagonal = sum(matrix[i][i] for i in range(n))
print(f"Сума чисел по діагоналі: {sum_diagonal}")
sum_last_column = sum(matrix[i][-1] for i in range(n))
print(f"Сума чисел останнього стовбця: {sum_last_column}")
