from db_config import mydb

cursor = mydb.cursor()

update_query = "UPDATE users SET email = %s WHERE username = %s"
values =  ("ojayZe", "saint@gmail.com")

cursor.execute(update_query, values)
mydb.commit()

print(f"{cursor.rowcount} record(s) updated.")

cursor.close()
mydb.close()