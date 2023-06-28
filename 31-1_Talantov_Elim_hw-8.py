# import sqlite3
#
# conn = sqlite3.connect('base.db')
# cursor = conn.cursor()
#
# cursor.execute('''CREATE TABLE IF NOT EXISTS countries (
#                     id INTEGER PRIMARY KEY AUTOINCREMENT,
#                     title TEXT NOT NULL
#                 )''')
#
# countries = [('Страна 1',), ('Страна 2',), ('Страна 3',)]
# cursor.executemany('INSERT INTO countries (title) VALUES (?)', countries)
#
# cursor.execute('''CREATE TABLE IF NOT EXISTS cities (
#                     id INTEGER PRIMARY KEY AUTOINCREMENT,
#                     title TEXT NOT NULL,
#                     area REAL DEFAULT 0,
#                     country_id INTEGER,
#                     FOREIGN KEY (country_id) REFERENCES countries(id)
#                 )''')
#
# cities = [('Город 1', 69.9, 1),
#           ('Город 2', 510.1, 1),
#           ('Город 3', 123.1, 2),
#           ('Город 4', 43.5, 2),
#           ('Город 5', 264.1, 3),
#           ('Город 6', 90.9, 3),
#           ('Город 7', 245.1, 3)]
# cursor.executemany('INSERT INTO cities (title, area, country_id) VALUES (?, ?, ?)', cities)
#
# cursor.execute('''CREATE TABLE IF NOT EXISTS employees (
#                     id INTEGER PRIMARY KEY AUTOINCREMENT,
#                     first_name TEXT NOT NULL,
#                     last_name TEXT NOT NULL,
#                     city_id INTEGER,
#                     FOREIGN KEY (city_id) REFERENCES cities(id)
#                 )''')
#
# employees = [('Элим', 'Талантов', 1),
#              ('Азим', 'Мырзабеков', 1),
#              ('Азирет', 'Толомушов', 1),
#              ('Эшалы', 'Токтомоматов', 2),
#              ('Мартин', 'Макаров ', 3),
#              ('Мартын', 'Константинов ', 4),
#              ('Герман ', 'Костин', 5),
#              ('Флор ', 'Андреев ', 5),
#              ('Артем', 'Рогов ', 6),
#              ('Татьяна', 'Козлова', 6),
#              ('Наоми ', 'Наоми', 7),
#              ('Елена', 'Соколова', 7),
#              ('Генриетта', 'Егорова ', 7),
#              ('Фелиция ', 'Титова', 7),
#              ('Чеслава', 'Алексеева ', 7)]
# cursor.executemany('INSERT INTO employees (first_name, last_name, city_id) VALUES (?, ?, ?)', employees)
#
# conn.commit()
# conn.close()


database = [
    {"id": 1, "имя": "Элим", "фамилия": "Талантов", "страна": "Кыргызстан", "город": "Бишкек", "площадь_города": 127},
    {"id": 2, "имя": "Азим", "фамилия": "Мырзабеков", "страна": "Кыргызстан", "город": "Нарын", "площадь_города": 44.1},
    {"id": 3, "имя": "Джон", "фамилия": "Уик", "страна": "Беларуссия", "город": "Минск", "площадь_города": 348.8},
    {"id": 4, "имя": "Эндрю", "фамилия": "Гарфилд", "страна": "США", "город": "Лос-Анджелес", "площадь_города": 1299.0},
]

print(
    "Выбери сотрудника из списка по id, для выхода из программы введите 0:")
for entry in database:
    print(entry["город"])

selected_id = int(input("Введите id города (для выхода введите 0): "))

while selected_id != 0:
    found_employees = []
    for entry in database:
        if entry["id"] == selected_id:
            found_employees.append(entry)

    if found_employees:
        for employee in found_employees:
            print("Имя:", employee["имя"])
            print("Фамилия:", employee["фамилия"])
            print("Страна:", employee["страна"])
            print("Город проживания:", employee["город"])
            print("Площадь города:", employee["площадь_города"])
            print()
    else:
        print("Сотрудник не найден.")

    selected_id = int(input("Введите id города (для выхода введите 0): "))
