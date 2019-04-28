import pyodbc
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-5E19TC4\SQLEXPRESS;'
                      'Database=UPair;'
                      'Trusted_Connection=yes;')
conn.autocommit = True
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
    message.format(user=to_data.Name, target_user=from_data.Name,
                   target_user_email=from_data.Email)
    return message

def getAccount(email, password):
    account = cursor.execute("""
    select email
    from ACCOUNT
    where Email = ?
    and Password = ?
    """, email, password)
    if account == 'NULL':
        return 0
    rows = list()
    for row in account:
        rows.append(row)
    return rows

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


def Register(school_id, email, student_id, password):
    check_account = cursor.execute("""
    SELECT COUNT(*)
    FROM ACCOUNT
    WHERE Email = ?
    """, email)
    rows = list()
    for row in check_account:
        rows.append(row)
    if rows[0][0] == 0:
        student = cursor.execute("""
        INSERT INTO STUDENT VALUES(
        ?, ?, NULL, NULL, ?)
        """, student_id, email, school_id)
        account = cursor.execute("""
        INSERT INTO ACCOUNT VALUES(
        ?, ?, ?, ?)
        """, email, password, student_id, school_id)
        return True
    return False
    #conn.commit()
#print(getMessage(''))