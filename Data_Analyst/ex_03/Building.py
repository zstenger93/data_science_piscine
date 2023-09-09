import psycopg2
import matplotlib.pyplot as plt
from collections import defaultdict
from datetime import datetime

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

    # Number of Orders Bar Chart (Frequency)
    order_frequency = defaultdict(int)
    for user_id, event_time, event_type, price in data:
        if event_type == 'purchase':
            # Convert the event_time timestamp to a datetime object
            event_time = datetime.utcfromtimestamp(event_time)
            # Ensure event_time is in the format '%Y-%m-%d'
            date_str = event_time.strftime('%Y-%m-%d')
            order_frequency[date_str] += 1

    order_dates = list(order_frequency.keys())
    order_counts = list(order_frequency.values())

    plt.figure(figsize=(10, 6))
    plt.bar(order_dates, order_counts)
    plt.xlabel("Frequency")
    plt.ylabel("Number of Customers")
    plt.title("Number of Orders by Frequency")

    # Altairian Dollars Spent Bar Chart
    customer_spending = defaultdict(float)
    for user_id, event_time, event_type, price in data:
        if event_type == 'purchase':
            customer_spending[user_id] += price

    customer_ids = list(customer_spending.keys())
    customer_total_spending = list(customer_spending.values())

    plt.figure(figsize=(10, 6))
    plt.bar(customer_ids, customer_total_spending)
    plt.xlabel("Customer IDs")
    plt.ylabel("Altairian Dollars Spent")
    plt.title("Altairian Dollars Spent by Customers")

    plt.tight_layout()
    plt.show()

except Exception as e:
    print(f"Error: {e}")
