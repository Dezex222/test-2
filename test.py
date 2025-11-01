# 1. Зберігаємо ціни товарів у змінних
apple_price = 12
banana_price = 25
orange_price = 30

# 2. Запитуємо скільки кожного товару хоче купити користувач
apples = int(input("Скільки яблук ви хочете купити?" ))
bananas = int(input("Скільки бананів ви хочете купити?" ))
oranges = int(input("Скільки апельсинів ви хочете купити? "))

# 3. Обчислюємо загальну вартість покупки
total = apples * apple_price + bananas * banana_price + oranges * orange_price

# 4. Виводимо результат
print("Загальна вартість покупки:", total,)

# 5. Порахуємо окремо яблука, банани, апельсини 
apple_total = apples * apple_price
banana_total = bananas * banana_price
orange_total = oranges * orange_price

# 6. Виводимо результати
print("Вартість яблук:" , apple_total)
print("Вартість бананів:" ,banana_total)
print("Вартість апельсинів:" , orange_total)
