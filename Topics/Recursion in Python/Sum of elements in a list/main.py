def list_sum(some_list):
    sum = 0
    if some_list == []:
        return 0
    # base case
    elif len(some_list) == 1:
        return some_list[0]
    # recursive case
    else:
        for i in some_list:
            sum = sum + i
        return sum
