from base import Parent

class Cart(Parent):
    file_name = "cart.json"

    @staticmethod
    def add_to_cart(user_id, product_id, quantity):
        with Cart.connect() as conn:
            with conn.cursor() as cursor:
                sql = """
                INSERT INTO cart(user_id, product_id, quantity)
                VALUES (%s, %s, %s)
                ON DUPLICATE KEY UPDATE quantity = quantity + %s
                """
                cursor.execute(sql, (user_id, product_id, quantity, quantity))
                conn.commit()
                print("✅ Mahsulot savatchaga qo‘shildi")

    @staticmethod
    def view_cart(user_id):
        with Cart.connect() as conn:
            with conn.cursor() as cursor:
                sql = """
                SELECT p.name, c.quantity, p.price, (c.quantity * p.price) as total
                FROM cart c
                JOIN products p ON c.product_id = p.id
                WHERE c.user_id = %s
                """
                cursor.execute(sql, (user_id,))
                return cursor.fetchall()

    @staticmethod
    def remove_from_cart(user_id, product_id):
        with Cart.connect() as conn:
            with conn.cursor() as cursor:
                sql = "DELETE FROM cart WHERE user_id = %s AND product_id = %s"
                cursor.execute(sql, (user_id, product_id))
                if cursor.rowcount:
                    print("🗑️ Mahsulot savatchadan o‘chirildi")
                else:
                    print("❌ Bunday mahsulot savatchada yo‘q")
                conn.commit()
