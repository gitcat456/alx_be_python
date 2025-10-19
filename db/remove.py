from db_config import mydb

cursor = mydb.cursor()

deletion_query = "DELETE FROM users WHERE id = %s"
values = values = [(7,), (8,), (9,)]  #list of single-value tuples

cursor.executemany(deletion_query, values)
mydb.commit()

print(f"{cursor.rowcount} row(s) deleted.")

cursor.close()
mydb.close()