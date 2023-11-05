import random

random_numbers = set(random.randint(1, 100) for _ in range(15))
sum_odd = sum(x for x in random_numbers if x % 2 != 0)
sum_even = sum(x for x in random_numbers if x % 2 == 0)
print(random_numbers)

if sum_odd > sum_even:
    print("Так, сумма непарних чисел у множині більша за суму парних чисел")
else:
    print("Ні, сумма непарних чисел у множині не більша за суму парних чисел")
