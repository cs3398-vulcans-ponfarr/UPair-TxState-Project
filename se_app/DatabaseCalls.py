import pyodbc
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-ORJ51G8\SQLEXPRESS;'
                      'Database=UPair;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute('SELECT StudentID FROM dbo.StudentClass')

#Needs to be translated into a pyodbc sql statement.
#WHERE COURSEID in

    #(SELECT COURSEID

    #from STUDENTCLASS

    #WHERE STUDENTID = 'A00000002')

#GROUP BY STUDENTID

#HAVING COUNT(STUDENTID) >= 2;




for row in cursor:
    print(row)