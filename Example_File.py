# Calculate the area of a circle
import math

def calculate_area_circle(radius):
    area = math.pi * radius ** 2
    return area

# Test the function
radius_str = input("Enter the radius of the circle: ")
try:
    radius = float(radius_str)
    area = calculate_area_circle(radius)
    print("The area of the circle is:", area)
except ValueError:
    print("Please enter a valid number for the radius.")
