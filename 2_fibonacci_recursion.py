number = int(input("Enter a number to print its Fibonacci: "))

def fibonacci(first, second, iteration):
    if (iteration > 2):
        return str(first + second) + " " + fibonacci(second, (first + second), iteration - 1)
    return ""

fibonacci_series = ""
if number > 0:
    fibonacci_series += "0 "
if number > 1:
    fibonacci_series += "1 "
if (number > 2):
    fibonacci_series += str(fibonacci(0, 1, number)).strip()

print("The first " + str(number) + " fibonacci numbers are: " + fibonacci_series + ".")