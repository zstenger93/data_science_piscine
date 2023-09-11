import psycopg2
import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict

dbname = "piscineds"
user = "zstenger"
password = "msp"
host = "localhost"
port = "5432"

try:
    with open("chart_filled.sql", "r") as sql_file:
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
    
    daily_sales = defaultdict(float)
    daily_purchases = defaultdict(int)
    
    for user_id, event_time, event_type, price in data:
        if event_type == 'purchase':
            date_str = event_time.strftime('%Y-%m-%d')
            daily_sales[date_str] += price
            daily_purchases[date_str] += 1
    
    dates = list(daily_sales.keys())
    
    average_spend_per_customer = [daily_sales[date] / daily_purchases[date] * 10 for date in dates]
    
    plt.figure(figsize=(10, 6))
    plt.plot(dates, average_spend_per_customer, linestyle='-')
    plt.fill_between(dates, average_spend_per_customer, color='blue', alpha=0.3)
    plt.ylabel("Average Spend/Customer (in Altairian Dollars)")
    tick_positions = [0, len(dates) // 4, 2 * len(dates) // 4, 3 * len(dates) // 4]
    tick_labels = ["Oct", "Nov", "Dec", "Jan"]
    plt.xticks(tick_positions, tick_labels)
    plt.yticks(np.arange(0, max(average_spend_per_customer) + 1, 5))
    plt.xlim(dates[0], dates[-1])
    plt.ylim(0)
    plt.show()
except Exception as e:
    print(f"Error: {e}")