import pyodbc
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-ORJ51G8\SQLEXPRESS;'
                      'Database=UPair;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()

#cursor.execute('SELECT * FROM dbo.STUDENT')

#for row in cursor:
  #   print(row)

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


def getShared(user, student_id):
    shared = cursor.execute("""
    select StudentID
    from StudentClass
    where CourseID in 
    (select CourseID
    from StudentClass
    where StudentID = ?)
    group by StudentID
    having COUNT(StudentID) >= 2;
    """, student_id)
    if shared == 'NULL':
        return 0
    rows = list()
    for row in shared:
        rows.append(row)
    return rows
