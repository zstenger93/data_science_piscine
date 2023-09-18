import psycopg2
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Your database connection parameters
dbname = "piscineds"
user = "zstenger"
password = "msp"
host = "localhost"
port = "5432"

try:
    # Connect to the database
    conn = psycopg2.connect(
        dbname=dbname,
        user=user,
        password=password,
        host=host,
        port=port
    )
    print("Connected to PostgreSQL!")

    # Execute your SQL query
    with open("Cluster.sql", "r") as sql_file:
        sql_script = sql_file.read()
    with conn.cursor() as cursor:
        cursor.execute(sql_script)
        data = cursor.fetchall()

    # Create a DataFrame from the SQL query result
    dataframe = pd.DataFrame(data, columns=['purchase_months_category', 'customer_count', 'purchase_months'])

    # Apply K-Means clustering on the DataFrame
    kmeans = KMeans(n_clusters=5, random_state=0, n_init=10)
    clusters = kmeans.fit_predict(dataframe[['customer_count', 'purchase_months']])

    # Add cluster assignments to the DataFrame
    dataframe['Cluster'] = clusters

    # Visualize the clusters
    plt.figure(figsize=(8, 6))

    # Scatter plot
    plt.scatter(dataframe['customer_count'], dataframe['purchase_months'], c=dataframe['Cluster'], cmap='rainbow', marker='o', alpha=0.5)
    plt.title('K-Means Clustering of Customer Categories')
    plt.xlabel('Customer Count')
    plt.ylabel('Purchase Months')
    plt.show()

except Exception as e:
    print(f"Error: {e}")
