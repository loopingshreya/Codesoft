def calculator():
    while True:
        print("\n=== Simple Calculator ===")
        print("1 - Add")
        print("2 - Subtract")
        print("3 - Multiply")
        print("4 - Divide")
        print("5 - Exit")

        try:
            option = int(input("Choose an operation (1-5): "))

            if option == 5:
                print("Exiting... Goodbye!")
                break

            if option not in [1, 2, 3, 4]:
                print("Invalid option! Please choose between 1 and 5.")
                continue

            # Take input numbers
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            # Perform operation
            if option == 1:
                result = num1 + num2
            elif option == 2:
                result = num1 - num2
            elif option == 3:
                result = num1 * num2
            elif option == 4:
                if num2 == 0:
                    print("Error: Division by zero is not allowed.")
                    continue
                result = num1 / num2

            print("The result of the operation is: {}".format(result))

        except ValueError:
            print("Invalid input! Please enter numeric values.")
calculator()