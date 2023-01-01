from models.db_config import db_connect


def insert_order(email_user, order_id, photo_id, price, size, quantity, date):
    connection = db_connect('root', 'root', 'localhost', 'php_db')
    cursor = connection.cursor()
    sql = "INSERT INTO Orders (email_user, order_id, photo_id, quantity, size, price, date) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    values = (email_user, order_id, photo_id, quantity, size, price, date)
    cursor.execute(sql, values)
    connection.commit()
    cursor.close()
    connection.close()


def select_orders(email_user):
    connection = db_connect('root', 'root', 'localhost', 'php_db')
    cursor = connection.cursor()
    sql = "SELECT * FROM Orders INNER JOIN Photos ON Photos.id = Orders.photo_id WHERE email_user = %s ORDER BY date DESC, order_id"
    values = (email_user,)
    cursor.execute(sql, values)
    orders = cursor.fetchall()
    cursor.close()
    connection.close()
    return orders
