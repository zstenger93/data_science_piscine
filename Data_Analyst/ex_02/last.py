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

    avg_cart_prices = [row[1] for row in data]

    plt.figure(figsize=(10, 6))
    plt.boxplot(avg_cart_prices, vert=False, widths=0.5, notch=True,
                boxprops=dict(facecolor='lightblue', edgecolor='black'),
                flierprops=dict(marker='D', markersize=8, markerfacecolor='lightgray', markeredgecolor='none'),
                patch_artist=True, whis=0.2)
    plt.xticks(np.arange(int(min(avg_cart_prices)), int(max(avg_cart_prices)) + 1, step=2))
    plt.tight_layout()
    plt.xlim(min(avg_cart_prices) - 1, max(avg_cart_prices) + 1)
    plt.yticks([])
    plt.show()
except Exception as e:
    print(f"Error: {e}")
