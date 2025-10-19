from db_config import mydb

cursor = mydb.cursor()

users = [
    ("fred@2ke", "frednyots@gmail.com"),
    ("ojayZe", "ojatmkuu@gmail.com"),
    ("kellykans", "kelly004@gmail.com")
    
]

insert_query = "INSERT INTO users (username, email) VALUES (%s, %s)"
cursor.executemany(insert_query, users)

#Commit changes to the db
mydb.commit()


print(f"{cursor.rowcount} user(s) inserted successfully.")

cursor.close()
mydb.close()