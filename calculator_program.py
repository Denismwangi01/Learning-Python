# Display menu for the user
print("Welcome to the Calculator")
print("Choose an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

# Take user input
choice = input("Enter the number of your choice (1/2/3/4): ")

# Validate user input
if choice not in ['1', '2', '3', '4']:
    print("Invalid choice. Please restart the program.")
else:
    # Get numbers from the user
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")

    # Convert inputs to float
    num1 = float(num1)
    num2 = float(num2)

    # Perform the operation
    if choice == '1':
        result = num1 + num2
        operation = "Addition"
    elif choice == '2':
        result = num1 - num2
        operation = "Subtraction"
    elif choice == '3':
        result = num1 * num2
        operation = "Multiplication"
    elif choice == '4':
        # Handle division by zero
        if num2 == 0:
            result = "undefined (division by zero)"
        else:
            result = num1 / num2
        operation = "Division"

    # Display the result
    print(f"The result of {operation} is: {result}")
