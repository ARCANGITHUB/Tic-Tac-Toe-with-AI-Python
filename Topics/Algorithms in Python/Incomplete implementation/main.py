def startswith_capital_counter(names):
    counter = 0
    for name in str(names):
        if name.istitle():
            counter += 1

    return counter
