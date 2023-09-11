import psycopg2
import matplotlib.pyplot as plt

dbname = "piscineds"
user = "zstenger"
password = "msp"
host = "localhost"
port = "5432"

try:
    with open("frequency.sql", "r") as sql_file:
        sql_script1 = sql_file.read()
    with open("monetary.sql", "r") as sql_file:
        sql_script2 = sql_file.read()
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
    cursor.execute(sql_script1)
    print("SQL script 1 executed successfully!")
    data_frequency = cursor.fetchall()
    cursor.execute(sql_script2)
    print("SQL script 2 executed successfully!")
    data_monetary = cursor.fetchall()
    print("Data has been fetched from the table.")
    conn.commit()
    cursor.close()
    conn.close()

    frequency = [row[1] for row in data_frequency]
    monetary = [row[1] for row in data_monetary]

    fig, axs = plt.subplots(1, 2, figsize=(15, 6))

    axs[0].grid(True, zorder=-1)
    axs[0].hist(frequency, bins=5, edgecolor='k')
    axs[0].set_ylabel('customers')
    axs[0].set_xlabel('frequency')

    axs[1].grid(True, zorder=-1)
    axs[1].hist(monetary, bins=5, edgecolor='k')
    axs[1].set_ylabel('customers')
    axs[1].set_xlabel('monetary value in A')

    for ax in axs:
        ax.yaxis.grid(True, linestyle='-', alpha=0.7)
        ax.set_axisbelow(True)
    plt.show()

except Exception as e:
    print(f"Error: {e}")
