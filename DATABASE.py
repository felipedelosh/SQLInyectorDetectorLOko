"""
Base de datos del banco
"""
import sqlite3

class DataBase:
    def __init__(self):
        # Create a DB and open conection
        self.dataBasename = "DataBase"
        self.myConnect = sqlite3.connect(self.dataBasename)
        self.cursor = self.myConnect.cursor()
        self.createTables()
        # Close a principal Thread to sql
        self.closeDataBaseConection()

    def createTables(self):
        """
        This create a tables
        user(
            string username 50 pk,
             string password 50)
        """
        self.cursor.execute("create table if not exists user("+
            "username varchar(50)"+
            ", password varchar(50),"+
            "PRIMARY KEY(username))")

        print("Tablas de usuario creadas")

    def createUser(self, strusername, strpassword):
        try:
            conn = sqlite3.connect(self.dataBasename, check_same_thread=False)
            cur = conn.cursor()
            sql = "insert into user values('"+strusername+"', '"+strpassword+"');"
            cur.execute(sql)
            # Save a changes
            conn.commit()
            conn.close()
        except:
            pass

    def loginUser(self, strusername, strpassword):
        conn = sqlite3.connect(self.dataBasename, check_same_thread=False)
        cur = conn.cursor()
        sql = "select * from user where username='"+strusername+"' and password='"+strpassword+"';"
        cur.execute(sql)
        return len(cur.fetchall()) > 0


    def closeDataBaseConection(self):
        self.myConnect.close()


a = DataBase()
