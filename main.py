from users import User, user_crud
from utilities import menu
from orders import order_crud
from products import Product,product_crud
from category import Category,category_crud
from cart import Cart
def admin_menu():
    while True:
        habar = """
    🛠️ Admin panel:
        1. Foydalanuvchilarni boshqarish
        2. Mahsulotlarni boshqarish
        3. Buyurtmalarni ko‘rish
        0. Chiqish
        """
        tanlov = menu(habar, range(0, 4))
        if tanlov == 1:
            user_crud()
        elif tanlov == 2:
            product_crud()
        elif tanlov == 3:
            order_crud()
        elif tanlov == 0:
            break

    


def user_menu(user_id):
    habar = """
    Amallardan birini tanlang:
        1. Mahsulotni ko'rish
        2. Mahsulot qidirish
        3. Mahsulotni filtrlash            
        4. Savatchaga qo'shish
        5. Savatchani ko'rish (Har biri va Jami mahsulot summasi)
        6. Savatchadan o'chirish
        7. Profil
        0. Chiqish
        """
    while True:
        tanlov = menu(habar, range(0, 8))

        if tanlov == 1:
            for row in Product.read():
                print(row)

        elif tanlov == 2:
            name = input("Qidirmoqchi bo'lgan mahsulot nomi: ")
            for row in Product.search("name", name):
                print(row)

        elif tanlov == 3:
            for row in Category.read():
                print(row)
            category_id = int(input("Kategoriya ID sini kiriting: "))
            rows = Product.filtrlash(category_id)
            if rows:
                for row in rows:
                    print(row)
            else:
                print("Ushbu kategoriya bo‘yicha ma’lumot topilmadi.")

        elif tanlov == 4:
            product_id = int(input("Qo‘shmoqchi bo‘lgan mahsulot ID sini kiriting: "))
            quantity = int(input("Nechta qo‘shmoqchisiz? "))
            Cart.add_to_cart(user_id, product_id, quantity)

        elif tanlov == 5:
            cart_items = Cart.view_cart(user_id)
            if cart_items:
                total_sum = 0
                for item in cart_items:
                    print(f"Mahsulot: {item['name']}, Soni: {item['quantity']}, Narxi: {item['price']}, Jami: {item['total']}")
                    total_sum += item['total']
                print(f"Umumiy summa: {total_sum} so‘m")
            else:
                print("Savatcha bo‘sh")

        elif tanlov == 6:
            product_id = int(input("Qaysi mahsulotni o‘chirmoqchisiz? ID sini kiriting: "))
            Cart.remove_from_cart(user_id, product_id)

        elif tanlov == 7:
            user = User.read_one(user_id)
            print(f"Foydalanuvchi: {user['username']}, Role: {user['role']}")

        elif tanlov == 0:
            return

while True:
    habar = """
        Bittasini tanlang:
            1. Kirish
            2. Ro'yxatdan o'tish
            3. Chiqish
        """
    tanlov = menu(habar, range(1,4))

    if tanlov == 1:
        username = input("Login kiriting: ")
        password = input("Parolni kiriting: ")
        user_id, role = User.login(username, password)
        if user_id:
            if role == "admin":
                admin_menu()
            else:
                user_menu(user_id)

    elif tanlov == 2:
        username = input("Login kiriting")
        password = input("Parolni kiriting: ")
        if User.create(username,password):
            print("Ro'yxatdan o'tdingiz")
    else:
        break