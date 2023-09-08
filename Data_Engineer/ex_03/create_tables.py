import psycopg2

dbname = "piscineds"
user = "zstenger"
password = "msp"
host = "localhost"
port = "5432"


try:
    with open("create_tables.sql", "r") as sql_file:
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
    print("SQL script executed successfully!")
    data = cursor.fetchall()
    print("Data has been fetched from the table.")
    conn.commit()


except Exception as e:
    print(f"Error: {str(e)}")

finally:
    cursor.close()
    conn.close()
