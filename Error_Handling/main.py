# errors_handling
numbers = [10, 0, "a", 25]

# TypeError/ZeroDivisionError

for number in numbers:
    try:
        print(100 / number)
    except TypeError:
        print(f"Error: Invalid value '{number}' - not an integer")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
