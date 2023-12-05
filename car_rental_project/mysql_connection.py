import mysql.connector

# Replace these values with your MySQL credentials
host = 'localhost'
user = 'root'
password = ''
database = 'car_rental_db'

# Establish a connection to MySQL
try:
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    if connection.is_connected():
        print("Connected to MySQL!")

    # Execute queries or perform operations here
    
except mysql.connector.Error as e:
    print(f"Error connecting to MySQL: {e}")

finally:
    # Close the connection when done
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("MySQL connection closed.")
