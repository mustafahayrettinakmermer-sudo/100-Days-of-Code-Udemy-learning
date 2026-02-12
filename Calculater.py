n1 = int(input("Enter a number: "))
n2 = int(input("Enter another number: "))
operation_ask = input("+\n-\n*\n\n/\nEnter operation: ")


def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        print("O can not be devided !!! enter new number")
        n2 = int(input("Enter another number: "))
    return n1 / n2


operation = ["+", "-", "*", "/"]

continue_program = True
while continue_program:
    if operation_ask == operation[0]:
        result = add(n1,n2)
    elif operation_ask == operation[1]:
        result = subtract(n1,n2)
    elif operation_ask == operation[2]:
        result = multiply(n1,n2)
    elif operation_ask == operation[3]:
        result = divide(n1,n2)
    else:
        print("Invalid operation!!!!!")
        continue
    print(f"{n1} {operation_ask} {n2} = {result}")

    continue_again = input(f"\nContinue? (y/n) with the calculated value {result}: ")
    if continue_again == "y":
        n1 = result
        n2 = int(input("Enter another number: "))
        operation_ask = input("+\n-\n*\n\n/\nEnter operation: ")
    else:
        continue_program = False
        print("Goodbye!")

