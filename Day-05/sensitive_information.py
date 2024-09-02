# First save the sensitive_information in machine
export password="hatim"

# Programm:
def addition(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mul(num1, num2):
    return num1 * num2

print(addition(5, 10))  # Output: 15
print(sub(50, 10))     # Output: 40
print(mul(10, 20))     # Output: 200

num1 = int(sys.agrv[1])
operation = sys.agrv[2]
num2 = int(sys.agrv[3])

if operation == 'add':
  output = add(num1 + num2)
  print(output)


# Run command
python3 <file name> 2 & 3









