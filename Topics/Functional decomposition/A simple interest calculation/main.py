def calculate(amount, interest_rate, time):
    interest = (amount * interest_rate * time)/100
    total_amount = interest + amount
    return interest, total_amount


def print_result(interest, total_amount):
    print(f"The interest is: {interest}\n"
          f"The total amount is: {total_amount}")
