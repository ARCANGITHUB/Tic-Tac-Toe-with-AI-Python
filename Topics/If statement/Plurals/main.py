number = int(input())
word = input()

# write a condition for plurals

if number > 1 or number == 0:
    print(number, word + "s")

if number == 1:
    print(number, word)
