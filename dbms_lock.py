import cx_Oracle

def acquire_lock(connection, lock_name, lock_mode=cx_Oracle.LOCK_MODE_X):
    cursor = connection.cursor()

    # Acquire the lock
    cursor.callproc("DBMS_LOCK.REQUEST", (lock_name, lock_mode))

    # Commit the transaction
    connection.commit()

def release_lock(connection, lock_name):
    cursor = connection.cursor()

    # Release the lock
    cursor.callproc("DBMS_LOCK.RELEASE", (lock_name,))

    # Commit the transaction
    connection.commit()

# Replace 'your_username', 'your_password', and 'your_database' with your actual Oracle credentials
connection = cx_Oracle.connect('your_username/your_password@your_database')

lock_name = 'EXAMPLE_LOCK'

try:
    # Acquire the lock
    acquire_lock(connection, lock_name)
    print(f"Lock '{lock_name}' acquired successfully.")

    # Your critical section - perform operations that require the lock here

finally:
    # Release the lock in a finally block to ensure it's released even if an exception occurs
    release_lock(connection, lock_name)
    print(f"Lock '{lock_name}' released.")

# Close the database connection
connection.close()
