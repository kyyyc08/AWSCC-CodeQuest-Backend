from circle_area import calculate_area

print("\n===== Find the Area of a Circle =====")

radius = float(input("Enter the radius of the circle: "))
area = calculate_area(radius)

print("The area of the circle with radius", radius, "is:", area, "\n")