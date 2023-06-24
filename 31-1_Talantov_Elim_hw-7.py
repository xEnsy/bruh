import sqlite3

conn = sqlite3.connect('hw.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS products
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             product_title TEXT NOT NULL,
             price REAL NOT NULL DEFAULT 0.0,
             quantity INTEGER NOT NULL DEFAULT 0)''')

def add_products():
    products = [
        ("Жидкое мыло с запахом ванили", 120.50, 10),
        ("Мыло детское", 80.25, 5),
        ("Шампунь для сухих волос", 150.0, 8),
        ("Зубная паста с мятным ароматом", 70.0, 12),
        ("Маска для лица с экстрактом зеленого чая", 200.0, 3),
        ("Крем для рук с оливковым маслом", 90.0, 15),
        ("Очищающий гель для умывания", 110.0, 6),
        ("Лосьон для тела с алоэ вера", 180.0, 9),
        ("Кондиционер для волос", 130.0, 7),
        ("Масло для ногтей и кутикулы", 95.0, 11),
        ("Скраб для тела с солью Мертвого моря", 250.0, 4),
        ("Тоник для лица с ромашкой", 120.0, 10),
        ("Бальзам для губ с медом", 70.0, 13),
        ("Солнцезащитный крем SPF 50+", 180.0, 8),
        ("Дезодорант-антиперспирант", 100.0, 12)
    ]
    c.executemany("INSERT INTO products (product_title, price, quantity) VALUES (?, ?, ?)", products)
    conn.commit()
def change_quantity(product_id, new_quantity):
    c.execute("UPDATE products SET quantity = ? WHERE id = ?", (new_quantity, product_id))
    conn.commit()

def change_price(product_id, new_price):
    c.execute("UPDATE products SET price = ? WHERE id = ?", (new_price, product_id))
    conn.commit()

def delete_product(product_id):
    c.execute("DELETE FROM products WHERE id = ?", (product_id,))
    conn.commit()

def select_all_products():
    c.execute("SELECT * FROM products")
    products = c.fetchall()
    for product in products:
        print(product)

def select_cheaper_products():
    c.execute("SELECT * FROM products WHERE price < 100.0 AND quantity > 5")
    products = c.fetchall()
    for product in products:
        print(product)

def search_products_by_title(keyword):
    c.execute("SELECT * FROM products WHERE product_title LIKE ?", ('%{}%'.format(keyword),))
    products = c.fetchall()
    for product in products:
        print(product)

add_products()

change_quantity(1, 20)

change_price(2, 90.5)

delete_product(3)

select_all_products()

select_cheaper_products()

search_products_by_title("мыло")

conn.close()