import sqlite3
 
# conn = sqlite3.connect("mydatabase.db") # или :memory: чтобы сохранить в RAM
# cursor = conn.cursor()
 
# # Создание таблицы
# # cursor.execute("""CREATE TABLE price
# #                   (id int PRIMARY KEY NOT NULL, site text, price float, date datetime)
# #                """)


class Base:

    def __init__(self):
        self.conn = sqlite3.connect("mydatabase.db")
        
    def select(self, query):
        cursor = self.conn.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()

        return result  

    def insert(self, query):
        cursor = self.conn.cursor()
        cursor.execute(query)
        self.conn.commit()
        cursor.close() 
        
