salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
current_spend = spend
money_capital = 0
current_month = 1
while current_month <= months:
    money_capital = money_capital+current_spend-salary
    current_spend *= (1+increase)
    current_month += 1
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов: " + str(round(money_capital)))
