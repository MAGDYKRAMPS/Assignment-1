def can_vote(birth_year, current_year):
    age = current_year - birth_year
    if age >= 18:
        return True
    else:
        return False


# Test the function
test_cases = [1990, 2023]    

birth_year = int(input("Enter your birth year:"))
current_year = int(input("Enter the current year:"))

if can_vote(birth_year, current_year):
    print("You are old enough to vote!")
else:
    print("You are not old enough to vote yet.")
