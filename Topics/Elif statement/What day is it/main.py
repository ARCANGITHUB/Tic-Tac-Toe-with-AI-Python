utc = int(input())
start = 0

if utc < -10:
    print("Monday")
elif -10 <= utc <= 13:
    print("Tuesday")
elif utc > 13:
    print("Wednesday")
