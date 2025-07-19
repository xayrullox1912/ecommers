import pymysql
from pymysql.cursors import DictCursor
from dotenv import load_dotenv
import os

load_dotenv()  # .env faylni yuklaydi

class Parent:
    @staticmethod
    def connect():
        return pymysql.connect(
            host="localhost",
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_DATABASE"),
            cursorclass=DictCursor
        )
