num = int(input("Enter a number: "))

# Find last digit
last_digit = num % 10

# Find first digit
while num >= 10:
    num //= 10
first_digit = num

# Sum of first and last digit
sum_digits = first_digit + last_digit

print("Sum of first and last digit:", sum_digits)