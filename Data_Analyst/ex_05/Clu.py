import psycopg2
import matplotlib.pyplot as plt
import numpy as np

dbname = "piscineds"
user = "zstenger"
password = "msp"
host = "localhost"
port = "5432"

try:
    with open("Clu.sql", "r") as sql_file:
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

    categories = [row[0] for row in data]
    user_counts = [int(row[1]) for row in data]
    months_purchased = [int(row[2]) for row in data]
    avg_purchase_frequency = [float(row[3]) for row in data]

    circle_sizes = [count * 10 for count in user_counts]

    unique_colors = plt.cm.tab20(np.linspace(0, 1, len(categories)))

    normalized_circle_sizes = [count / max(user_counts) * 300 for count in user_counts]

    # Plotting the filled circles and annotations on the graph
    plt.figure(figsize=(10, 6))
    for i, category in enumerate(categories):
        plt.scatter(months_purchased[i], avg_purchase_frequency[i], s=normalized_circle_sizes[i], c=[unique_colors[i]], alpha=0.7)
        plt.annotate(f"{category}\n{user_counts[i]} user", (months_purchased[i], avg_purchase_frequency[i]), 
                    fontsize=10, ha='center')
    # plt.ylim(-8, 22)
    plt.xticks(np.arange(0, max(months_purchased) + 1, step=1))
    plt.xlabel("Months Purchased In")
    plt.ylabel("Average Purchase Frequency")
    plt.title("Groups Visualization")
    plt.grid(True)
    plt.show()

except Exception as e:
    print(f"Error: {e}")
