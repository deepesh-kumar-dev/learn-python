number = int(input("Enter a number to print its Fibonacci: "))

fibonacci_series = ""
if number > 0:
    first = 0
    fibonacci_series += str(first)
    if number > 1:
        second = 1
        fibonacci_series += " " + str(second)
        for i in range(2, number):
            current = first + second
            first = second
            second = current
            fibonacci_series += " " + str(current)

print("The first " + str(number) + " fibonacci numbers are: " + str(fibonacci_series).strip() + ".")