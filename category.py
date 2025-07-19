from base import Parent
from pymysql import IntegrityError
from products import Product,product_crud

class Category(Parent):

    @staticmethod
    def create(name):
        with Category.connect() as conn:
            with conn.cursor() as cursor:
                try:
                    sql = "INSERT INTO category (name) VALUES (%s)"
                    cursor.execute(sql, (name,))
                    conn.commit()
                    print("Kategoriya qo‘shildi.")
                except IntegrityError:
                    print("Bu kategoriya allaqachon mavjud.")

    @staticmethod
    def read():
        with Category.connect() as conn:
            with conn.cursor() as cursor:
                sql = "SELECT * FROM category"
                cursor.execute(sql)
                return cursor.fetchall()

    @staticmethod
    def update(category_id, new_name):
        with Category.connect() as conn:
            with conn.cursor() as cursor:
                sql = "UPDATE category SET name = %s WHERE id = %s"
                cursor.execute(sql, (new_name, category_id))
                if cursor.rowcount:
                    print("Kategoriya yangilandi.")
                else:
                    print("Kategoriya topilmadi.")
                conn.commit()

    @staticmethod
    def delete(category_id):
        with Category.connect() as conn:
            with conn.cursor() as cursor:
                sql = "DELETE FROM category WHERE id = %s"
                cursor.execute(sql, (category_id,))
                if cursor.rowcount:
                    print("Kategoriya o‘chirildi.")
                else:
                    print("Kategoriya topilmadi.")
                conn.commit()

def category_crud():
    habar = """
    Kategoriya amallaridan birini tanlang:
        1. Ko'rish
        2. Qo‘shish
        3. O‘zgartirish
        4. O‘chirish
        5. Chiqish
    """

    while True:
        tanlov = int(input(habar))

        match tanlov:
            case 1:
                for category in Category.read():
                    print(f"{category['id']}: {category['name']}")
            case 2:
                name = input("Mahsulot nomi: ")
                stock = int(input("Soni: "))
                price = int(input("Narxi: "))

                print("Mavjud kategoriyalar:")
                for category in Category.read():
                    print(f"{category['id']}: {category['name']}")

                category_id = int(input("Kategoriya ID sini tanlang: "))
                Product.create(name, stock, price, category_id)

            case 3:
                category_id = input("Kategoriya ID: ")
                new_name = input("Yangi nom: ")
                Category.update(category_id, new_name)
            case 4:
                category_id = input("Kategoriya ID: ")
                Category.delete(category_id)
            case 5:
                return

if __name__ == "__main__":
    while True:
        tanlov = input("1. Mahsulotlar CRUD\n2. Kategoriyalar CRUD\n3. Chiqish\n>>> ")
        if tanlov == "1":
            product_crud()
        elif tanlov == "2":
            category_crud()
        else:
            break
