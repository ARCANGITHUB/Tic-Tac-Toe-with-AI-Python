
n = 0
e = 0
s = 0

while True:
    n = int(input())
    e += n
    s += n**2
    if e == 0:
        break

print(s)
