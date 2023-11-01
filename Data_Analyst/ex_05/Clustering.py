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

    group_names = {
        0: "loyal gold",
        1: "inactive",
        2: "new customer",
        3: "loyal silver",
        4: "loyal platinum"
    }

    data_for_clustering = np.array([[row[1]] for row in data])

    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data_for_clustering)

    num_clusters = 5
    kmeans = KMeans(n_clusters=num_clusters, random_state=42, n_init=10)
    cluster_labels = kmeans.fit_predict(scaled_data)

    cluster_averages = []
    for i in range(num_clusters):
        cluster_points = np.array([data[j][1] for j in range(len(data)) if cluster_labels[j] == i])
        cluster_averages.append(np.mean(cluster_points))
    sorted_indices = np.argsort(cluster_averages)

    sorted_data = [data[idx] for idx in sorted_indices]

    plt.figure(figsize=(10, 6))
    for i, idx in enumerate(sorted_indices):
        cluster_points = np.array([data[j][1] for j in range(len(data)) if cluster_labels[j] == idx])
        color = plt.cm.viridis(i / num_clusters)
        plt.barh(i, np.mean(cluster_points), color=color, alpha=0.7)
        plt.text(np.mean(cluster_points) + 0.8, i, f'{group_names[idx]}', ha='left', va='center', fontsize=10, color='black', weight='bold')


    plt.ylabel("Clusters")
    plt.xlabel("Number of Customers")
    plt.title("Cluster Visualization")
    plt.yticks(range(num_clusters), [f'Cluster {i+1}' for i in range(num_clusters)])
    plt.grid(True)
    plt.show()

except Exception as e:
    print(f"Error: {e}")
