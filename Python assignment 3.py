def is_right_triangle(a, b, c):
    sides = [a, b, c]
    sides.sort()
    return sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2

a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

if a + b > c and a + c > b and b + c > a:
    print("The sides form a triangle.")

    if is_right_triangle(a, b, c):
        print("It is a right triangle.")
    else:
        print("It is not a right triangle.")
else:
    print("The given sides do not form a triangle.")