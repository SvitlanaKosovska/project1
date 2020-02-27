def exec(operation):
    while True:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print('Invalid input')
            continue
        else:
            operation(num1, num2)
            break

def division_operation(num1, num2):
    """The function divides two numbers"""
    if num2 != 0:
        print("Result: ", num1 / num2)
    else:
        print("""You can't divide by zero!""")


def multiply_operation(num1, num2):
    """The function is multiplication two numbers"""
    print('Result:', num1 * num2)


def adding_operation(num1, num2):
    """This function adds two numbers"""
    print('Result: ', num1 + num2)


def subtraction_operation(num1, num2):
    """This function subtracts two numbers"""
    print('Result: ', num1 - num2)


def power_of_a_number_operation(num1, num2):
    """this function raises the number to a power"""
    print('Result: ', pow(num1, num2))


print('Type "exit" to quit')

while True:
    operation = input("Select operation (add, sub, mult, div, pow, exit) ")
    if operation in '(add, sub, mult, div, pow, exit)':
        if operation == 'exit':
            break
        else:
            if operation == 'div':
                exec(division_operation)
            elif operation == 'mult':
                exec(multiply_operation)
            elif operation == 'add':
                exec(adding_operation)
            elif operation == 'sub':
                exec(subtraction_operation)
            elif operation == 'pow':
                exec(power_of_a_number_operation)
    else:
        print('Invalid input')


print('The end.')
