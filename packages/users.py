from .utils import file_to_dict, dict_to_file
from colorama import Fore

"""
ESTE MÓDULO SE VA A USAR PARA TRABAJAR CON OBJETOS LUEGO, CREANDO UNA CLASE 'User()'
"""

def user_exists(username:str, database_path:str) -> bool:
    
    users_dict = file_to_dict(database_path)
    is_user = False
    
    try:
        if username in users_dict.keys():
            is_user = True
    
    except:
        print(f"{Fore.MAGENTA}The database has not been created yet. Try later.{Fore.RESET}")

    return is_user

def valid_username(database_path:str, new=False) -> str:
    username = input(f"{Fore.LIGHTGREEN_EX}Please type in your{' new' if new else '' } username: {Fore.RESET}")
    while len(username) < 3 or user_exists(username=username, database_path=database_path): 
        if len(username) < 3:
            print(f"{Fore.RED}Username must be at least 3 characters long.{Fore.RESET}\n")
            username = input("Please type another username: ")
            
        elif user_exists(username=username, database_path=database_path):
            username = input(f"{Fore.MAGENTA}User already exists. Please choose another username: {Fore.RESET}")
    
    return username
    


def validate_login(database_path:str, username:str, password:str) -> bool:
    
    valid_login = False
    users_dict = file_to_dict(database_path)
    if user_exists(username=username,database_path=database_path):
        
        if str(users_dict[username]["password"]) == password:
            valid_login = True
        else:
            print(f"{Fore.RED}Password does not match the username: {username}. Please try again{Fore.RESET}\n")
    else:
        print(f"{Fore.RED}Username: '{username}' does not exist.{Fore.RESET}\n")
        
        
    return valid_login


















