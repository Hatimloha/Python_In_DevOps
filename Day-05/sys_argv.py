import sys

# Define your functions
def addition(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mul(num1, num2):
    return num1 * num2

# Main function to handle command-line arguments
def main():
    if len(sys.argv) != 4:
        print("Usage: python script.py <operation> <num1> <num2>")
        sys.exit(1)

    operation = sys.argv[1]
    try:
        num1 = float(sys.argv[2])
        num2 = float(sys.argv[3])
    except ValueError:
        print("Error: num1 and num2 must be numbers.")
        sys.exit(1)

    if operation == 'add':
        result = addition(num1, num2)
    elif operation == 'sub':
        result = sub(num1, num2)
    elif operation == 'mul':
        result = mul(num1, num2)
    else:
        print("Error: Operation must be 'add', 'sub', or 'mul'.")
        sys.exit(1)

    print(f'Result: {result}')

if __name__ == '__main__':
    main()
