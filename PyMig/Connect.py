import mysql.connector


class Connect:
    def __init__(self, host:str='localhost', user:str='root', password:str='', database:str=''):
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
        conn  = mysql.connector.connect(self.host, self.user, self.password, self.database)
        cursor = conn.cursor()
        return cursor

    def show_database(self):
        db = self.connect()
        cursor = db.cursor()
        cursor.execute("SHOW DATABASES")
        arr = []
        for i in cursor:
            arr.append(i[0])
        return arr

