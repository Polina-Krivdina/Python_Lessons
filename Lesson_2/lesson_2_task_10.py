def bank(X, Y):
    interest_rate = 0.1
    total_amount = X

    for _ in range(Y):
        total_amount += total_amount * interest_rate

    return total_amount

initial_deposit = 10000
years = 60

result = bank(initial_deposit, years)
print(f"Сумма на счету спустя {years} лет: {result:.2f} рублей")