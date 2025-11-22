# Вдосконалений калькулятор з циклом

while True:
    a = float(input("Введіть перше число: "))
    b = float(input("Введіть друге число: "))

    print("Оберіть операцію:")
    print("1 - додавання")
    print("2 - віднімання")
    print("3 - множення")
    print("4 - ділення")

    choice = input("Ваш вибір (1/2/3/4): ")

    if choice == "1":
        print("Результат:", a + b)
    elif choice == "2":
        print("Результат:", a - b)
    elif choice == "3":
        print("Результат:", a * b)
    elif choice == "4":
        if b != 0:
            print("Результат:", a / b)
        else:
            print("Помилка: ділення на нуль!")
    else:
        print("Невірна операція")

    # Запит чи продовжити
    again = input("Бажаєте зробити ще одну операцію? (так/ні): ").lower()

    if again != "так":
        print("Дякую за використання калькулятора!")
        break
