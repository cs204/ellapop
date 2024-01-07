def coffee_machine():
    coffee_cost = 50
    total_amount = 0

    while total_amount < coffee_cost:
        print(f"Нужная сумма: {coffee_cost - total_amount}")

        coin = input("Вставьте монету: ")

        if coin in ["50", "20", "10", "5"]:
            total_amount += int(coin)

    change_owed = total_amount - coffee_cost
    print(f"Ваша сдача: {change_owed}")

coffee_machine()