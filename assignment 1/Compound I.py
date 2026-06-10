# Program to calculate Compound Interest

P = float(input("Enter Principal Amount: "))
R = float(input("Enter Annual Interest Rate (%): "))
T = float(input("Enter Time (in years): "))

A = P * (1 + R / 100) ** T
CI = A - P

print("Compound Interest =", CI)
print("Total Amount =", A)