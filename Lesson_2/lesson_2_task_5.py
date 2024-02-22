def month_to_season(month) :
    if month in [1, 2, 12]:
        return "Winter"
    elif month in [3, 4, 5]:
        return "Spring"
    elif month in [6, 7, 8]:
        return "Summer"
    elif month in [9,10, 11]:
        return "Autumn"
    else :
        "Uncorrected"

month_number = 12
result = month_to_season(month_number)
print (f'Month {month_number} corresponds to the season: {result}')