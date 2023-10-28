import psycopg2
import matplotlib.pyplot as plt

dbname = "piscineds"
user = "zstenger"
password = "msp"
host = "localhost"
port = "5432"

try:
    with open("pie.sql", "r") as sql_file:
        sql_script = sql_file.read()
    print("SQL code has been imported!")
    conn = psycopg2.connect(
        dbname=dbname,
        user=user,
        password=password,
        host=host,
        port=port
    )
    print("Connected to postgres!")
    cursor = conn.cursor()
    cursor.execute(sql_script)
    print("SQL script executed successfully!")
    data = cursor.fetchall()
    print("Data has been fetched from the table.")
    conn.commit()
    cursor.close()
    conn.close()

    event_colors = {'view': 'blue', 'purchase': 'red', 'remove_from_cart': 'green', 'cart': 'orange'}
    event_types, counts = zip(*data)
    plt.pie(counts, labels=[f"{event_type}" for event_type in event_types],
            autopct='%1.1f%%', startangle=0, colors=[event_colors.get(event, 'gray') for event in event_types])
    plt.axis('equal')
    plt.show()
except Exception as e:
    print(f"Error: {str(e)}")