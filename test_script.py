import math
from time import sleep


radius = float(input("Input radius of circle in cm: "))
area = math.pi * radius * radius

print(f"The area of a cirlce with radius {radius} is {area}")
sleep(2)
print("Goodbye")