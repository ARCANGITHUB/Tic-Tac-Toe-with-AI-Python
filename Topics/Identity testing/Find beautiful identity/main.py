def object_with_beautiful_identity():
    for i in range(10_000):
        # Change the next line
        if id(i) % 1000 == 888:
            # print(id(i))
            return i


# print(object_with_beautiful_identity())
