deposit = int(input())
years = 0

while deposit < 700000:
    deposit += (deposit * 0.071)
    # print(deposit)
    years += 1


print(years)
