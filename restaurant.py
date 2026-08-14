import pyodbc

conn = pyodbc.connect(
    "DRIVER={ODBC Driver 18 for SQL Server};"
    "SERVER=localhost,1433;"
    "DATABASE=master;"
    "UID=SA;"
    "PWD=YourStrongPassword123!;"
    "TrustServerCertificate=yes;"
)
cursor=conn.cursor()
MenuID =4
cursor.execute("exec[order]@MenuID=?",MenuID)
results=cursor.fetchone()

if results is None:  
    print("Food is not available")
else:
    print(results)
