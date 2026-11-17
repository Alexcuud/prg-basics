###
# A program that calculates the volume
# and surface area of ​​a cuboid with sides a, b, and c.
# Read the dimensions of the cuboid from the keyboard.
#
a = input('a=')
b = input('b=')
c = input('c=')
int_a = int(a)
int_b = int(b)
int_c = int(c)
volume = int_a * int_b * int_c
surface_area = 2 * (int_a*int_b + int_a*int_c + int_b*int_c)
print(f'The volume of a cuboid with sides {a}, {b}, and {c} is {volume}')