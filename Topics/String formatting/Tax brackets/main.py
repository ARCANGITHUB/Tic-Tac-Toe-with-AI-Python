sample = int(input())
total = 0

if 0 <= sample <= 15527:
    tax = 0
    percentage = "0%"
    calculated_tax = sample * tax
    total += calculated_tax
    print(f"The tax for {sample} is {percentage}. That is {total:.0f} dollars!")
elif 15528 <= sample <= 42707:
    tax = 0.15
    percentage = "15%"
    calculated_tax = sample * tax
    total += calculated_tax
    print(f"The tax for {sample} is {percentage}. That is {total:.0f} dollars!")
elif 42708 <= sample <= 132406:
    tax = 0.25
    percentage = "25%"
    calculated_tax = sample * tax
    total += calculated_tax
    print(f"The tax for {sample} is {percentage}. That is {total:.0f} dollars!")
elif sample >= 132407:
    tax = 0.28
    percentage = "28%"
    calculated_tax = sample * tax
    total += calculated_tax
    print(f"The tax for {sample} is {percentage}. That is {total:.0f} dollars!")
