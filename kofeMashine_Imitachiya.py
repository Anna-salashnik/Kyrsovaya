class CoffeeMachine:
    def __init__(self):
        # Инициализация ингредиентов и цен
        self.ingredients = {
            "water": 1000,
            "coffee_beans": 500,
            "milk": 200,
            "sugar": 100,
        }
        self.prices = {
            "espresso": 30,
            "latte": 50,
            "americano": 40,
            "cappuccino": 60,
        }
        
        print("Рецепты кофе:")
        print("Эспрессо: 50 мл воды, 20 г кофейных зерен")
        print("Латте: 50 мл воды, 20 г кофейных зерен, 100 мл молока")
        print("Американо: 50 мл воды, 20 г кофейных зерен")
        print("Капучино: 50 мл воды, 20 г кофейных зерен, 100 мл молока, 15 г сахара")
        
        # Вывод меню
        print("Меню напитков:")
        for coffee, price in self.prices.items():
            print(f"{coffee}: {price} рублей")

    def serve_coffee(self):
        # Выбор и проверка напитка
        coffee = input("Выберите напиток (espresso, latte, americano, cappuccino): ")
        if coffee not in self.prices:
            print("Неправильный выбор напитка.")
            return

        # Выбор способа оплаты
        payment_method = input("Выберите способ оплаты (нал/безнал): ")
        if payment_method not in ["нал", "безнал"]:
            print("Неправильный способ оплаты.")
            return

        # Оплата и выдача сдачи
        money_inserted = float(input("Введите сумму денег: "))
        if money_inserted < self.prices[coffee]:
            print("Недостаточно денег.")
            return
        change = money_inserted - self.prices[coffee]

        # Добавление сахара
        sugar = input("Добавить сахар? (да/нет): ")
        if sugar not in ["да", "нет"]:
            print("Неправильный ответ.")
            return
        # Приготовление кофе
        self.make_coffee(coffee, sugar, payment_method)

        # Выдача кофе и сдачи
        print(f"{coffee} готов!")
        if sugar == "да":
            print("Сахар добавлен.")
        if change > 0:
            print(f"Ваша сдача: {change} рублей.")
        if payment_method == "безнал":
            print("Спасибо за покупку!")
        elif payment_method == "нал":
            print("Спасибо за наличные!")

    def make_coffee(self, coffee, sugar, payment_method):
        # Проверка наличия ингредиентов
        ingredients_needed = {
            "espresso": {"water": 50, "coffee_beans": 20},
            "latte": {"water": 50, "coffee_beans": 20, "milk": 100},
            "americano": {"water": 50, "coffee_beans": 20},
            "cappuccino": {"water": 50, "coffee_beans": 20, "milk": 100, "sugar": 15},
        }
        for ingredient, amount in ingredients_needed[coffee].items():
            if self.ingredients[ingredient] < amount:
                print("Недостаточно ингредиентов.")
                return

        # Приготовление кофе
        for ingredient, amount in ingredients_needed[coffee].items():
            self.ingredients[ingredient] -= amount


# Использование кофейной машины
machine = CoffeeMachine()
machine.serve_coffee()
