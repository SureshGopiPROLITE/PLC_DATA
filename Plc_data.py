import snap7
import struct
import pyodbc
from datetime import datetime
import time
import pandas as pd

# Connect to the PLC
plc = snap7.client.Client()
plc.connect('192.168.0.1', 0, 1)  # IP address, rack, slot (from HW settings)

# Connect to SQL Server database
conn = pyodbc.connect(
    'DRIVER=SQL Server;'
    'SERVER=SURESHGOPI;'
    'DATABASE=PLCDB2;'
)

cursor = conn.cursor()

# Check if the table exists
if not cursor.tables(table='plc_data', tableType='TABLE').fetchone():
    # Table does not exist, create it
    cursor.execute('''CREATE TABLE plc_data (
                        Id INTEGER PRIMARY KEY IDENTITY(1,1),
                        TimeStamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                        Name NVARCHAR(255),
                        DataType NVARCHAR(50),
                        Value FLOAT
                    )''')
    conn.commit()
    print("Table 'plc_data' created successfully.")
else:
    print("Table 'plc_data' already exists.")


# Read offsets and data types from Excel into pandas DataFrame
offsets_df = pd.read_excel("C:\prolite\Plc_data\PLC_DB_Access.xlsx")

# Fetch all rows from the cursor
Info_DB = cursor.execute(''' SELECT * FROM Info_DB ''')
conn.commit()
rows = Info_DB.fetchall()

# Get column names from cursor description
columns = [x[0] for x in cursor.description]

# Create DataFrame from fetched rows and column names
df = pd.DataFrame(rows, columns=columns)
print(df)

# Function to read data and insert into database
def readAndInsert(db_number, start_offset, data_type, bit_offset, name):
    if data_type == 'BOOL':
        reading = plc.db_read(db_number, start_offset, 1)
        value = snap7.util.get_bool(reading, 0, bit_offset)
    elif data_type == 'REAL':
        reading = plc.db_read(db_number, start_offset, 4)
        value = struct.unpack('>f', reading)[0]
    elif data_type == 'INT':
        reading = plc.db_read(db_number, start_offset, 2)
        value = struct.unpack('>h', reading)[0]
    else:
        print("Unsupported data type:", data_type)
        return
    
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print('Timestamp:', timestamp)
    print('DB Number: {}, Start Offset: {}, Data Type: {}, Value: {}, Name: {}'.format(db_number, start_offset, data_type, value, name))
    
    # Insert data into database
    cursor.execute('''INSERT INTO plc_data (TimeStamp, Name, DataType, Value)
                    VALUES (?, ?, ?, ?)''', (timestamp, name, data_type, value))
    conn.commit()


try:
    # Loop to log data every 5 seconds until interrupted
    while True:
        for index, row in offsets_df.iterrows():
            db_number = row['db_number']
            start_offset = row['start_offset']
            data_type = row['data_type']
            name = row['Name']
            bit_offset = row['bit_offset']
            print(db_number, start_offset, data_type, name)
            readAndInsert(db_number, start_offset, data_type, bit_offset, name)
        time.sleep(5)  # Sleep for 5 seconds
        
except KeyboardInterrupt:
    print("Program terminated by user.")
    
finally:
    # Close connections
    cursor.close()
    conn.close()
    plc.disconnect()
