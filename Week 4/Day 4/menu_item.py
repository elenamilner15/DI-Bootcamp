import psycopg2
from db_connection import connect_to_db


class MenuItem:
    connection = connect_to_db()
    def __init__(self, item_name, item_price):
        self.item_name = item_name
        self.item_price = item_price        

    def save(self):
        query = "INSERT INTO menu_items (item_name, item_price) VALUES (%s, %s)"       
        with self.connection.cursor() as cursor:
            cursor.execute(query, (self.item_name, self.item_price))
            self.connection.commit()

    def update(self, new_item_name, new_item_price):
        query = "UPDATE menu_items SET item_name = %s, item_price = %s WHERE item_name = %s AND item_price = %s;"
        with self.connection.cursor() as cursor:
            cursor.execute(query, (new_item_name, new_item_price, self.item_name, self.item_price))
            self.connection.commit()
        

    def delete(self):
        query = "DELETE FROM menu_items WHERE item_name ILIKE %s"
        with self.connection.cursor() as cursor:
            cursor.execute(query, (self.item_name,))
        self.connection.commit()
    



















