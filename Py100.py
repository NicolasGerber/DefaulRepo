
def add(n1,n2):
    return n1 + n2
def sub(n1,n2):
    return n1 - n2
def mult(n1,n2):
    return n1 * n2
def div(n1,n2):
    return n1 / n2
operations = {"+": add,
              "-": sub,
              "*": mult,
              "/": div,
              }
def calculator(): #Using this function as recursion
    print("CALCULATOR")
    should_accumulate = True
    num1 = float(input("Type he first number: "))
    while should_accumulate:
        operation = input("Type the operation you want to realize (+,-,*,/): ")
        num2 = float(input("Now type the second number:"))
        result = operations[operation](num1,num2)
        print(f"{num1} {operation} {num2} = {result}")
        choice = input(f"Type 'y' to continue calculating with {result} or type 'n' to start a new calculation: ")

        if choice == 'y':
            num1 = result
        else:
            should_accumulate = False
            print("\n" *20)
            calculator()
calculator()