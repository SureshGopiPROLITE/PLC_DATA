import sys
from PyQt5.QtWidgets import QApplication, QFileDialog, QMainWindow
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt, QThread, pyqtSignal
import pyodbc
import pandas as pd
import snap7
import struct
from datetime import datetime
import time
from PyQt5 import QtWidgets
import concurrent.futures

global connStatus

executor = concurrent.futures.ThreadPoolExecutor(max_workers=10)

class PLCDataLogger(QMainWindow):
    def __init__(self):
        super(PLCDataLogger, self).__init__()
        loadUi('plc_data.ui', self)

        self.show_data_btn.clicked.connect(self.show_data)
        self.export_btn.clicked.connect(self.export_data)
        self.btnConnect.clicked.connect(lambda: self.thread_and_handle(self.plcConnect))
        self.btnDisconnect.clicked.connect(lambda: self.thread_and_handle(self.plcDisconnect))
        self.navHome.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.homePage))
        self.navExport.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.exportPage))
        self.navLog.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.logPage))
        self.navHelp.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.helpPage))
        self.navImp.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.importPage))
        self.btnImpExcel.clicked.connect(self.open_excel_file)
        self.btnImpExcel.clicked.connect(lambda: self.thread_and_handle(self.dbConnection))
        
        self.log = self.findChild(QtWidgets.QTextEdit, 'textStatus')
        self.logField = self.findChild(QtWidgets.QTextEdit, 'logField')
        self.logImp = self.findChild(QtWidgets.QTextEdit, 'logImp')
        
        # Establish database connection
        
        
    def thread_and_handle(self, func):
        future = executor.submit(func)
        future.add_done_callback(self.handle_result)

    def handle_result(self, future):
        connStatus = future.result()  # Get the result from the future
        print("Connection Status:", connStatus)
        # Now you can use the result as needed

    def dbConnection(self):
        self.conn = pyodbc.connect(
            'DRIVER=SQL Server;'
            'SERVER=SURESHGOPI;'
            'DATABASE=PLCDB2;'
        )
        self.cursor = self.conn.cursor()

    def plcConnect(self):
        # self.self.dfPlcdb = pd.read_excel("C:\prolite\Plc_data\PLC_DB_Access.xlsx")
        # print(self.self.dfPlcdb)
        try:
            self.plc = snap7.client.Client()
            self.plc.connect('192.168.0.1', 0, 1)
            print("PLC Connected", self.plc)
            print("DB Connected", self.cursor)
            print("DB Connected", self.conn)
            self.log.append('PLC is connected')
            local_connStatus = True
            self.run_logging(local_connStatus)
        except Exception as e:
            print("Not connecting", e)
            local_connStatus = False
        return local_connStatus

    def plcDisconnect(self):
        try:
            self.plc.disconnect()
            self.log.append('PLC is Disconnected')
            local_connStatus = False
        except Exception as e:
            print("Error while disconnecting:", e)
            local_connStatus = False
        return local_connStatus

    def open_excel_file(self):
        # Open file dialog to select Excel file
        file_name, _ = QFileDialog.getOpenFileName(self, "Open Excel File", "", "Excel files (*.xlsx *.xls)")
        if file_name:
            # Read data from Excel into DataFrame
            try:
                self.dfPlcdb = pd.read_excel(file_name)
                self.insert_data_into_mysql()
                self.logImp.append("Data inserted into MySQL table successfully.")
            except Exception as e:
                self.logImp.append(f"Error reading Excel file: {e}")

    def insert_data_into_mysql(self):
        try:
            # Truncate the table to clear all existing data
            truncate_query = "TRUNCATE TABLE Data"
            self.cursor.execute(truncate_query)

            # Dynamically generate CREATE TABLE query based on DataFrame columns
            columns = ', '.join([f"{col} VARCHAR(255)" for col in self.dfPlcdb.columns])
            create_table_query = f"""
                IF NOT EXISTS (SELECT * FROM sys.tables WHERE name='Data')
                BEGIN
                    CREATE TABLE Data ({columns})
                END
            """
            self.cursor.execute(create_table_query)

            # Insert data into the table
            for index, row in self.dfPlcdb.iterrows():
                # Dynamically generate INSERT INTO query based on DataFrame columns
                placeholders = ', '.join(['?' for _ in self.dfPlcdb.columns])  # Using ? as parameter placeholder
                columns = ', '.join(self.dfPlcdb.columns)
                sql = f"INSERT INTO Data ({columns}) VALUES ({placeholders})"
                # Pass values as a tuple directly to execute
                self.cursor.execute(sql, tuple(row))

            # Commit changes
            self.conn.commit()

            self.logImp.append("Data inserted into MySQL table successfully.")
        except Exception as e:
            self.logImp.append(f"Error inserting data into MySQL table: {e}")



    def run_logging(self, local_connStatus):
        while local_connStatus:
            try:
                self.logField.append('PLC data fetching')
                # Loop to log data every 5 seconds until interrupted
                for index, row in self.dfPlcdb.iterrows():
                    db_number = row['db_number']
                    start_offset = row['start_offset']
                    data_type = row['data_type']
                    name = row['Name']
                    bit_offset = row['bit_offset']
                    print(db_number, start_offset, data_type, bit_offser, name)
                    self.read_and_insert(self, db_number, start_offset, data_type, bit_offset, name)
                time.sleep(5)  # Sleep for 5 second
            except KeyboardInterrupt:
                print("Program terminated by user.")
                                                                                    
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

        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_message = 'DB Number: {}, Start Offset: {}, Data Type: {}, Value: {}, Name: {}'.format(db_number, start_offset, data_type, value, name)
        print(log_message)

        self.cursor.execute('''INSERT INTO plc_data (TimeStamp, Name, DataType, Value)
                            VALUES (?, ?, ?, ?)''', (timestamp, name, data_type, value))
        self.conn.commit()
    
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
        
     
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PLCDataLogger()
    window.show()
    sys.exit(app.exec_())
