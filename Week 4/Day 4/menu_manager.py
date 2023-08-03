import psycopg2
from db_connection import connect_to_db

class MenuManager:
    connection = connect_to_db()
    def __init__(self):
        pass
       
    
    
    def all_items(self):
        query = "SELECT * FROM menu_items order by item_id"
        with self.connection .cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
            for item in result:
                formatted_string = f"{item[0]}.   {item[1]}   price {item[2]} NIS"                
                print(formatted_string)


    
    def one_item(self, item_name):
        query = "SELECT * FROM Menu_Items WHERE item_name ILIKE %s"
        with self.connection .cursor() as cursor:
            cursor.execute(query, (item_name,))
            item = cursor.fetchone()
        if item:
            formatted_string = f"#{item[0]}   {item[1]}   price {item[2]} NIS"
            print(formatted_string)
        else:
            print(f"No item found with the name '{item_name}'.")