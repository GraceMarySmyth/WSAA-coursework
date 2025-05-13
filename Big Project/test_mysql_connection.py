import mysql.connector
from dbconfig import mysql

print("🔧 Attempting direct MySQL connection...")

try:
    conn = mysql.connector.connect(
        host=mysql['host'],
        user=mysql['user'],
        password=mysql['password'],
        database=mysql['database']
    )
    print("✅ Successfully connected to MySQL!")
    cursor = conn.cursor()
    cursor.execute("SHOW TABLES;")
    for table in cursor.fetchall():
        print("📦 Found table:", table[0])
    conn.close()
except Exception as e:
    print("❌ Connection failed:", e)
