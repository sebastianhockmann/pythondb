import sqlite3
import time

conn = sqlite3.connect('mydatabase.db') # create a connection object
conn.close()

print("SQLite version:", sqlite3.sqlite_version)

create_table_sql_query = '''
CREATE TABLE IF NOT EXISTS data_logger(
Id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
Temp_Sensor1 REAL,
Temp_Sensor2 REAL,
Temp_Sensor3 REAL,
IP_Address TEXT,
TimeStamp INTEGER

) STRICT;
'''


connection_object = sqlite3.connect('datalogger.sqlite')
cursor_object = connection_object.cursor()
cursor_object.execute(create_table_sql_query)
connection_object.commit()
connection_object.close()

# Sample data
temp1 = 25.3
temp2 = 34.6
temp3 = 24.8
ip_address = '192.168.0.101'
timestamp = int(time.time())  # current Unix time
insert_data_sql_query = '''
          INSERT INTO data_logger (Temp_Sensor1,
                                   Temp_Sensor2,
                                   Temp_Sensor3,
                                   IP_Address,
                                   TimeStamp)
          VALUES (?, ?, ?, ?, ?)
   '''
# Connect and insert data
with sqlite3.connect('datalogger.sqlite') as connection_object:
   cursor_object  = connection_object.cursor()
   cursor_object.execute(insert_data_sql_query, (temp1, temp2, temp3, ip_address, timestamp))


cursor_object.execute("SELECT * FROM data_logger")

# Fetch all rows from the executed query
rows = cursor_object.fetchall()

# Print the results
for row in rows:
    print(row)