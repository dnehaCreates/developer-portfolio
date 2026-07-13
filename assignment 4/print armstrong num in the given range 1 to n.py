# Print Armstrong numbers from 1 to n using nested loops

n = int(input("Enter the value of n: "))

for num in range(1, n + 1):
    temp = num
    digits = 0

    # Count number of digits (nested loop)
    while temp > 0:
        digits += 1
        temp //= 10

    temp = num
    sum = 0

    # Calculate Armstrong sum (nested loop)
    while temp > 0:
        digit = temp % 10
        power = 1

        for i in range(digits):   # nested loop for power calculation
            power *= digit

        sum += power
        temp //= 10

    # Check Armstrong number
    if sum == num:
        print(num)