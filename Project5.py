import mysql.connector
from mysql.connector import Error
import re

db_name = 'Module 6: Project'
user = 'root'
password = 'password'   # Not My Real Password
host = 'localhost'

email_regex = r'^[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}$'
phone_regex = r'^\+?1?\d{9,15}$'

def validate_email(email):
    return re.match(email_regex, email)

def validate_phone_number(phone):
    return re.match(phone_regex, phone)

def create_customer(conn, name, email, phone):
    try:
        cursor = conn.cursor()
        sql = "INSERT INTO Customers (name, email, phone) VALUES (%s, %s, %s)"
        cursor.execute(sql, (name, email, phone))
        conn.commit()
        return cursor.lastrowid
    except Error as e:
        print(f"Error Creating Csutomer: {e}")
    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()

def read_customer(conn, customer_id):
    try:
        cursor = conn.cursor(dictionary=True)
        sql = "SELECT * FROM Customers WHERE id = %s"
        cursor.execute(sql, (customer_id,))
        return cursor.fetchone()
    except Error as e:
        print(f"Error Reading Customer: {e}")
    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()

def update_customer(conn, customer_id, name, email, phone):
    try:
        cursor = conn.cursor()
        sql = "UPDATE Customers SET name = %s, email = %s, phone = %s WHERE id = %s"
        cursor.execute(sql, (name, email, phone, customer_id))
        conn.commit()
    except Error as e:
        print(f"Error Updating Customer: {e}")
    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()

def delete_customer(conn, customer_id):
    try:
        cursor = conn.cursor()
        sql = "DELETE FROM Customers WHERE id = %s"
        cursor.execute(sql, (customer_id,))
        conn.commit()
    except Error as e:
        print(f"Error Deleting Customer: {e}")
    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()

def create_customer_account(conn, customer_id, username, password):
    try:
        cursor = conn.cursor()
        sql = "INSERT INTO CustomerAccounts (customer_id, username, password) VALUES (%s, %s, %s)"
        cursor.execute(sql, (customer_id, username, password))
        conn.commit()
        return cursor.lastrowid
    except Error as e:
        print(f"Error Creating Customer Cccount: {e}")
    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()

def read_customer_account(conn, customer_account_id):
    try:
        cursor = conn.cursor(dictionary=True)
        sql = "SELECT * FROM CustomerAccounts WHERE id = %s"
        cursor.execute(sql, (customer_account_id,))
        return cursor.fetchone()
    except Error as e:
        print(f"Error Reading Customer Account: {e}")
    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()

def update_customer_account(conn, customer_account_id, username, password):
    try:
        cursor = conn.cursor()
        sql = "UPDATE CustomerAccounts SET username = %s, password = %s WHERE id = %s"
        cursor.execute(sql, (username, password, customer_account_id))
        conn.commit()
    except Error as e:
        print(f"Error Updating Csutomer Account: {e}")
    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()

def delete_customer_account(conn, customer_account_id):
    try:
        cursor = conn.cursor()
        sql = "DELETE FROM CustomerAccounts WHERE id = %s"
        cursor.execute(sql, (customer_account_id,))
        conn.commit()
    except Error as e:
        print(f"Error Deleting Customer Account: {e}")
    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()

def create_product(conn, name, price):
    try:
        cursor = conn.cursor()
        sql = "INSERT INTO Products (name, price) VALUES (%s, %s)"
        cursor.execute(sql, (name, price))
        conn.commit()
        return cursor.lastrowid
    except Error as e:
        print(f"Error Creating Product: {e}")
    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()

def read_product(conn, product_id):
    try:
        cursor = conn.cursor(dictionary=True)
        sql = "SELECT * FROM Products WHERE id = %s"
        cursor.execute(sql, (product_id,))
        return cursor.fetchone()
    except Error as e:
        print(f"Error Rading Product: {e}")
    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()

def update_product(conn, product_id, name, price):
    try:
        cursor = conn.cursor()
        sql = "UPDATE Products SET name = %s, price = %s WHERE id = %s"
        cursor.execute(sql, (name, price, product_id))
        conn.commit()
    except Error as e:
        print(f"Error Updating Product: {e}")
    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()

def delete_product(conn, product_id):
    try:
        cursor = conn.cursor()
        sql = "DELETE FROM Products WHERE id = %s"
        cursor.execute(sql, (product_id,))
        conn.commit()
    except Error as e:
        print(f"Error Deleting Product: {e}")
    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()

def list_products(conn):
    try:
        cursor = conn.cursor(dictionary=True)
        sql = "SELECT * FROM Products"
        cursor.execute(sql)
        return cursor.fetchall()
    except Error as e:
        print(f"Error listing Products: {e}")
    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()




try:
    conn = mysql.connector.connect(
        database = db_name,
        user = user,
        password = password,
        host = host
    )

    if conn.is_connected():
        print('Connected to MySQL Database')

    new_customer_id = create_customer(conn, "John Doe", "john@doe.com", "1234567890")
    if new_customer_id:
        print(f"Created Customer with ID: {new_customer_id}")

    customer_details = read_customer(conn, 1234567890)
    if customer_details:
        print("Customer Details:")
        print(customer_details)

    update_customer(conn, 1234567890, "John Smith", "john@smith.com", "1234567890")

    delete_customer(conn, 1234567890)

finally:
    if conn and conn.is_connected():
        conn.close()
        print('MySQL Connection is Now Closed')
