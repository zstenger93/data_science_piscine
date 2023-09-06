import psycopg2

dbname = "piscineds"
user = "zstenger"
password = "msp"
host = "localhost"
port = "5432"

with open("create_tables.sql", "r") as sql_file:
    sql_script = sql_file.read()

try:
    conn = psycopg2.connect(
        dbname=dbname,
        user=user,
        password=password,
        host=host,
        port=port
    )

    # Open a cursor to execute SQL commands
    cursor = conn.cursor()
    cursor.execute(sql_script)
    conn.commit()

    print("SQL script executed successfully!")

except Exception as e:
    print(f"Error: {str(e)}")

finally:
    cursor.close()
    conn.close()
