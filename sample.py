# python sample.py

from dotenv import load_dotenv
load_dotenv()

import psycopg2
import os

# データベースとのコネクションを確立します。
# connection = psycopg2.connect("host=127.0.0.1 dbname=postgres user=postgres password=postgres")
connection = psycopg2.connect(os.getenv('PG_URL'))

# カーソルをオープンします
cursor = connection.cursor()
cursor.execute("SELECT datname FROM pg_database WHERE datistemplate = false;")
query_result = cursor.fetchall()
print(query_result)

