# add_two_numbers.py

# Function to add two numbers
def add_numbers(num1, num2):
    return num1 + num2


if __name__ == "__main__":
    try:
        # Input from the user
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        # Add the numbers
        result = add_numbers(num1, num2)

        # Print the result
        print(f"The result of adding {num1} and {num2} is: {result}")
    except ValueError:
        print("Invalid input. Please enter numeric values.")


       
        
