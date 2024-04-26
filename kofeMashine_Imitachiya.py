class CoffeeMachine:
    def __init__(self):
        self.water = 1000
        self.coffee_beans = 500
        self.milk = 200
        self.sugar = 100
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

    def display_menu(self):
        print("Добро пожаловать!")
        print("Меню напитков:")
        print("1. Эспрессо - 30 рублей")
        print("2. Латте - 50 рублей")
        print("3. Американо - 40 рублей")
        print("4. Капучино - 60 рублей")

    def serve_coffee(self):
        self.display_menu()

        choice = input("Выберите номер напитка (1 - Эспрессо, 2 - Латте, 3 - Американо, 4 - Капучино): ")
        if choice not in ["1", "2", "3", "4"]:
            print("Ошибка: Некорректный выбор.")
            return

        selected_coffee = "espresso" if choice == "1" else "latte" if choice == "2" else "americano" if choice == "3" else "cappuccino"
        price = self.prices[selected_coffee]

        payment_method = input("Выберите способ оплаты (нал/безнал): ")
        if payment_method not in ["нал", "безнал"]:
            print("Ошибка: Некорректный способ оплаты.")
            return

        money_inserted = float(input("Введите сумму денег: "))
        if money_inserted < price:
            print("Ошибка: Недостаточно денег для покупки.")
            return

        sugar = input("Добавить сахар? (да/нет): ")
        
        if sugar not in ["да", "нет"]:
            print("Ошибка: Некорректный ответ.")
            return
        
        self.make_coffee(selected_coffee, money_inserted - price, sugar, payment_method)

    def make_coffee(self, coffee_type, change, sugar, payment_method):
        if coffee_type == "espresso":
            if self.water < 50 or self.coffee_beans < 20:
                print("Ошибка: Недостаточно ингредиентов для приготовления эспрессо.")
                return
            self.water -= 50
            self.coffee_beans -= 20
            print("Эспрессо готов!")
        elif coffee_type == "latte":
            if self.water < 50 or self.coffee_beans < 20 or self.milk < 100:
                print("Ошибка: Недостаточно ингредиентов для приготовления латте.")
                return
            self.water -= 50
            self.coffee_beans -= 20
            self.milk -= 100
            print("Латте готов!")
        elif coffee_type == "americano":
            if self.water < 50 or self.coffee_beans < 20:
                print("Ошибка: Недостаточно ингредиентов для приготовления американо.")
                return
            self.water -= 50
            self.coffee_beans -= 20
            print("Американо готов!")
        elif coffee_type == "cappuccino":
            if self.water < 50 or self.coffee_beans < 20 or self.milk < 100 or self.sugar < 15:
                print("Ошибка: Недостаточно ингредиентов для приготовления капучино.")
                return
            self.water -= 50
            self.coffee_beans -= 20
            self.milk -= 100
            self.sugar -= 15
            print("Капучино готов!")

        if sugar.lower() == "да":
            print("Сахар добавлен.")

        if sugar.lower() == "нет":
            print("Сахар не добавлен.")

        if change > 0:
            print(f"Ваша сдача: {change} рублей.")

        if payment_method == "безнал":
            print("Спасибо за покупку!")
        elif payment_method == "нал":
            print("Спасибо за наличные!")


# Использование кофейной машины
machine = CoffeeMachine()
machine.serve_coffee()