# Basic Calculator
from colorama import init, Fore, Style
# Class Function with different methods
class Calculator :
    def __init__(self):
        pass

    def add(self):
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        total = a + b
        return f"Result = {total}"
    
    def minus(self):
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        total = a - b
        return f"Result = {total}"

    def multiplication(self):
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        total = a * b
        return f"Result = {total}"

    def division(self):
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        total = a / b
        if b == 0:
                return "Error: Division by zero"
        return f"Result = {total}"

    def power(self):
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        total = a ** b
        return f"Result = {total}"

    def floor_mod(self):
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        total = a // b
        remainder = a % b
        return f"Result = {total} / remainder: {remainder}"

        

# Main program
if __name__ == "__main__":
    name = input("What is your name? ")
    answer = input(f"Is your name {name}?")
    while True:
        print("Are you sure? (yes/no)")
        name_confirm = input().lower()
        if name_confirm == "yes":
            break
        elif name_confirm == "no":
            name = input("Please enter your correct name: ")
    
            print(Fore.GREEN + f"Hello, {name}! "+ Style.RESET_ALL)
        
        else:
            print(Fore.RED + "Invalid input. Please enter 'yes' or 'no'." + Style.RESET_ALL)

    print("=" * 40)
    print(Fore.GREEN + f"Welcome back {name}" + Style.RESET_ALL)
    print("=" * 40)
    calc = Calculator()

    while True:
        operator = input("Choose your operator (+ - * / ** //): ")
        if operator == "+":
            print("=="* 40)
            calc = Calculator()
            print(calc.add())
            print("=="* 40)
            continue
            
        elif operator == "-":
            print("=="* 40)
            calc = Calculator()
            print(calc.minus())
            print("=="* 40)
            continue
        elif operator == "*":
            print("=="* 40)
            calc = Calculator()
            print(calc.multiplication())
            print("=="* 40)
            continue
        elif operator == "/":
            print("=="* 40)
            calc = Calculator()
            print(calc.division())
            print("=="* 40)
            continue
        elif operator == "**":
            print("=="* 40)
            calc = Calculator()
            print(calc.power())
            print("=="* 40)
            continue
        elif operator == "//":
            calc = Calculator()
            print(calc.floor_mod())
            print("=="* 40)
            continue
        elif operator == "end":
            print("~"* 40)
            print(Fore.BLUE + f"Goodbye {name}" + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + f"{operator} is not valid..." + Style.RESET_ALL)

    

  
