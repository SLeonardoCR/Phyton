import sqlite3

class Database:
    def __init__(self, db):#this method is executed when the class is instantiated
        self.conn=sqlite3.connect(db)
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, author TEXT,"+
        "year INTEGER, isbn INTEGER)")
        self.conn.commit()

    def insert(self, title, author, year, isbn):
        self.cur.execute("INSERT INTO book (title, author, year, isbn) VALUES (?,?,?,?)", (title, author, year, isbn))
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * FROM book")
        rows=self.cur.fetchall()
        return rows

    def search(self, title="", author="", year=0, isbn=0):
        self.cur.execute("SELECT * FROM book WHERE title=? OR author =? OR year=? OR isbn=?", (title, author, year, isbn))
        rows=self.cur.fetchall()
        return rows

    def delete(self, id):
        self.cur.execute("DELETE FROM book WHERE id=?", (id,))
        self.conn.commit()

    def update(self, id, title, author, year, isbn):
        self.cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?", (title, author, year, isbn, id))
        self.conn.commit()

    def __del__(self):#this is executed when the instance is deleted from the script
        self.conn.close()



#connect()
#insert("WUTUP", "No she", 2487, 156)
#delete(2)
#update(3, "The Moon", "John Smith", 1997, 549682)
#print(view())
#print(search(year=2417))