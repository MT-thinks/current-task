import os
import sqlite3

class Database:
    """При создании базы данных .db в конце указывать НЕ нужно"""
    default_path = "./database"
    
    
    def __init__(self, spread_sheet: str) -> None:
        self.conn = self.__connect_db(f'{spread_sheet}.db')
        self.cursor = self.conn.cursor()
        
        match spread_sheet:
            case "users":
                self._create_users()
            case "tasks":
                self._create_tasks()
            case _:
                raise ValueError("Unknown name spread_sheet")
        
        
        
    def _create_users(self) -> None:
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS "users" (
	            "id"	INTEGER NOT NULL,
	            "hash_id"	TEXT NOT NULL UNIQUE,
	            "name"	TEXT,
	            "group_name"	TEXT,
	            "registry_data"	TEXT NOT NULL,
	                PRIMARY KEY("id")
                 )
        ''')
        self.conn.commit()
        
    
    def _create_tasks(self) -> None:
        ...
    
    
    def __connect_db(self, spread_sheet: str) -> sqlite3.Connection:
        if "database" not in os.listdir():
            os.mkdir("./database")
        
        return sqlite3.connect(os.path.join(Database.default_path, spread_sheet))
    
    
        
db = Database("users") # example
