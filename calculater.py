# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

# Function to display the calculator shape
def display_calculator():
    print("      ")
    print("     _________________")
    print("    |  _____________  |")
    print("    | |             | |")
    print("    | |  Calculator | |")
    print("    | |             | |")
    print("    | |_____________| |")
    print("    | |             | |")
    print("    | |  7   8   9  | |")
    print("    | |  4   5   6  | |")
    print("    | |  1   2   3  | |")
    print("    | |  0   .   +  | |")
    print("    | |  *   -   /  | |")
    print("    | |_____________| |")
    print("    |_________________|\n")
display_calculator()
# Main calculator function

    
print("      Options:\n")

print(" -------------------------------")
print("|*Enter 'add' for addition       |")
print("|*Enter 'subt' for subtraction   |")
print("|*Enter 'mul' for multiplication |")
print("|*Enter 'div' for division       |")
print("|*Enter 'quit' to end the program|")
print("---------------------------------\n") 
def calculator():
    while True:
        user_input = input("Enter Your Choice: ")

        if user_input == "quit":
            break
        elif user_input in ["add", "sub", "mul", "div"]:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if user_input == "add":
                
                print("            Result= ", add(num1, num2))
                
            elif user_input == "sub":
                print("             Result= ", subtract(num1, num2))
            elif user_input == "mul":
                print("             Result= ", multiply(num1, num2))
            elif user_input == "div":
                print("             Result= ", divide(num1, num2))
        else:
            print("Invalid input")

# Call the calculator function to start the program
calculator()
