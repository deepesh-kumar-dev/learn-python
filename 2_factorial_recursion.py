number = int(input("Enter a number to get its factorial: "))

def factorial(number):
    if number > 1:
        return number * factorial(number - 1)
    return 1

print("factorial of " + str(number) + " is: " + str(factorial(number)))