import psycopg2
import matplotlib.pyplot as plt
from datetime import datetime

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
    data = cursor.fetchall()
    conn.commit()
    print("SQL script executed successfully!")
    cursor.close()
    conn.close()
    
    purchase_counts = {}
    
    for event_time, event_type in data:
        if event_type == 'purchase':
            # Extract the year, month, and day from the event_time
            year, month, day = event_time.year, event_time.month, event_time.day
            
            # Create a date object with the year, month, and day
            date = datetime(year, month, day)
            
            # Format the date to 'YYYY-MM-DD' string
            date_str = date.strftime('%Y-%m-%d')
            
            # If the date is within the range (October to February), increment the count
            if month >= 10 or month <= 2:
                if date_str not in purchase_counts:
                    purchase_counts[date_str] = 0
                purchase_counts[date_str] += 1
    
    # Extract the dates and counts
    sorted_counts = sorted(purchase_counts.items())
    dates, counts = zip(*sorted_counts)
    
    plt.figure(figsize=(12, 8))
    plt.plot(dates, counts, linestyle='-')
    plt.ylabel("Number of customers")
    plt.xticks(rotation=45)
    plt.gca().get_xaxis().set_major_locator(plt.MaxNLocator(5))
    plt.gca().get_yaxis().set_major_locator(plt.MaxNLocator(5))
    plt.xlim(dates[0], dates[-1])
    plt.tight_layout()
    plt.show()
    
except Exception as e:
    print(f"Error: {e}")