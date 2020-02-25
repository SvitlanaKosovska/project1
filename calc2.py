def division_operation():
    """The function divides two numbers"""
    global num1
    global num2
    if num2 != 0:
        print("Result: ", num1 / num2)
    else:
        print("""You can't divide by zero!""")


def multiply_operation():
    """The function is multiplication two numbers"""
    global num1
    global num2
    print('Result:', num1 * num2)


def adding_operation():
    """This function adds two numbers"""
    global num1
    global num2
    print('Result: ', num1 + num2)


def subtraction_operation():
    """This function subtracts two numbers"""
    global num1
    global num2
    print('Result: ', num1 - num2)


def power_of_a_number_operation():
    """this function raises the number to a power"""
    global num1
    global num2
    print('Result: ', pow(num1, num2))


print('Type "exit" to quit')

while True:
    operation = input("Select operation (add, sub, mult, div, pow, exit) ")
    if operation in '(add, sub, mult, div, pow, exit)':
        if operation == 'exit':
            break
        else:
            while True:
                try:
                    num1 = float(input("Enter first number: "))
                    num2 = float(input("Enter second number: "))
                except ValueError:
                    print('Invalid input')
                else:
                    if operation == 'div':
                        division_operation()
                    elif operation == 'mult':
                        multiply_operation()
                    elif operation == 'add':
                        adding_operation()
                    elif operation == 'sub':
                        subtraction_operation()
                    elif operation == 'pow':
                        power_of_a_number_operation()
                break
    else:
        print('Invalid input')


print('The end.')
