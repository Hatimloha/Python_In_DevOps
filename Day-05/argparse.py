import argparse

# Define your functions
def addition(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mul(num1, num2):
    return num1 * num2

# Set up argument parsing
def main():
    parser = argparse.ArgumentParser(description='Perform basic arithmetic operations.')
    
    # Add arguments
    parser.add_argument('operation', choices=['add', 'sub', 'mul'], help='The arithmetic operation to perform')
    parser.add_argument('num1', type=float, help='The first number')
    parser.add_argument('num2', type=float, help='The second number')
    
    # Parse arguments
    args = parser.parse_args()
    
    # Perform the requested operation
    if args.operation == 'add':
        result = addition(args.num1, args.num2)
    elif args.operation == 'sub':
        result = sub(args.num1, args.num2)
    elif args.operation == 'mul':
        result = mul(args.num1, args.num2)
    
    # Print the result
    print(f'Result: {result}')

if __name__ == '__main__':
    main()
