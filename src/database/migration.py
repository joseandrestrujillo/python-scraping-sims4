import sqlite3 as sql

class migration:
    def createDB():
        conn = sql.connect("scraper.db")
        conn.commit()
        conn.close()
    
    def createTable():
        conn = sql.connect("scraper.db")
        cursor = conn.cursor()
        cursor.execute(
            """CREATE TABLE status_game(
                stock INTEGER,
                price REAL     
            )"""
        )
        conn.commit()
        conn.close()


migration.createDB()
migration.createTable()

