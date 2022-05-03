import mysql.connector
from utils import MainUtils


class Connect:
    def __init__(self, host: str = 'localhost', user: str = 'root', password: str = '', database: str = ''):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def connect(self):
        conn = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password
        )
        return conn

    def connect_db(self):
        try:
            conn = mysql.connector.connect(
                host=self.host, user=self.user, password=self.password, database=self.database)

            cursor = conn.cursor()
            return cursor
        except:
            MainUtils.box_line("connect db: Something went wrong.")

    def show_database(self):
        db = self.connect()
        cursor = db.cursor()
        cursor.execute("SHOW DATABASES")
        arr = []
        for i in cursor:
            arr.append(i[0])
        return arr
