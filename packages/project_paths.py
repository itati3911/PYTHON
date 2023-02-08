import os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

DATABASE_FILE_TXT = os.path.join(BASE_DIR, "users_db.txt")

DATABASE_FILE_JSON = os.path.join(BASE_DIR, "users_db.json")

DATABASE_FILE_CSV = os.path.join(BASE_DIR, "users_db.csv")

"""
CAMBIAR EL PATH DE ACÁ ABAJO POR ALGUNO DE LOS 3 DE ARRIBA 'DATABASE', segun se quiera realizar el proceso con un archivo .txt, .json o .csv.    
"""

FILE_PATH = DATABASE_FILE_JSON