import pyodbc
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-ORJ51G8\SQLEXPRESS;'
                      'Database=UPair;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute('SELECT * FROM dbo.STUDENT')

for row in cursor:
    print(row)