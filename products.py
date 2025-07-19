from pymysql import IntegrityError
from base import Parent

class Product(Parent):

    @staticmethod
    def create(name, stock, price, category):
        with Product.connect() as conn:
            with conn.cursor() as cursor:
                try:
                    sql = "INSERT INTO products (name, stock, price, category) VALUES (%s, %s, %s, %s)"
                    cursor.execute(sql, (name, stock, price, category))
                    conn.commit()
                except IntegrityError:
                    print("Bu mahsulot bazada bor")

    @staticmethod
    def search(field,value):
        with Product.connect() as conn:
            with conn.cursor() as cursor:

                sql = f"Select * from products where {field} = %s"

                cursor.execute(sql, (value,))
                return cursor.fetchall()

    @staticmethod
    def filtrlash(category_id):
        with Product.connect() as conn:
            with conn.cursor() as cursor:
                sql = f"select * from products where category = %s "
                cursor.execute(sql,(category_id,))
                return cursor.fetchall()


    @staticmethod
    def read():
        with Product.connect() as conn:
            with conn.cursor() as cursor:
                sql = "SELECT * FROM products"
                cursor.execute(sql)
                return cursor.fetchall()

    @staticmethod
    def read_one(product_id):
        with Product.connect() as conn:
            with conn.cursor() as cursor:
                sql = "SELECT * FROM products WHERE id=%s"
                cursor.execute(sql, (product_id,))
                return cursor.fetchone()

    @staticmethod
    def update(product_id, field, value):
        with Product.connect() as conn:
            with conn.cursor() as cursor:
                sql = f"UPDATE products SET {field} = %s WHERE id = %s"
                cursor.execute(sql, (value, product_id))
                if cursor.rowcount:
                    print("Mahsulot o‘zgartirildi")
                else:
                    print("Bunday mahsulot yo‘q")
                conn.commit()

    @staticmethod
    def delete(product_id):
        with Product.connect() as conn:
            with conn.cursor() as cursor:
                sql = "DELETE FROM products WHERE id = %s"
                cursor.execute(sql, (product_id,))
                if cursor.rowcount:
                    print("Mahsulot o‘chirildi")
                else:
                    print("Bunday mahsulot topilmadi")
                conn.commit()


def product_crud():
    habar = """
    Mahsulot amallaridan birini tanlang
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
                for product in Product.read():
                    print(f"{product['id']}: {product['name']} - {product['stock']} dona - {product['price']} so'm - {product['category']}")
            case 2:
                name = input("Mahsulot nomi: ")
                stock = int(input("Soni: "))
                price = int(input("Narxi: "))
                category = input("Kategoriyasi: ")
                Product.create(name, stock, price, category)
            case 3:
                product_id = input("O'zgartirmoqchi bo‘lgan mahsulot IDsi: ")
                field = input("Qaysi ustunni o‘zgartirmoqchisiz? (name, stock, price, category): ")
                value = input("Yangi qiymat: ")
                Product.update(product_id, field, value)
            case 4:
                product_id = input("Qaysi mahsulotni o‘chirmoqchisiz? (ID): ")
                Product.delete(product_id)
            case 5:
                return
if __name__ == "__main__":
    product_crud()