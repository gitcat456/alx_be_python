from db_config import mydb

cursor = mydb.cursor()

create_table_query = """
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL
)
"""

cursor.execute(create_table_query)
cursor.execute("SHOW TABLES")

print(cursor.fetchall())

cursor.close()
mydb.close()