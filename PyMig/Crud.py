import mysql.connector
from .Connect import Connect


class Crud(Connect):
    def __init__(self,  host:str='localhost', user:str='root', password:str='', database:str=''):
        Connect.__init__(self, host, user, password, database)
    
    def create_db(self):
        pass