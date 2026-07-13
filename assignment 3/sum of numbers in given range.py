# Sum of numbers in a given range

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

total = 0

for i in range(start, end + 1):
    total += i

print("Sum =", total)