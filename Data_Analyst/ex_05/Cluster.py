import psycopg2
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

dbname = "piscineds"
user = "zstenger"
password = "msp"
host = "localhost"
port = "5432"

try:
    with open("Cluster.sql", "r") as sql_file:
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
    data = [(row[2], row[3], row[4]) for row in data]

    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data)

    
    num_clusters = 5 
    kmeans = KMeans(n_clusters=num_clusters, random_state=42, n_init = 10)
    cluster_labels = kmeans.fit_predict(scaled_data)

    plt.figure(figsize=(10, 6))
    for i in range(num_clusters):
        cluster_points = np.array([data[j] for j in range(len(data)) if cluster_labels[j] == i])
        plt.scatter(cluster_points[:, 0], cluster_points[:, 1], s=100, alpha=0.7, label=f'Cluster {i+1}')

    for i, txt in enumerate(categories):
        plt.annotate(f"{txt}\n{user_counts[i]} user", (data[i][0], data[i][1]), fontsize=10, ha='center')

    plt.xlabel("Months Purchased")
    plt.ylabel("Average Purchase Frequency")
    plt.title("Cluster Visualization")
    plt.legend()
    plt.grid(True)
    plt.show()

except Exception as e:
    print(f"Error: {e}")