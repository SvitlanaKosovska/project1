def division_operation():
    """The function divides two numbers"""
    while True:
        try:
            num1 = float(input("Введіть перше число "))
            num2 = float(input("Введіть друге число "))
        except ValueError:
            print("Потрібно ввести число!")
        else:
            if num2 != 0:
                print("Результат ділення: ", num1 / num2)
            else:
                print('Ділити на нуль не можна')
        break


def multiply_operation():
    """The function is multiplication two numbers"""
    while True:
        try:
            num1 = float(input("Введіть перше число "))
            num2 = float(input("Введіть друге число "))
        except ValueError:
            print("Потрібно ввести число!")
        else:
            print('Результат множення:', num1 * num2)
        break


def adding_operation():
    """This function adds two numbers"""
    while True:
        try:
            num1 = float(input("Введіть перше число "))
            num2 = float(input("Введіть друге число "))
        except ValueError:
            print("Потрібно ввести число!")
        else:
            print('Результат додавання: ', num1 + num2)
        break


def subtraction_operation():
    """This function subtracts two numbers"""
    while True:
        try:
            num1 = float(input("Введіть перше число "))
            num2 = float(input("Введіть друге число "))
        except ValueError:
            print("Потрібно ввести число!")
        else:
            print('Результат віднімання: ', num1 - num2)
        break


def power_of_a_number_operation():
    """this function raises the number to a power"""
    while True:
        try:
            num1 = float(input("Введіть число "))
            n = float(input("Введіть степінь, до якого треба піднести число "))
        except ValueError:
            print("Потрібно ввести число!")
        else:
            print('Результат піднесення до степеня: ', pow(num1, n))
        break


print('Exit - завершить роботу програми')

while True:
    operation = input("Введіть дію (+, -, *, /, power_of_a_number, exit) ")
    if operation in '(+, -, *, /, power_of_a_number, exit)':
        if operation == 'exit':
            break
        else:
            if operation == '/':
                division_operation()
            elif operation == '*':
                multiply_operation()
            elif operation == '+':
                adding_operation()
            elif operation == '-':
                subtraction_operation()
            elif operation == 'power_of_a_number':
                power_of_a_number_operation()
    else:
        print('Невірно введена операція')