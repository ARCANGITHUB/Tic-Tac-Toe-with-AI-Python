name = input()


def normalize(name):
    for char in name:
        if char == "é":
            new_name = name.replace("é", "e")
        elif char == "ë":
            new_name = name.replace("ë", "e")
        elif char == "á":
            new_name = name.replace("á", "a")
        elif char == "å":
            new_name = name.replace("å", "aa")
        elif char == "œ":
            new_name = name.replace("œ", "oe")
        elif char == "æ":
            new_name = name.replace("æ", "ae")

    return new_name


print(normalize(name))
