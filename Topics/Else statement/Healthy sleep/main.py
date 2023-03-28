a = int(input())
b = int(input())
h = int(input())

if h < a:
    print("Deficiency")

if h > b:
    print("Excess")
else:
    if a <= h <= b:
        print("Normal")
