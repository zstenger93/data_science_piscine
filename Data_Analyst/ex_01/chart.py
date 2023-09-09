import psycopg2
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

dbname = "piscineds"
user = "zstenger"
password = "msp"
host = "localhost"
port = "5432"

try:
    with open("chart.sql", "r") as sql_file:
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
    cursor.close()
    conn.close()
    
    purchase_counts = {}
    
    for event_time, event_type in data:
        if event_type == 'purchase':
            year, month, day = event_time.year, event_time.month, event_time.day
            date = datetime(year, month, day)
            date_str = date.strftime('%Y-%m-%d')
            if month >= 10 or month <= 1:
                if date_str not in purchase_counts:
                    purchase_counts[date_str] = 0
                purchase_counts[date_str] += 1
    
    sorted_counts = sorted(purchase_counts.items())
    dates, counts = zip(*sorted_counts)
    
    plt.figure(figsize=(12, 8))
    plt.plot(dates, counts, linestyle='-')
    plt.ylabel("Number of customers")
    plt.gca().yaxis.set_major_formatter(FuncFormatter(lambda x, pos: f'{int(x / 10)}'))
    tick_positions = [0, len(dates) // 4, 2 * len(dates) // 4, 3 * len(dates) // 4]
    tick_labels = ["Oct", "Nov", "Dec", "Jan"]
    plt.xticks(tick_positions, tick_labels)
    plt.xlim(dates[0], dates[-1])
    plt.show()
except Exception as e:
    print(f"Error: {e}")