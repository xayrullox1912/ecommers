from pymysql import IntegrityError
from base import Parent

class User(Parent):
    file_name = "users.json"

    def __init__(self, username, password, role="user"):
        self.username = username
        self.password = password
        self.role = role



    @staticmethod
    def read():
        with User.connect() as conn:
            with conn.cursor() as cursor:
                sql = "SELECT * FROM users"
                cursor.execute(sql)
                return cursor.fetchall()

    # CRUD
    @staticmethod
    def login(username, password):
        with User.connect() as conn:
            with conn.cursor() as cursor:
                sql = "SELECT * FROM users WHERE username=%s"
                cursor.execute(sql, (username,))
                row = cursor.fetchone()
                if row:
                    if row['password'] == password:
                        return row["id"], row["role"]
                    else:
                        print("Parol/login xato")
                        return None, None
                else:
                    print("Bunday foydalanuvchi bazada yo'q")
                    return None, None

    # CRUD
    @staticmethod
    def register(username, password):
        try:
            return User.create(username, password)
        except IntegrityError:
            print("Bunday foydalanuvchi bazada bor")
            return None

    @staticmethod
    def create(username, password):
        with User.connect() as conn:
            with conn.cursor() as cursor:
                sql = "INSERT INTO users(username, password) VALUES(%s,%s)"
                cursor.execute(sql, (username, password))
                conn.commit()

        return username

    @staticmethod
    def read_one(user_id):
        with User.connect() as conn:
            with conn.cursor() as cursor:
                sql = "SELECT * FROM users WHERE id=%s"
                cursor.execute(sql, (user_id,))
                return cursor.fetchone()

    @staticmethod
    def update(user_id, field, value):
        with User.connect() as conn:
            with conn.cursor() as cursor:
                sql = f"UPDATE users SET {field}=%s WHERE id=%s"
                cursor.execute(sql, (value, user_id))
                if cursor.rowcount:
                    print("Foydalanuvchi o'zgartirildi")
                conn.commit()

    @staticmethod
    def delete(user_id):
        with User.connect() as conn:
            with conn.cursor() as cursor:
                sql = f"DELETE FROM users where id= %s"
                cursor.execute(sql, (user_id,))
                if cursor.rowcount:
                    print("Foydalanuvchi o'chirildi")
                else:
                    print("Bunday foydalanuvchi yo'q")
                conn.commit()


def user_crud():
    habar = """
    Foydalanuvchi amallaridan birini tanlang
        1. Ko'rish
        2. Kiritish
        3. O'zgaritrish
        4. O'chirish
        5. Chiqish
    """

    while True:
        tanlov = int(input(habar))

        match tanlov:
            case 1:
                for user in User.read():
                    print(f"{user['username']}")
            case 2:
                username = input("Login kiriting")
                password = input("Parolni kiriting: ")
                User.create(username, password)
            case 3:

                user_id = input("O'zgartirmoqchi bo'lgan foydalanuvchi idsi")
                field = input("O'zgartirmoqchi bo'lgan ustun nomi")
                value = input("Qiymatni kiriting: ")
                User.update(user_id, field, value)
            case 4:
                user_id = input("Qaysi foydalanuvchini o'chirmoqchisiz?")
                User.delete(user_id)
            case 5:
                return


if __name__ == "__main__":
    user_crud()
