<<<<<<< HEAD
# Calculate the area of a circle
import math

def calculate_area_circle(radius):
    area = math.pi * radius ** 2
    return area

# Test the function
radius = input("Enter the radius of the circle: ")
area = calculate_area_circle(radius)
print("The area of the circle is:", area)