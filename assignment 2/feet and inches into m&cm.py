# Convert feet and inches to meters and centimeters

# Input
feet = int(input("Enter feet: "))
inches = int(input("Enter inches: "))

total_inches = (feet * 12) + inches

# Convert inches to centimeters (1 inch = 2.54 cm)
centimeters = total_inches * 2.54

# Convert cm to meters and remaining cm
meters = int(centimeters // 100)
remaining_cm = centimeters % 100

