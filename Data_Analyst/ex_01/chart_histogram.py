import psycopg2
from datetime import datetime
import matplotlib.pyplot as plt
from collections import defaultdict

dbname = "piscineds"
user = "zstenger"
password = "msp"
host = "localhost"
port = "5432"

try:
    with open("chart_histogram.sql", "r") as sql_file:
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
    
    monthly_sales = defaultdict(float)
    
    for event_time, event_type, price in data:
        if event_type == 'purchase':
            year, month, day = event_time.year, event_time.month, event_time.day
            month_str = datetime(year, month, 1).strftime('%b')
            monthly_sales[month_str] += price
    
    months = ['Oct', 'Nov', 'Dec', 'Jan']
    sales = [monthly_sales[month] for month in months]
    
    plt.figure(figsize=(10, 6))
    plt.bar(months, sales)
    plt.ylabel("Total Sales (in Altairian Dollars)")
    plt.show()
except Exception as e:
    print(f"Error: {e}")
