import psycopg2
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


dbname = "piscineds"
user = "zstenger"
password = "msp"
host = "localhost"
port = "5432"

try:
    with open("elbowPresley.sql", "r") as sql_file:
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

    wss = []
    for k in range(1, 11):
        kmeans = KMeans(n_clusters=k, random_state=0, n_init=10).fit(data)
        wss.append(kmeans.inertia_)

    plt.plot(range(1, 11), wss)
    plt.xlabel("Number of clusters")
    plt.title("The Elbow Method")
    plt.show()
except Exception as e:
    print(f"Error: {e}")
