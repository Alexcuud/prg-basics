circumference = int(input("Enter the circumference in cm: "))
diameter = circumference / (2 * 3.14)
diameter_ok = diameter>= 50
print(f'Diameter is greater than or equal to 50 cm: {diameter_ok}')