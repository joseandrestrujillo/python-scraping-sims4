import sqlite3 as sql

class controller:
    def insertStatus(stock, price):
        conn = sql.connect("scraper.db")
        cursor = conn.cursor()
        query = f"INSERT INTO status_game VALUES({stock},{price})"
        cursor.execute(query)
        conn.commit()
        conn.close()

    def getLastStatus():
        conn = sql.connect("scraper.db")
        cursor = conn.cursor()
        query = f"SELECT * FROM status_game ORDER BY rowid DESC LIMIT 1;"
        cursor.execute(query)
        data = cursor.fetchone()
        conn.commit()
        conn.close()
        return data

    def getMinorPrice():
        conn = sql.connect("scraper.db")
        cursor = conn.cursor()
        query = f"SELECT * FROM status_game WHERE stock=1 ORDER BY price ASC LIMIT 1;"
        cursor.execute(query)
        data = cursor.fetchone()
        conn.commit()
        conn.close()
        return data
