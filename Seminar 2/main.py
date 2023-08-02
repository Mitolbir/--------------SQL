import pymysql
from config import host, user, password, db_name

try:
    connection = pymysql.connect(
        host = host,
        port = 3306,
        user = user,
        password = password,
        database = db_name,
        cursorclass = pymysql.cursors.DictCursor
    )
    print("Connected")

    try:
        cursor = connection.cursor()

        #Дроп таблицы
        drop_query = """DROP TABLE IF EXISTS test"""
        cursor.execute(drop_query)

        #Создаем таблицу. Для многострочного запроса используем """ запрос """#
        create_query = """CREATE TABLE IF NOT EXISTS test
                        (id INT PRIMARY KEY AUTO_INCREMENT,
                        firstname VARCHAR(45));"""
        cursor.execute(create_query)
        print("Table created")

        #Занесение информации
        insert_query = """INSERT test(firstname)
                        VALUES ("Anton"),("Alex"),("Misha");"""
        cursor.execute(insert_query)
        connection.commit() #для insert, update и delete

        # Обновление информации
        update_query = """UPDATE test SET firstname = 'TEST' WHERE id = 1;"""
        cursor.execute(update_query)
        connection.commit()

        # Удаление информации
        delete_query = """DELETE FROM test WHERE id = 3;"""
        cursor.execute(delete_query)
        connection.commit()

        # Чтение информации (select)
        select_query = """SELECT * FROM test;"""
        cursor.execute(select_query)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        print(rows)

    finally:
        connection.close()

except Exception as ex:
    print(ex)
    print("Refused")