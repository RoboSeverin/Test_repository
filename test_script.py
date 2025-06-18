import math
from time import sleep

def calculate_area_cli():
    radius = float(input("Input radius of circle in cm: "))
    area = math.pi * radius * radius

    print(f"The area of a cirlce with radius {radius} is {area}")

calculate_area_cli()
