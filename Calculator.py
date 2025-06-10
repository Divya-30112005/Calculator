def calculator():
    print("Welcome to the Python Console Calculator!")
    print("Enter a mathematical expression using +, -, *, /, %")
    print("Type 'exit' to quit.")

    while True:
        user_input = input(">> ")

        if user_input.lower() == 'exit':
            print("Goodbye!")
            break

        # Filter input to allow only numbers and operators
        allowed_chars = "0123456789+-*/%.() "
        if all(char in allowed_chars for char in user_input):
            try:
                result = eval(user_input)
                print("= ", result)
            except ZeroDivisionError:
                print("Error: Division by zero.")
            except Exception as e:
                print("Invalid expression. Error:", e)
        else:
            print("Invalid characters detected. Please use only digits and operators.")

# Run the calculator
if __name__ == "__main__":
    calculator()
