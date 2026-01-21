import time
import threading
from Core import app, bot, database


def main_loop():
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Сервер остановлен")
        
        
# ссылку на базы данных необходимо будет передавать в run() бота и сайта
db_users = database.Database("users") 
db_tasks = database.Database("tasks")

print(db_users.user_info(id=19)) # debug database

flask_thread = threading.Thread(target=app.run, kwargs= { "debug": False }, daemon=True)
flask_thread.start()

bot.run()        

main_loop()