cards = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
         '9': 9, '10': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}
count = 0
total = 0
while count < 6:

    user = input()
    count += 1

    if user in cards:
        total += (cards[user])
    else:
        count -= 1
        # break

print(total/count)
