def calculate_factorial(number: int) -> int:
    if number == 1:
        return 1
    else:
        return number * calculate_factorial(number - 1)

def calculate_unique_birthday_probability(n):
    days_in_a_year = 365
    unique_birthdays = calculate_factorial(days_in_a_year) / calculate_factorial(days_in_a_year - n)
    possible_birthday_choices = days_in_a_year ** n 
    probability = unique_birthdays / possible_birthday_choices
    return probability


if __name__=="__main__":
    n = 2
    unique_birthday_probability = calculate_unique_birthday_probability(n)
    share_birthday_probability = 1 - unique_birthday_probability
    print(f"If there are {n} people in a room")
    print(f"\t\t\t\tProbablity of nobody shares a birthday is {unique_birthday_probability:.2%}")
    print(f"\t\t\t\tProbablity of at least two people with shared birthday is {share_birthday_probability:.2%}")
    print()
    
    while (unique_birthday_probability > 0.5):
        n += 1
        unique_birthday_probability = calculate_unique_birthday_probability(n)
        share_birthday_probability = 1 - unique_birthday_probability
        print(f"If there are {n} people in a room")
        print(f"\t\t\t\tProbablity of nobody shares a birthday is {unique_birthday_probability:.2%}")
        print(f"\t\t\t\tProbablity of at least two people with shared birthday is {share_birthday_probability:.2%}")
        print()