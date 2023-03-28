# BOX DIMENSIONS
a = int(input())
b = int(input())
c = int(input())
# DOORWAY DIMENSIONS
x = int(input())
y = int(input())

doorway = x * y
box1 = a * b
box2 = a * c
box3 = b * c

if doorway > box1:
    print("The box can be carried")
elif doorway > box2:
    print("The box can be carried")
elif doorway > box3:
    print("The box can be carried")
else:
    print("The box cannot be carried")
