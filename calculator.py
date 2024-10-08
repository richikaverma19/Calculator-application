from colorama import init, Fore, Style

# Initialize Colorama for colored output
init(autoreset=True)

# Calculator functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return Fore.RED + "Error! Division by zero."
    return x / y

# Display the calculator menu
def show_menu():
    print(Fore.CYAN + "="*35)
    print(Fore.MAGENTA + "          Simple Calculator")
    print(Fore.CYAN + "="*35)
    print(Fore.YELLOW + "Select an operation:")
    print(Fore.YELLOW + "1. Add")
    print(Fore.YELLOW + "2. Subtract")
    print(Fore.YELLOW + "3. Multiply")
    print(Fore.YELLOW + "4. Divide")
    print(Fore.YELLOW + "5. Exit")
    print(Fore.CYAN + "="*35)

# Main calculator logic
def calculator():
    while True:
        show_menu()
        try:
            choice = input(Fore.CYAN + "Choose an operation (1-5): " + Fore.WHITE)
            
            if choice == '5':
                print(Fore.GREEN + "Goodbye! Thanks for using the calculator!")
                break
            
            if choice in ['1', '2', '3', '4']:
                num1 = float(input(Fore.CYAN + "Enter the first number: " + Fore.WHITE))
                num2 = float(input(Fore.CYAN + "Enter the second number: " + Fore.WHITE))

                if choice == '1':
                    result = add(num1, num2)
                    print(Fore.GREEN + f"\nThe result of {num1} + {num2} is: {result}\n")

                elif choice == '2':
                    result = subtract(num1, num2)
                    print(Fore.GREEN + f"\nThe result of {num1} - {num2} is: {result}\n")

                elif choice == '3':
                    result = multiply(num1, num2)
                    print(Fore.GREEN + f"\nThe result of {num1} * {num2} is: {result}\n")

                elif choice == '4':
                    result = divide(num1, num2)
                    print(Fore.GREEN + f"\nThe result of {num1} / {num2} is: {result}\n")
            else:
                print(Fore.RED + "Invalid choice! Please choose a valid operation.\n")
        
        except ValueError:
            print(Fore.RED + "Invalid input! Please enter numbers only.\n")

if __name__ == "__main__":
    calculator()
