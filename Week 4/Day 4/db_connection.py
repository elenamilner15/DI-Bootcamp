import psycopg2

def connect_to_db():
    connection = None
    try:
        connection = psycopg2.connect(
            database='Menu',
            user='postgres',
            password='test',
            host='localhost'            
        )
        return connection
    except psycopg2.Error as e:
        print("Error connecting to the database:", e)
        return None