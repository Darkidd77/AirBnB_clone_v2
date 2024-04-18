-- Creates a MySQL server with:
--   Database hbnb_test_db.
--   User hbnb_test password hbnb_test_pwd in localhost.
--   Grants all privileges hbnb_test on hbnb_test_db.
--   Grants SELECT privilege for hbnb_test on performance_schema.


-- Connect to the MySQL server as root (adjust the credentials if needed)
db = MySQLdb.connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='your_root_password'
)

-- Create cursor object to execute queries
cursor = db.cursor()

-- Create database if it doesn't exist
cursor.execute("CREATE DATABASE IF NOT EXISTS hbnb_test_db")

-- Create user if it doesn't exist & set the password
cursor.execute("CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd'")

-- Grant all privileges hbnb_test_db to hbnb_test
cursor.execute("GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost'")

-- Grant SELECT privilege on performance_schema to hbnb_test
cursor.execute("GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost'")

-- Flush privileges to apply changes
cursor.execute("FLUSH PRIVILEGES")

-- Close cursor and database connection
cursor.close()
db.close()
