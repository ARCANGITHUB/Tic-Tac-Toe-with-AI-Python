def average_mark(*marks):
    total = 0
    for mark in marks:
        total += mark

    result = round(total/len(marks), 1)
    # print(round(total/len(marks), 1))
    return result
