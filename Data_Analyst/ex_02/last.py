import psycopg2
import numpy as np
import matplotlib.pyplot as plt

dbname = "piscineds"
user = "zstenger"
password = "msp"
host = "localhost"
port = "5432"

try:
    with open("last.sql", "r") as sql_file:
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

    user_avg_cart_prices = {}
    for user_id, event_type, price in data:
        if event_type == 'cart':
            if user_id not in user_avg_cart_prices:
                user_avg_cart_prices[user_id] = []
            user_avg_cart_prices[user_id].append(price)

    avg_cart_prices = [np.mean(user_avg_cart_prices[user_id]) for user_id in user_avg_cart_prices.keys()]


    min_value = min(avg_cart_prices)
    max_value = max(avg_cart_prices)

    plt.figure(figsize=(10, 6))
    plt.boxplot(avg_cart_prices, vert=False, widths=0.5, notch=True,
                boxprops=dict(facecolor='lightblue', edgecolor='black'),
                flierprops=dict(marker='D', markersize=8, markerfacecolor='lightgray', markeredgecolor='none'),
                patch_artist=True, whis=0.2)
    plt.xticks(np.arange(int(min_value), int(max_value) + 1, step=2))
    plt.tight_layout()
    plt.xlim(min_value - 1, max_value + 1)
    plt.yticks([])
    plt.show()
except Exception as e:
    print(f"Error: {e}")
