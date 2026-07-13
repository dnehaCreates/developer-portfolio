n = int(input("Enter range (n): "))

print("Perfect numbers between 1 and", n, "are:")

for num in range(1, n + 1):
    sum_div = 0

    for i in range(1, num):
        if num % i == 0:
            sum_div += i

    if sum_div == num:
        print(num)