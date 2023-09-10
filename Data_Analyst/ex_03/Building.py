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

    total_customers_per_day = defaultdict(int)
    customer_spending = defaultdict(float)

    for row in data:
        event_time, user_id, event_type, price = row
        if event_type == 'purchase':
            customer_spending[user_id] += price
            if event_time.month == 10:
                total_customers_per_day[event_time.day] += 1

    days_in_october = list(total_customers_per_day.keys())
    total_customer_counts = [count for count in total_customers_per_day.values()]

    customer_ids = list(customer_spending.keys())
    spending_values = list(customer_spending.values())

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    ax1.bar(days_in_october, total_customer_counts, color='skyblue')
    ax1.set_xlabel('frequency')
    ax1.set_ylabel('customers')
    ax1.grid(axis='y', linestyle='--', alpha=0.7)

    ax2.bar(spending_values, customer_ids, color='skyblue')
    ax2.set_xlabel('monetary value in A')
    ax2.set_ylabel('customers')
    ax2.grid(axis='y', linestyle='--', alpha=0.7)

    plt.tight_layout()
    plt.show()

except Exception as e:
    print(f"Error: {e}")
