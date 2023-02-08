import os
import json
import pandas as pd
from .project_paths import DATABASE_FILE_TXT, DATABASE_FILE_CSV, DATABASE_FILE_JSON
from colorama import Fore




def file_to_dict(database_path:str) -> dict:
    
    users_dict = {}
    
    try:
        filename, file_extension = os.path.splitext(database_path)
        
        if file_extension == ".txt":

            with open(database_path) as database_file:
                data = database_file.read() 
                users_dict = json.loads(data)   
                     
        elif file_extension == ".json":
            
            with open(database_path) as database_file:
                users_dict = json.load(database_file)        
                

        elif file_extension == ".csv":

            file = pd.read_csv(database_path)
            file = file.loc[:, ~file.columns.str.contains('^Unnamed')]
            
            users_dict = file.set_index('username').T.to_dict('dict')
            
            
    except:
        print("Path does not exist or Database has not been created yet.")  
        
    
    return users_dict


def dict_to_file(users_dict:dict, save_to:str) -> None:
    
    try:
        filename, file_extension = os.path.splitext(save_to)
        if file_extension == ".json":
            with open(DATABASE_FILE_JSON, "w") as file_to_save:
                json.dump(users_dict, file_to_save)
        
        elif file_extension == ".txt":
            with open(DATABASE_FILE_TXT, "w") as file_to_save:
                file_to_save.write(json.dumps(users_dict))
            
        elif file_extension == ".csv":   
            
            list_of_keys = ["username"]
            rows = []
            
            for key, value in users_dict.items():             
                for sub_key, sub_val in value.items():
                    list_of_keys.append(sub_key)
                break
                
            for key, value in users_dict.items():
                vals_row = []
                rows.append(vals_row)
                vals_row.append(key)
                for sub_key, sub_val in value.items():
                    vals_row.append(sub_val)
            
            users_df = pd.DataFrame(data=rows, columns=list_of_keys)
            users_df = users_df.loc[:, ~users_df.columns.str.contains('^Unnamed')]
            
            users_df.to_csv(DATABASE_FILE_CSV)
                
            
        else:
            print("Path error. The path doesn't exist..")
    
    except:
        print("Argument 'users_dict' MUST BE a dictionary. Try again.")
   
        
def require(data) -> str:
    data_required = input(f'{Fore.LIGHTGREEN_EX}Please type in your {data}: {Fore.RESET}')
    return data_required


def get_max_len(list_of_options:list) -> int:
    max = ""
    max_length = 0
    for option in list_of_options:
        if len(option) > len(max):
            max = option
    
    max_length = len(max)
    
    return max_length
   
