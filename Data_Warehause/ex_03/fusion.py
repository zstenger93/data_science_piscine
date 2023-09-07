import psycopg2

dbname = "piscineds"
user = "zstenger"
password = "msp"
host = "localhost"
port = "5432"

try:
    with open("fusion.sql", "r") as sql_file:
        sql_script = sql_file.read()
    print("SQL code have been imported!")
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
    data = cursor.fetchall()
    conn.commit()
    print("SQL script executed successfully!")
except Exception as e:
    print(f"Error: {str(e)}")

finally:
    cursor.close()
    conn.close()