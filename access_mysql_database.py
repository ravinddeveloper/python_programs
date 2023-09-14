import mysql.connector

cnx = mysql.connector.connect(user='root', 
                              password='11111', #enter database password
                              host='127.0.0.1', #port address
                              database='emp')   #database name


cursor = cnx.cursor()
query = ("SELECT stu_id, stu_name, stu_phno FROM student")
cursor.execute(query)

for (stu_id, stu_name, stu_phno) in cursor:
  print("student id : {}, student name :  {} , student phone number:  {}".format(stu_id, stu_name, stu_phno))

print("updated value")
query2 = ("update student set stu_name='ravi' ,stu_phno='83103679' where stu_id='1'")
cursor.execute(query2)

cursor.execute(query)
for (stu_id, stu_name, stu_phno) in cursor:
  print("student id : {}, student name :  {} , student phone number:  {}".format(stu_id, stu_name, stu_phno))

cnx.commit()
cursor.close()
cnx.close()
