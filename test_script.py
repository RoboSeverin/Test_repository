import math
from time import sleep

def calculate_area_cli():
    radius = float(input("Input radius of circle in cm: "))
    area = math.pi * radius * radius

    print(f"The area of a cirlce with radius {radius} is {area}")

def proceed_prompt():
    proceed_bool : bool = False
    proceed_str = input("Want to continue? y/n\n")
    if proceed_str == "y" or proceed_str == "Y":
        proceed_bool = True
    return proceed_bool


calculate_area_cli()
proceed = proceed_prompt()

while proceed:
    calculate_area_cli()
    proceed = proceed_prompt()

