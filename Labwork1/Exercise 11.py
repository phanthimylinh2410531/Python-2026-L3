# Compute the distance between 2 points

x1 = float(input("x1 = "))
x2 = float(input("x2 = "))
y1 = float(input("y1 = "))
y2 = float(input("y2 = "))

distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

print("The distance between (",x1,", ",y1,") and (",x2,", ",y2,") is", distance)