number = int(input("Enter a number to get its factorial: "))

factorial = 1
for i in range(1, number + 1):
    factorial *= i

print("factorial of " + str(number) + " is: " + str(factorial))