money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
month = 0
current_sum = money_capital
current_spend=spend
while True:
    current_sum=current_sum+salary-spend
    spend*=1.05
    if current_sum<=0:
        break
    month+=1
print("Количество месяцев, которое можно протянуть без долгов:", month)
