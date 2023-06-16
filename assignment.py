def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True  # Divisible by 400: Leap year
            else:
                return False  # Divisible by 100 but not by 400: Not a leap year
        else:
            return True  # Divisible by 4 but not by 100: Leap year
    else:
        return False  # Not divisible by 4: Not a leap year


# Test the function with different years
test_years = [2000, 2020, 2021, 1900, 2004]

for year in test_years:
    if is_leap_year(year):
        print(year, "is a leap year.")
    else:
        print(year, "is not a leap year.")
