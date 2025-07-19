from base import Parent

class Order(Parent):


    @staticmethod
    def create(product, total, user, state=1):
        with Order.connect() as conn:
            with conn.cursor() as cursor:
                sql = "INSERT INTO orders (product, total, user, state) VALUES (%s, %s, %s, %s)"
                cursor.execute(sql, (product, total, user, state))
                conn.commit()

    @staticmethod
    def read():
        with Order.connect() as conn:
            with conn.cursor() as cursor:
                sql = "SELECT * FROM orders"
                cursor.execute(sql)
                return cursor.fetchall()

    @staticmethod
    def update(order_id, field, value):
        with Order.connect() as conn:
            with conn.cursor() as cursor:
                sql = f"UPDATE orders SET {field} = %s WHERE id = %s"
                cursor.execute(sql, (value, order_id))
                if cursor.rowcount:
                    print("Buyurtma o‘zgartirildi.")
                else:
                    print("Bunday buyurtma topilmadi.")
                conn.commit()

    @staticmethod
    def delete(order_id):
        with Order.connect() as conn:
            with conn.cursor() as cursor:
                sql = "DELETE FROM orders WHERE id = %s"
                cursor.execute(sql, (order_id,))
                if cursor.rowcount:
                    print("Buyurtma o‘chirildi.")
                else:
                    print("Bunday buyurtma yo‘q.")
                conn.commit()
def order_crud():
    habar = """
    Buyurtma CRUD amallaridan birini tanlang:
        1. Ko'rish
        2. Kiritish
        3. O'zgartirish
        4. O'chirish
        5. Chiqish
    """

    while True:
        tanlov = int(input(habar))

        match tanlov:
            case 1:
                for order in Order.read():
                    print(f"{order['id']}: {order['product']} ({order['total']} dona) - {order['user']} - State: {order['state']}")
            case 2:
                product = input("Mahsulot nomi: ")
                total = int(input("Sonini kiriting: "))
                user = input("Ismingiz: ")
                Order.create(product, total, user)
            case 3:
                order_id = input("O‘zgartirmoqchi bo‘lgan order ID si: ")
                field = input("Qaysi ustunni o‘zgartirmoqchisiz? (product, total, user, state): ")
                value = input("Yangi qiymat: ")
                Order.update(order_id, field, value)
            case 4:
                order_id = input("O‘chirmoqchi bo‘lgan order ID si: ")
                Order.delete(order_id)
            case 5:
                break

if __name__ == "__main__":
    order_crud()