# put your python code here
def multiply(a, *args):
    total = a * 1
    for n in args:
        total *= n

    return total


# print(multiply(14))
