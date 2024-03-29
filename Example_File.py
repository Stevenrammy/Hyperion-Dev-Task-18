 Adding-comments-and-unit-information
""" This program calculates the area of a circle in cm squared"""

 master
# Calculate the area of a circle
import math

def calculate_area_circle(radius):
    area = math.pi * radius ** 2
    return area

# Test the function
Adding-comments-and-unit-information
radius_str = input("Enter the radius of the circle (in cm): ") # Asked for unit (cm)
try:
    radius = float(radius_str)
    area = calculate_area_circle(radius)
    print("The area of the circle is: {:.2f} cm squared.".format(area)) # Rounded to 2 decimals and provided unit
except ValueError:
    print("Please enter a valid number for the radius.")
    

radius_str = input("Enter the radius of the circle: ")
try:
    radius = float(radius_str)
    area = calculate_area_circle(radius)
    print("The area of the circle is:", area)
except ValueError:
    print("Please enter a valid number for the radius.")
master
