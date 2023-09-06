import psycopg2
from psycopg2 import sql


dbname = "piscineds"
user = "zstenger"
password = "msp"
host = "localhost"
port = "5432"

with open("merge_tables.sql", "r") as sql_file:
    sql_script = sql_file.read()

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    dbname=dbname,
    user=user,
    password=password,
    host=host,
    port=port
)

# Open a cursor to execute SQL commands
cursor = conn.cursor()
cursor.execute(sql_script)
conn.commit()
cursor.close()
conn.close()
