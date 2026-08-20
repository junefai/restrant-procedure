import pyodbc

conn = pyodbc.connect(
    "DRIVER={ODBC Driver 18 for SQL Server};"
    "SERVER=localhost,1433;"
    "DATABASE=master;"
    "UID=ccc;"
    "PWD=xxxxx;"
    "TrustServerCertificate=yes;"
)
cursor=conn.cursor()
Food = "Apple Pie"
quantity=5
cursor.execute("exec [placed_order]@FoodName=?,@quantity=?",Food,quantity)
results=cursor.fetchone()
if results is None:
    print(f"not_available")
else:
    print(results)
conn.commit()    
