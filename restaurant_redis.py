import pyodbc

conn = pyodbc.connect(
    "DRIVER={ODBC Driver 18 for SQL Server};"
    "SERVER=localhost,1433;"
    "DATABASE=master;"
    "UID=rrr;"
    "PWD=yyyy!;"
    "TrustServerCertificate=yes;"
)
cursor=conn.cursor()

import redis
import json
r = redis.Redis(host='localhost', port=6379)
cursor.execute("select dbo.order_python2();")
results=cursor.fetchall()


for row in results:
    data = json.loads(row[0])
    for menu in data:
        r.hset(
           f"menu:{menu['MenuID']}",
           "data",
            json.dumps(menu))
print(r.hgetall("menu:13"))       



