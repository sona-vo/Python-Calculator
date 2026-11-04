def calculation(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        return a / b
    else:
        raise ValueError("Invalid operator")

while True:

    print("\n===== PYTHON CALCULATOR =====")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")

    try:

        choice = int(input("Enter your choice: "))
        if choice == 5:
            print("Thank you for using calculator!")
            break
        if choice not in [1, 2, 3, 4]:
            print("Invalid choice! Please select 1 to 5.")
            continue
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if choice == 1:
            operator = '+'
        elif choice == 2:
            operator = '-'
        elif choice == 3:
            operator = '*'
        elif choice == 4:
            operator = '/'
        result = calculation(num1, num2, operator)
        print("Result:", result)

    except ValueError:
        print("Error! Please enter valid numbers.")
    except ZeroDivisionError:
        print("Error! Cannot divide by zero.")
    except Exception as e:
        print("Unexpected error:", e)