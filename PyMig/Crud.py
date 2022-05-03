from .Connect import Connect
from utils import MainUtils


class Crud(Connect):
    def __init__(self,  host: str = 'localhost', user: str = 'root', password: str = '', database: str = ''):
        Connect.__init__(self, host, user, password, database)

# """Database CRUD part start"""

    def exist_db(self):
        connection = super().connect()
        cursor = connection.cursor()
        cursor.execute(f"SHOW DATABASES LIKE '{self.database}'")
        arr = []
        for i in cursor:
            arr.append(i[0])
        if len(arr) > 0:
            return True
        else:
            return False

    def create_db(self):
        if self.exist_db() == True:
            MainUtils.box_line(f"{self.database} - database exist.")
        else:
            try:
                connection = super().connect()
                cursor = connection.cursor()
                cursor.execute(
                    f"CREATE DATABASE IF NOT EXISTS {self.database}")
                if self.exist_db() == True:
                    MainUtils.box_line(f"{self.database} - database created.")
            except:
                MainUtils.box_line(
                    f"Something went wrong. {self.database} - database not created.")

    def drop_db(self):
        if self.exist_db() != True:
            MainUtils.box_line(f"{self.database} - database not exist.")
        else:
            try:
                connection = super().connect()
                cursor = connection.cursor()
                cursor.execute(f"DROP DATABASE {self.database}")
                if self.exist_db() != True:
                    MainUtils.box_line(f"{self.database} - database removed.")
            except:
                MainUtils.box_line(
                    f"Something went wrong. {self.database} - database not removed.")


# """Database CRUD part finished"""
