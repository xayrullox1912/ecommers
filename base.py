import pymysql
from pymysql.cursors import DictCursor

class Parent:
    @staticmethod
    def connect():
        return pymysql.connect(
            host="localhost",
            user="root",
            password="2009",
            database="ec",
            cursorclass=DictCursor
        )
