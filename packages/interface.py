from .utils import file_to_dict, dict_to_file, require
from .menu import show_menu, show_options
from .users import valid_username, user_exists, validate_login
from .project_paths import FILE_PATH
from colorama import Fore
import os



OTHER_DATA_REQUIRED = ["password", "phone_number"]



def register() -> None:
    
    db = file_to_dict(FILE_PATH)
    user_dict = {}
    if db:
        username = valid_username(database_path=FILE_PATH).lower()
        
        if not user_exists(username=username, database_path=FILE_PATH):
            for data in OTHER_DATA_REQUIRED:
                user_dict[data] = require(data)
                    
            
            old_users = file_to_dict(FILE_PATH)
            old_users[username] = user_dict 
            
            dict_to_file(users_dict=old_users,save_to=FILE_PATH)
            print("\n")
            print(f"{Fore.LIGHTGREEN_EX}User registered successfully!{Fore.RESET}")
            os.system("pause")
    else:
        dict_to_file(users_dict=user_dict, save_to=FILE_PATH)
        username = valid_username(database_path=FILE_PATH).lower()
        
        if not user_exists(username=username, database_path=FILE_PATH):
            for data in OTHER_DATA_REQUIRED:
                user_dict[data] = require(data)
                    
            
            old_users = file_to_dict(FILE_PATH)
            old_users[username] = user_dict 
            
            dict_to_file(users_dict=old_users,save_to=FILE_PATH)
            print("\n")
            print(f"{Fore.LIGHTGREEN_EX}User registered successfully!{Fore.RESET}")
            os.system("pause")
        
        
        
def get_list_of_users() -> list:
    
    users_dict = file_to_dict(FILE_PATH)
    if users_dict:
        if users_dict.keys():
            list_of_users = list(users_dict.keys())
            
            users = show_options(list_of_options=list_of_users, optional_title="LIST OF REGISTERED USERS:")
            os.system("pause")
            
            print(users)
        else:
            print(f"{Fore.MAGENTA}Database is still empty, please register new users to see a list.{Fore.RESET}")
    else:
        print(f"{Fore.MAGENTA}Database hasn't been created yet. Please register new users to see a list.{Fore.RESET}")
    os.system("pause") 

def change_username(old_username) -> None:
    
    
    username = valid_username(database_path=FILE_PATH, new=True)
    users_dict = file_to_dict(FILE_PATH)
    users_dict[username] = users_dict.pop(old_username)
    
    dict_to_file(users_dict=users_dict, save_to=FILE_PATH)
    
    print(f"{Fore.LIGHTGREEN_EX}Username has been changed successfully!{Fore.RESET}")
    os.system("pause") 
    
    
def change_password(username) -> None:
    
    equals = False
    while not equals:
        new_password = input("Please enter your new password: ")
        repeat_password = input("Please repeat the password: ")
        
        if new_password == repeat_password:
            equals = True
        else:
            print(f"{Fore.RED}Passwords do not match. Please try again...{Fore.RESET}")
            
    users_dict = file_to_dict(FILE_PATH)
    users_dict[username]["password"] = new_password
    
    dict_to_file(users_dict=users_dict, save_to=FILE_PATH)
    
    print(f"{Fore.LIGHTGREEN_EX}Password has been changed successfully!{Fore.RESET}")
    os.system("pause") 


def delete_user() -> None:
    salir = False
    users_dict = file_to_dict(FILE_PATH)
    if users_dict:
        username = input("Which user would you like to delete from database? ")
        while not user_exists(username=username, database_path=FILE_PATH) and not salir:
            username = input(f"{Fore.MAGENTA}User does not exist. Please try another username: {Fore.RESET}") 
            if username == '0':
                salir = True

        
        users_dict.pop(username)  
        dict_to_file(users_dict=users_dict, save_to=FILE_PATH)
        
        print(f"{Fore.MAGENTA}User deleted successfully.{Fore.RESET}")
    os.system("pause") 
    

def login() -> None:
    
    users_dict = file_to_dict(FILE_PATH)
    valid_user = False
    
    if users_dict:
        while not valid_user:
            
            username = input("Please type in your username: ").lower()
            password = input("Please type in your password: ")
        
            if validate_login(database_path=FILE_PATH, username=username, password=password):
                valid_user = True
                title = f'{Fore.MAGENTA}Your are logged in as{Fore.RESET} {Fore.LIGHTBLUE_EX}{username}{Fore.RESET}'
                login_options = {
                    1: change_username,
                    2: change_password,
                }
                show_menu(menu_options=login_options, optional_title=title, optional_argument=username)  
    os.system("pause")   

def delete_database():
    
    users_dict = file_to_dict(FILE_PATH)
    if users_dict:
        sure = input(f"{Fore.RED}WARNING! You are about to delete the whole database. Are you sure you want to continue? [Y/N]: {Fore.RESET}").upper()
        
        while sure != 'Y' and sure != 'N':
            print("You can only type 'Y' for Yes, or 'N' for No.")
            sure = input(f"{Fore.RED}WARNING! You are about to delete the whole database. Are you sure you want to continue? [Y/N]: {Fore.RESET}")
        
        if sure == 'Y':
            os.remove(FILE_PATH)
            print(f"{Fore.RED}Database has been deleted successfully.{Fore.RESET}")
            os.system("pause")  
        else:
            os.system("pause") 
    else:
        print(print(f"{Fore.MAGENTA}Database hasn't been created yet. Please register new users to see a list.{Fore.RESET}"))
        os.system("pause") 
    
