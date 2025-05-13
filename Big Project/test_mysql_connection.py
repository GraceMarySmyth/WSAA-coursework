import mysql.connector
import pymysql
from dbconfig import mysql as dbcreds
'''
print("🔧 Attempting direct MySQL connection...")

try:
    conn = mysql.connector.connect(
        host=dbcreds['host'],
        user=dbcreds['user'],
        password=dbcreds['password'],
        database=dbcreds['database']
    )
    print("✅ Successfully connected to MySQL!")
    cursor = conn.cursor()
    cursor.execute("SHOW TABLES;")
    for table in cursor.fetchall():
        print("📦 Found table:", table[0])
    conn.close()
except Exception as e:
    print("❌ Connection failed:", e)
    '''
conn = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    database='smyth_family_recipes'
)
print("✅ Connected to MySQL using PyMySQL!")
conn.close()

# changed to pymysql. mysql-connectorpython is either not working or stalling silently