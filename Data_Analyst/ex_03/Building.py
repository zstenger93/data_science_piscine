import psycopg2
import matplotlib.pyplot as plt
from collections import defaultdict

dbname = "piscineds"
user = "zstenger"
password = "msp"
host = "localhost"
port = "5432"

try:
    with open("Building.sql", "r") as sql_file:
        sql_script = sql_file.read()
    print("SQL code has been imported!")
    conn = psycopg2.connect(
        dbname=dbname,
        user=user,
        password=password,
        host=host,
        port=port
    )
    print("Connected to PostgreSQL!")
    cursor = conn.cursor()
    cursor.execute(sql_script)
    print("SQL script executed successfully!")
    data = cursor.fetchall()
    print("Data has been fetched from the table.")
    conn.commit()
    cursor.close()
    conn.close()

    total_customers_per_day = defaultdict(int)
    customer_spending = defaultdict(float)

    for row in data:
        event_time, user_id, event_type, price = row


except Exception as e:
    print(f"Error: {e}")
