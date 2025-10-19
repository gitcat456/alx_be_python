from db_config import mydb

cursor = mydb.cursor()

#query execution
cursor.execute("SELECT * FROM student ")

#fetch all results
student = cursor.fetchall()
for stud in student:
    print(stud)
    
    
cursor.close()
mydb.close()
