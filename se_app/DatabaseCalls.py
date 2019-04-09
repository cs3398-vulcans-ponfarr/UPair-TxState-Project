import pyodbc
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-ORJ51G8\SQLEXPRESS;'
                      'Database=UPair;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute('SELECT * FROM dbo.STUDENT')

for row in cursor:
    print(row)

def getMessage(user, target_user, school_id):
    message = cursor.execute("""
    select MessageText
      from AUTO_MESSAGES
     where SchoolID = ?
       and MessageID = 1
    """, school_id)
    to_data = cursor.execute("""
    select FirstName +' '+LastName as Name, Email
      from STUDENT
     where StudentID = ?
     and SchoolID = ?
    """, user,school_id).fetchone()
    from_data = cursor.execute("""
    select FirstName +' '+LastName as Name, Email
      from STUDENT
     where StudentID = ?
     and SchoolID = ?
    """, target_user,school_id).fetchone()
    message.format(user=to_data.Name, target_user=from_data.Name, \
                   target_user_email=from_data.Email)
return message
