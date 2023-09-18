import psycopg2
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

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

    dataframe = pd.DataFrame(data, columns=['Month', 'Day', 'User_ID'])

    # Calculate centroids (average month) for each unique month
    unique_months = dataframe['Month'].unique()
    centroids = []
    for month in unique_months:
        centroid_month = dataframe[dataframe['Month'] == month]['Month'].mean()
        centroids.append(centroid_month)

    # Apply K-Means clustering
    kmeans = KMeans(n_clusters=len(centroids), random_state=0, n_init=10)
    clusters = kmeans.fit_predict(dataframe[['Month', 'Day']])

    # Add cluster assignments to the DataFrame
    dataframe['Cluster'] = clusters

    # Extract cluster centers (centroids)
    centroids = kmeans.cluster_centers_

    # Visualize the clusters and centroids
    plt.scatter(dataframe['Month'], dataframe['Day'], c=dataframe['Cluster'], cmap='rainbow', marker='o', alpha=0.5)
    plt.scatter(centroids[:, 0], centroids[:, 1], c='black', marker='X', s=100)
    plt.title('K-Means Clustering with Centroids (One for Each Month)')
    plt.xlabel('Month')
    plt.ylabel('Day')
    plt.show()

except Exception as e:
    print(f"Error: {e}")