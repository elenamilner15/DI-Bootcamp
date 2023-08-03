import psycopg2
import requests
import random

def fetch_random_countries(num_countries):
    url = f"https://restcountries.com/v3.1/all"
    response = requests.get(url)
    countries_data = response.json()
    
    random_countries = random.sample(countries_data, num_countries)
    return random_countries


def populate_database(countries_data):
    conn = psycopg2.connect(
        dbname="countries",
        user = 'postgres',
        password='test',
        host='localhost'
    )
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE countries (name VARCHAR(30), capital VARCHAR(30), flag TEXT, subregion VARCHAR(30), population INTEGER)""")
    
    for country in countries_data:
        name = country['name']['common']
        capital = country['capital'][0] if 'capital' in country else ''
        flag = country['flags']['svg'] if 'flags' in country else ''
        subregion = country['subregion'] if 'subregion' in country else ''
        population = country['population'] if 'population' in country else 0

        cursor.execute("INSERT INTO countries VALUES (%s, %s, %s, %s, %s)",
                       (name, capital, flag, subregion, population))

    conn.commit()
    conn.close()
    
    
    
num_countries_to_fetch = 10

random_countries = fetch_random_countries(num_countries_to_fetch)
populate_database(random_countries)

print(f"{num_countries_to_fetch} random countries added to the database.")