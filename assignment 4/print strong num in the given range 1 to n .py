# Print strong numbers in the range 1 to n

import math

n = int(input("Enter the range: "))

for num in range(1, n + 1):
    temp = num
    sum_fact = 0

    while temp > 0:
        digit = temp % 10
        sum_fact += math.factorial(digit)
        temp //= 10

    if sum_fact == num:
        print(num)