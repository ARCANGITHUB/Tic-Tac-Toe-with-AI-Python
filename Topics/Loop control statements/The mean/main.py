number = 0
sum1 = 0
q = 0


while True:
    number = input()
    if number == ".":
        break
    sum1 += int(number)
    q += 1

print(sum1/q)
