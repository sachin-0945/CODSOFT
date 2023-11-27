def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return 'Error! Division by zero is not allowed.'
    else:
        return x / y
while(True):
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    operation = input("Enter the number of the operation you want to perform: ")

    if operation == '5':
        exit()
    elif operation not in ['1','2','3','4','5']:
        print("Invalid operation!")    
    else: 
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if operation == '1':
            print(num1,'+',num2,'=', add(num1, num2))
        elif operation == '2':
            print(num1,'-',num2,'=', subtract(num1, num2))
        elif operation == '3':
            print(num1,'x',num2,'=', multiply(num1, num2))
        elif operation == '4':
            print(num1,'/',num2,'=', divide(num1, num2))

