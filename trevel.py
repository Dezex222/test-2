# Запит даних у користувача
distance = float(input("Введіть відстань до міста (км): "))
speed = float(input("Введіть середню швидкість автомобіля (км/год): "))
fuel_price = float(input("Введіть вартість 1 літра бензину (грн): "))
fuel_consumption = float(input("Введіть витрату бензину на 100 км (л): "))

# Розрахунки
time = distance / speed
fuel_needed = (distance / 100) * fuel_consumption
trip_cost = fuel_needed * fuel_price

# Виведення результатів
print("\n--- Результати поїздки ---")
print("Час у дорозі:", round(time, 2), "год")
print("Потрібно бензину:", round(fuel_needed, 2), "л")
print("Вартість поїздки:", round(trip_cost, 2), "грн")
