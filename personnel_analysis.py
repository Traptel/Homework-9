data = [
 {"name": "Alisa", "country": "UA", "item": "socks", "price": 15},
 {"name": "Alisa", "country": "UA", "item": "socks", "price": 25},
 {"name": "Ben", "country": "US", "item": "pencil", "price": 95},
 {"name": "Alisa", "country": "UA", "item": "pencil", "price": 45},
 {"name": "Oleg", "country": "GB", "item": "socks", "price": 100},
 {"name": "Ben", "country": "US", "item": "pencil", "price": 10}
]

workers = {data[i]['name'] for i in range(len(data))}
print(workers)
worker_suma = {}

for worker in data:
    name = worker["name"]
    price = worker["price"]
    if name in worker_suma:
        worker_suma[name] += price
    else:
        worker_suma[name] = price

print("Словник із сумою виторгу за тиждень:", worker_suma, sep="\n")
