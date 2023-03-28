sentence = input()


def aver(sent):

    for sym in [',', '!', '?', ';', '.', '"', "'"]:
        sent = sent.replace(sym, '')

    words = sent.split()

    total = 0
    for word in words:
        total += len(word)
        result = total / len(words)

    return result


print(aver(sentence))
