import sys
from PyQt5.QtWidgets import QApplication, QFileDialog, QMainWindow
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt
import pyodbc
import pandas as pd
import snap7
import struct
from datetime import datetime
import time
from PyQt5 import QtWidgets
from timeloop import Timeloop
tl = Timeloop()

class PLCDataLogger(QMainWindow):
    def __init__(self):
        super(PLCDataLogger, self).__init__()
        loadUi('plc_data.ui', self)  # Load the UI file

        self.show_data_btn.clicked.connect(self.show_data)
        self.export_btn.clicked.connect(self.export_data)  # Connect export button to export_data method
        self.btnConnect.clicked.connect(self.plc_connect)
        self.btnDisconnect.clicked.connect(self.plc_disconnect)
        self.log = self.findChild(QtWidgets.QTextEdit, 'textStatus')
        self.navHome.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.homePage))
        self.navExport.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.exportPage))
        self.navLog.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.logPage))
        self.navHelp.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.helpPage))


    def plc_connect(self):
        #Reading excel file as pd
        self.offsets_df = pd.read_excel("C:\prolite\Plc_data\PLC_DB_Access.xlsx")
        try:
            # Connect to PLC
            self.plc = snap7.client.Client()
            self.plc.connect('192.168.0.1', 0, 1)  # IP address, rack, slot (from HW settings)

            # Connect to SQL Server database
            self.conn = pyodbc.connect(
                'DRIVER=SQL Server;'
                'SERVER=SURESHGOPI;'
                'DATABASE=PLCDB2;'
            )
            self.cursor = self.conn.cursor()
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            self.log.append('PLC is connected', timestamp)
            self.run_logging()
           
        except:
            self.log.append('PLC is not connected ip error')
    
        tl.start(block=True) 
        
    def plc_disconnect(self):
         # Disconnect from PLC
        tl.stop(block=False)
        # self.plc.disconnect()
        self.log.append('PLC is Disconnected')
        # Close SQL Server connection
        # self.cursor.close()
        

    def show_data(self):
        from_time = self.from_time.dateTime().toString(Qt.ISODate)
        to_time = self.to_time.dateTime().toString(Qt.ISODate)

        # Query database for data between specified timestamps
        query = "SELECT * FROM plc_data WHERE TimeStamp BETWEEN ? AND ?"
        self.cursor.execute(query, (from_time, to_time))
        data = self.cursor.fetchall()

        # Populate data into a QStandardItemModel
        model = QStandardItemModel(len(data), len(data[0]), self)
        model.setHorizontalHeaderLabels(['ID', 'TimeStamp', 'Name', 'DataType', 'Value'])
        for row_num, row_data in enumerate(data):
            for col_num, value in enumerate(row_data):
                item = QStandardItem(str(value))
                model.setItem(row_num, col_num, item)

        # Set the model for the QTableView
        self.table_view.setModel(model)

    def export_data(self):
        # Get the data from the QStandardItemModel
        model = self.table_view.model()
        if not model:
            return  # No data to export

        # Convert data to DataFrame
        data = []
        for row in range(model.rowCount()):
            row_data = []
            for column in range(model.columnCount()):
                index = model.index(row, column)
                row_data.append(model.data(index))
            data.append(row_data)

        # Create DataFrame
        df = pd.DataFrame(data, columns=['ID', 'TimeStamp', 'Name', 'DataType', 'Value'])

        # Export DataFrame to Excel file
        file_name, _ = QFileDialog.getSaveFileName(self, "Save File", "", "Excel files (*.xlsx)")
        if file_name:
            df.to_excel(file_name, index=False)
    
    def read_and_insert(self, db_number, start_offset, data_type, bit_offset, name):
        if data_type == 'BOOL':
            reading = self.plc.db_read(db_number, start_offset, 1)
            value = snap7.util.get_bool(reading, 0, bit_offset)
        elif data_type == 'REAL':
            reading = self.plc.db_read(db_number, start_offset, 4)
            value = struct.unpack('>f', reading)[0]
        elif data_type == 'INT':
            reading = self.plc.db_read(db_number, start_offset, 2)
            value = struct.unpack('>h', reading)[0]
        else:
            print("Unsupported data type:", data_type)
            return
        # Assuming you want to store the formatted string in a variable called 'log_message'
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_message = 'DB Number: {}, Start Offset: {}, Data Type: {}, Value: {}, Name: {}'.format(db_number, start_offset, data_type, value, name)

        print(log_message)  # Optionally, you can print the message if needed
        # self.log.append('PLC Data \n ', timestamp , "\n")

      
        # print('Timestamp:', timestamp)
        # print('DB Number: {}, Start Offset: {}, Data Type: {}, Value: {}, Name: {}'.format(db_number, start_offset,
        #                                                                                     data_type, value, name))

        # Insert data into database
        self.cursor.execute('''INSERT INTO plc_data (TimeStamp, Name, DataType, Value)
                            VALUES (?, ?, ?, ?)''', (timestamp, name, data_type, value))
        self.conn.commit()

    def run_logging(self):
        try:
            self.log.append('PLC is connected')
            # Loop to log data every 5 seconds until interrupted
            while True:
                for index, row in self.offsets_df.iterrows():
                    db_number = row['db_number']
                    start_offset = row['start_offset']
                    data_type = row['data_type']
                    name = row['Name']
                    bit_offset = row['bit_offset']
                    print(db_number, start_offset, data_type, name)
                    self.read_and_insert(db_number, start_offset, data_type, bit_offset, name)
                time.sleep(5)  # Sleep for 5 seconds

        except KeyboardInterrupt:
            print("Program terminated by user.")

        finally:
            # Close connections
            self.cursor.close()
            self.conn.close()
            self.plc.disconnect()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PLCDataLogger()
    window.show()
    # window.run_logging()
    sys.exit(app.exec_())
