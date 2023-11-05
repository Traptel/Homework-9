import random

int_elements = [random.randint(1, 500) for _ in range(25)]

print("Початковий список:", int_elements, sep="\n")
print("Список, що складається із квадратів int_elements:",
      [x ** 2 for x in int_elements], sep="\n")
print("Список з остач ділення на 11 елементів int_elements:",
      [x % 11 for x in int_elements], sep="\n")
print("Список лише з парних елементів int_elements:",
      [x for x in int_elements if x % 2 == 0], sep="\n")
print("Список з елементів int_elements з непарною кількістю цифр:",
      [x for x in int_elements if len(str(x)) % 2 != 0], sep="\n")
print("Список з елементів int_elements, які не є кратними 3:",
      [x for x in int_elements if x % 3 != 0], sep="\n")
