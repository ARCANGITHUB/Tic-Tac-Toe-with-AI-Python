groups = ['1A', '1B', '1C', '2A', '2B', '2C', '3A', '3B', '3C']

kindergarten = {}

kindergarten = dict.fromkeys(groups)

n_groups = int(input())
count = 0
items = 0

while count < n_groups:
    count += 1
    for item in kindergarten:
        items += 1
        if items <= n_groups:
            children = int(input())
            kindergarten[item] = children
            pass
        else:
            break

print(kindergarten)
