start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

print("Even numbers:")
for i in range(start, end + 1):
    if i % 2 == 0:
        print(i, end=" ")

print("\nOdd numbers:")
for i in range(start, end + 1):
    if i % 2 != 0:
        print(i, end=" ")