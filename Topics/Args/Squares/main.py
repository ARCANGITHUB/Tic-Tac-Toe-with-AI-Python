def sq_sum(*nums):
    total = 0
    for num in nums:
        num *= num
        total += num

    return total


# print(sq_sum(1, 10, 10))
