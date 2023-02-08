from colorama import Fore
from .utils import get_max_len

SALIR = 0


def show_menu(menu_options:dict, optional_title:str="", optional_argument:str="") -> None:
    
    salir = False
    list_of_options = []
    for option in list(menu_options.values()):
        opt = str(option.__name__).replace('_', ' ')
        list_of_options.append(opt)
        
    while not salir:
        show_options(list_of_options = list_of_options, optional_title=optional_title)
        option = select_option()
        
        if option == SALIR:
            print(f"{Fore.LIGHTGREEN_EX}Thank you for using our service. Please come back soon!{Fore.RESET}")
            salir = True
        
        else: 
            try:
                if not optional_argument:
                    menu_options[option]()
                else:
                    menu_options[option](optional_argument)            
            except:
                print(f"{Fore.RED}The option you selected is not available. Please try again.{Fore.RESET}")
           
            
            

def select_option() -> int:
    #system("cls")
    option_ok = False
    option = ""

    while not option_ok:
        try:
            option = int(input(f"{Fore.LIGHTBLUE_EX}Please select an option: {Fore.RESET}"))
            print("\n")
            option_ok = True
        except:
            print(f"{Fore.RED}You can only enter numbers. Please try again.{Fore.RESET}")
    
    return option    
    
    
def show_options(list_of_options:list, optional_title:str="") -> None:
    options_max_len = get_max_len(list_of_options)
    final_str = f"""{Fore.RED}
        ╔══════════════════════════════════════════╗
        ║            {Fore.RESET}{Fore.BLUE}INNOKENTIY CODING ©           {Fore.RESET}{Fore.RED}║
        ║         {Fore.RESET}{Fore.BLUE}USERS DATABASE INTERFACE         {Fore.RESET}{Fore.RED}║
        ╚══════════════════════════════════════════╝{Fore.RESET}
        \nDeveloped by {Fore.MAGENTA}@andresdeinnocentiis{Fore.RESET}\n\n"""
    
    final_str += f'{Fore.MAGENTA}{optional_title.title()}{Fore.RESET}\n\n' if optional_title else "\b"
    
    for index, option in enumerate(list_of_options):
        final_str += f'{Fore.YELLOW}{index+1}.{Fore.RESET} {Fore.GREEN}{option.upper()}{Fore.RESET}\n'
    
    final_str += f"{Fore.LIGHTRED_EX}{'-'*(options_max_len+5)}{Fore.RESET}\n"
    final_str += f"{Fore.YELLOW}0.{Fore.RESET} {Fore.RED}SALIR{Fore.RESET}\n"
    
    print(final_str)
