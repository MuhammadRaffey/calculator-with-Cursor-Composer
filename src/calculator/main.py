from .calculator import Calculator
from colorama import init, Fore, Style

def main():
    init()
    
    calc = Calculator()
    
    print(f"\n{Fore.CYAN}╔══════════════════════╗{Style.RESET_ALL}")
    print(f"{Fore.CYAN}║  {Fore.YELLOW}Simple Calculator{Fore.CYAN}   ║{Style.RESET_ALL}")
    print(f"{Fore.CYAN}╚══════════════════════╝{Style.RESET_ALL}\n")
    
    print(f"{Fore.GREEN}Available Operations:{Style.RESET_ALL}")
    print(f"{Fore.WHITE}1.{Style.RESET_ALL} {Fore.YELLOW}Add{Style.RESET_ALL}")
    print(f"{Fore.WHITE}2.{Style.RESET_ALL} {Fore.YELLOW}Subtract{Style.RESET_ALL}")
    print(f"{Fore.WHITE}3.{Style.RESET_ALL} {Fore.YELLOW}Multiply{Style.RESET_ALL}")
    print(f"{Fore.WHITE}4.{Style.RESET_ALL} {Fore.YELLOW}Divide{Style.RESET_ALL}\n")
    
    while True:
        try:
            choice = int(input(f"{Fore.GREEN}Enter choice (1-4): {Style.RESET_ALL}"))
            if not 1 <= choice <= 4:
                raise ValueError("Please enter a number between 1 and 4")
            break
        except ValueError as e:
            print(f"{Fore.RED}Invalid input! {str(e)}{Style.RESET_ALL}")

    def get_number(prompt):
        while True:
            try:
                return float(input(f"{Fore.GREEN}{prompt}: {Style.RESET_ALL}"))
            except ValueError:
                print(f"{Fore.RED}Invalid input! Please enter a valid number.{Style.RESET_ALL}")

    try:
        num1 = get_number("Enter first number")
        num2 = get_number("Enter second number")
        
        print(f"\n{Fore.CYAN}═══════ Result ═══════{Style.RESET_ALL}")
        
        operations = {
            1: (calc.add, '+'),
            2: (calc.subtract, '-'),
            3: (calc.multiply, '*'),
            4: (calc.divide, '/')
        }
        
        operation, symbol = operations[choice]
        try:
            result = operation(num1, num2)
            print(f"{Fore.WHITE}{num1} {Fore.YELLOW}{symbol}{Style.RESET_ALL} "
                  f"{Fore.WHITE}{num2} {Fore.YELLOW}={Style.RESET_ALL} "
                  f"{Fore.GREEN}{result}{Style.RESET_ALL}")
        except ZeroDivisionError:
            print(f"{Fore.RED}Error: Cannot divide by zero!{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.RED}Error performing calculation: {str(e)}{Style.RESET_ALL}")
            
    except Exception as e:
        print(f"{Fore.RED}An unexpected error occurred: {str(e)}{Style.RESET_ALL}")
    
    print(f"\n{Fore.CYAN}═══════════════════════{Style.RESET_ALL}")

if __name__ == "__main__":
    main()