def is_year_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

chosen_year = 2009

leap_year_result = is_year_leap(chosen_year)

print(f"Год {chosen_year}: {leap_year_result}")