dictionary = ['all', 'an', 'and', 'as', 'closely', 'correct', 'equivocal',
              'examine', 'indication', 'is', 'means', 'minutely', 'or', 'scrutinize',
              'sign', 'the', 'to', 'uncertain']

sentence = input()
sentence = sentence.split()
words = 0

for word in sentence:
    if word not in dictionary:
        print(word)
    elif word in dictionary:
        words += 1
        if words == len(sentence):
            print("OK")
