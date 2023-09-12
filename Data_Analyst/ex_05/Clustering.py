import psycopg2
import matplotlib.pyplot as plt

dbname = "piscineds"
user = "zstenger"
password = "msp"
host = "localhost"
port = "5432"

try:
    with open("Clustering.sql", "r") as sql_file:
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

    groups = ["inactive_customers", "loyal_customers", "regular_customers", "new_customers"]
    counts = [int(row[1]) for row in data]
    colors = ['grey', 'red', 'green', 'gold']

    plt.figure(figsize=(20, 8))
    plt.barh(groups, counts)
    plt.xlabel("Number of Customers")
    plt.gca().invert_yaxis()
    plt.gca().get_xaxis().get_major_formatter().set_scientific(False)

    for i, count in enumerate(counts):
        plt.barh(groups[i], counts[i], color=colors[i])
        plt.text(count, i, str(count), va='center', fontsize=12, color='black', weight='bold')
    plt.yticks(range(len(groups)), groups, fontsize=12, weight='bold')

    plt.tight_layout()
    plt.show()

except Exception as e:
    print(f"Error: {e}")
