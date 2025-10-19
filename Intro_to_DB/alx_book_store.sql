import mysql_connector_python

mydb = mysql.connector.connect(
    host="localhost",
    user="Astax",
    password="Pt$#523jI",
    database="alx_book_store"
)

cursor = mydb.cursor()

table_definitions = [

    """
    CREATE TABLE IF NOT EXISTS Authors (
        author_id INT PRIMARY KEY,
        author_name VARCHAR(215)
    )

    """,

    """
    CREATE TABLE IF NOT EXISTS Books (
        book_id INT PRIMARY KEY,
        title VARCHAR(130),
        author_id INT,
        price DOUBLE,
        publication_date DATE,
        FOREIGN KEY (author_id) REFERENCES Authors(author_id)
    )

    """,

    """
    CREATE TABLE IF NOT EXISTS Customers (
        customer_id INT PRIMARY KEY,
        customer_name VARCHAR(215),
        address TEXT
    )
    """,

    """
    CREATE TABLE IF NOT EXISTS Orders (
        order_id INT PRIMARY KEY,
        customer_id INT,
        order_date DATE,
        FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
    )
    """,

    """
    """
]