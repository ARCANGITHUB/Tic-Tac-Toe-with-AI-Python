string = "red yellow fox bite orange goose beeeeeeeeeeep"
vowels = 'aeiou'
number = 0

for char in string:
    for vowel in vowels:
        if vowel == char:
            number += 1

print(number)
