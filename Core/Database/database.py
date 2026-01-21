import os
import sqlite3
import datetime
from zoneinfo import ZoneInfo
from ..Hash_tools import hash

class Database:
    """При создании базы данных .db в конце указывать НЕ нужно"""
    
    default_path = "./database"
    
    
    def __init__(self, spread_sheet: str) -> None:
        self.conn = self.__connect_db(f'{spread_sheet}.db')
        self.cursor = self.conn.cursor()
        
        match spread_sheet:
            case "users":
                self.__create_users_db()
            case "tasks":
                self.__create_tasks_db()
            case _:
                raise ValueError("Unknown name spread_sheet")
        
        
    def user_info(self, id: int) -> dict[str, str]:
        """Возвращает информацию о пользователе"""
        
        self.cursor.execute(
            "SELECT * FROM users WHERE id = ?",
            (id,)
        )
        
        result = self.cursor.fetchone()
        
        if result is None:
            self.__create_user(id)
            return self.user_info(id)
        
        column_names = [description[0] for description in self.cursor.description]
        
        return dict(zip(column_names, result))
    
    
    def update_user_info(self, **kwargs) -> None: # не реализована, пока-что только как заглушка
        """Обновляет информацию о пользователе"""
        
        self.cursor.execute(
            """UPDATE users
            SET name = ?, group_name = ?
            WHERE id = ?
            """,
            ()
        )
        self.conn.commit()
    
    
    def task_info():
        """Выводит информацию о задаче"""
        ...


    def create_task():
        """Создает новую задачу"""
        ...
    
        
    def __create_user(self, id) -> None:
        """Создает нового пользователя в бд users"""
        
        now_data = ZoneInfo("Europe/Moscow")
        now_data = datetime.datetime.now(now_data)
        now_data = now_data.strftime("%d-%m-%Y %H:%M:%S")
        
        self.cursor.execute(
            "INSERT INTO users (id, hash_id, name, group_name, registry_data, is_admin, is_banned) VALUES (?, ?, ?, ?, ?, ?, ?)",
            (id, hash.sha256_hash(str(id)), None, None, now_data, 0, 0) 
        ) 
        
        self.conn.commit()
                    
        
    def __create_users_db(self) -> None:
        """Проверяет существование бд пользователей и создает если нет"""
        
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS "users" (
	            "id"	INTEGER NOT NULL,
	            "hash_id"	TEXT NOT NULL UNIQUE,
	            "name"	TEXT,
	            "group_name"	TEXT,
	            "registry_data"	TEXT NOT NULL,
	            "is_admin"	INTEGER NOT NULL,
	            "is_banned"	INTEGER NOT NULL,
	        PRIMARY KEY("id")
                )
        ''')
        
        self.conn.commit()
        
    
    def __create_tasks_db(self) -> None:
        """Проверяет существование бд заданий и создает если нет"""
        ...
    
    
    def __connect_db(self, spread_sheet: str) -> sqlite3.Connection:
        """Подключает бд и создает папку database"""
        
        if "database" not in os.listdir():
            os.mkdir("./database")
        
        return sqlite3.connect(os.path.join(Database.default_path, spread_sheet))