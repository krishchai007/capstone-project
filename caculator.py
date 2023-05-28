# Calculator program

# Function to add two numbers
def add(a, b):
    return a + b

# Function to subtract two numbers
def subtract(a, b):
    return a - b

# Function to multiply two numbers
def multiply(a, b):
    return a * b

# Main program
print("Welcome to the Calculator Program!")

while True:
    print("Select an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Exit")

    choice = int(input("Enter your choice (1-4): "))

    if choice == 4:
        print("Exiting the program...")
        break

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if choice == 1:
        result = add(num1, num2)
        print("Result: ", result)
    elif choice == 2:
        result = subtract(num1, num2)
        print("Result: ", result)
    elif choice == 3:
        result = multiply(num1, num2)
        print("Result: ", result)
        if result:
            print("Result: ", result)

    print("--------------------")
