import sys
from PyQt5.QtWidgets import QApplication, QFileDialog, QMainWindow
from PyQt5.QtGui import *
from PyQt5.uic import loadUi
from PyQt5.QtCore import *
import pyodbc
import pandas as pd
import snap7
import struct
import datetime
from datetime import datetime
import time
from PyQt5 import QtWidgets, QtGui, uic
import concurrent.futures
from plc_data_ui import Ui_MainWindow
from getmac import get_mac_address as gma
print(gma())
from sqlalchemy import create_engine, text
from PyQt5.QtCore import QTimer
# from Welcome_plc_ui import Ui_WelcomeWindow
global local_connStatus
global A

executor = concurrent.futures.ThreadPoolExecutor(max_workers=10)
global plc


class PLCDataLogger(QtWidgets.QMainWindow):

    def __init__(self): 
        super(PLCDataLogger, self).__init__()
        uic.loadUi('Welcome_plc.ui', self)
        self.logcon = self.findChild(QtWidgets.QTextEdit, 'connStatus')
        self.btnConnectDb.clicked.connect(self.dbConnection)
        # self.logging_loop_active = False
    
    def openWindow(self):
        if self.local_A == True & self.dateExp == True:
            self.window = QtWidgets.QMainWindow()
            self.Ui = Ui_MainWindow()
            self.Ui.setupUi(self.window)
            Mainwindow.hide()
            self.window.show()

            # self.logging_loop_active = False
            # self.window.closeEvent = self.local_connStatus = False      
    
            
            self.logImp = self.Ui.logImp
            self.logField = self.Ui.logField
            self.log = self.Ui.textStatus
            self.Ui.show_data_btn.clicked.connect(self.show_data)
            self.Ui.export_btn.clicked.connect(self.export_data)
            self.Ui.btnConnect.clicked.connect(lambda: self.thread_and_handle(self.plcConnect))
            self.Ui.btnDisconnect.clicked.connect(lambda: self.thread_and_handle(self.plcDisconnect))
            self.Ui.btnClearLog.clicked.connect(self.clear_logs)
            self.Ui.navHome.clicked.connect(lambda: self.Ui.stackedWidget.setCurrentWidget(self.Ui.homePage))
            self.Ui.navExport.clicked.connect(lambda: self.Ui.stackedWidget.setCurrentWidget(self.Ui.exportPage))
            self.Ui.navLog.clicked.connect(lambda: self.Ui.stackedWidget.setCurrentWidget(self.Ui.logPage))
            self.Ui.navHelp.clicked.connect(lambda: self.Ui.stackedWidget.setCurrentWidget(self.Ui.helpPage))
            self.Ui.navImp.clicked.connect(lambda: self.Ui.stackedWidget.setCurrentWidget(self.Ui.importPage))
            self.Ui.navAbout.clicked.connect(lambda: self.Ui.stackedWidget.setCurrentWidget(self.Ui.aboutPage))
            self.Ui.btnImpExcel.clicked.connect(self.open_excel_file)
        else:
            self.logcon.append('Error: Contact admin')
            
    def stop_logging(self):
        # Method to stop the logging loop
        self.local_connStatus = False

    def log_to_file(self, message):
        # timestamp = datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S] ")
        with open('log.txt', 'a') as file:
            file.write( message + '\n')
        self.logField.append(message)

    def clear_logs(self):
        self.logField.clear()  # Clear the text editor
        with open('log.txt', 'w') as file:
            file.write('')  # Clear the log file

    def closeEvent(self, event):
        # Called when the Ui_MainWindow is closed
        self.stop_logging
        print("Ui_MainWindow closed")  # Stop the loop
        event.accept() 

        # Call the default closeEvent method

    def restrict_soft(self):
        for index, row in self.dfInfo.iterrows():
            if row['Particulars'] == 'Software_type':
                software_type = row['Info']
                print("Software Type:", software_type)
                
            elif row['Particulars'] == 'Software_sold_date':
                Software_sold_date = row['Info']
                print("Release Date String:", Software_sold_date)
                
                try:
                    # Assuming the date format is 'DD/MM/YYYY'
                    Software_date = datetime.strptime(Software_sold_date, '%d/%m/%Y')
                    print("Release Date:", Software_date)
                    
                    self.current_date = datetime.now()
                    print(self.current_date)

                    if software_type == '0':
                        # Check if the software is within the allowed time period (1 month)
                        if (self.current_date - Software_date).days > 30:
                            self.dateExp = False
                            print("Date Expired:", self.dateExp) 
                        else:
                            self.dateExp = True
                            self.logcon.append("License Expired" )
                            print("Date Expired:", self.dateExp)
                        
                except ValueError as e:
                    print("Error parsing release date:", e)
                    
    
        return self.dateExp
 
    def authentication(self):
        for index, row in self.dfInfo.iterrows():
            if row['Particulars'] == 'Local_System_Macid':
                if row['Info'] == gma():
                    print(self.dfInfo)
                    self.local_A = True
                    return self.local_A
                else:
                    print(self.dfInfo)
                    self.local_A = False
                    self.logcon.append("License Invalid" )
                    return self.local_A             
                        
    def thread_and_handle(self, func):
        future = executor.submit(func)
        future.add_done_callback(self.handle_result)

    def handle_result(self, future):
        connStatus = future.result()  # Get the result from the future
        print(connStatus)
            # Now you can use the result as needed
                                                                           
    def dbConnection(self):
        try:
            self.conn = pyodbc.connect(
            'DRIVER=SQL Server;'
            'SERVER=SURESHGOPI;'
            'DATABASE=PLCDB2;'
            )
            self.cursor = self.conn.cursor()
            # Create SQLAlchemy engine
            self.engine = create_engine('mssql+pyodbc://SURESHGOPI/PLCDB2?driver=SQL+Server')
            # Execute SQL query and read data into DataFrame
            self.con = self.engine.connect()
            query = text('SELECT * FROM Info_DB')
            self.dfInfo = pd.read_sql_query(query, self.con)         

            self.logcon.append('SQL DB is connected')
            self.authentication()
            self.restrict_soft()
            self.openWindow()
            
        except Exception as e:
            print("Error connecting to database:", e)
            self.logcon.append("Error connecting to database:" + str(e))

    def plcConnect(self):
        try:
            self.current_date = datetime.now()
            self.plc = snap7.client.Client()
            self.plc.connect('192.168.0.1', 0, 1)
            print("PLC Connected", self.plc)
            print("DB Connected", self.cursor)
            print("DB Connected", self.conn)
            self.log.append('PLC is connected')
            message = 'PLC is connected ' + str(self.current_date)
            self.log_to_file(message)
            self.local_connStatus = True
            self.dfPlc()
            self.run_logging()
        except Exception as e:
            self.log.append(f'PLC is not connected: {e}') 
            print("Not connecting", e)
            self.local_connStatus = False
            # Retry connecting after a delay
            # QTimer.singleShot(240000000, self.plcConnect())  # Retry after 5 seconds
        return self.local_connStatus

    def plcDisconnect(self):
        try:
            self.current_date = datetime.now()
            self.plc.disconnect()
            self.log.append('PLC is Disconnected')
            self.local_connStatus = False
            message = 'PLC data fetching Disconnected' + str(self.current_date)
            self.log_to_file(message)
        except Exception as e:
            print("Error while disconnecting:", e)
            self.local_connStatus = False
            
        return self.local_connStatus

    def open_excel_file(self):
        # Open file dialog to select Excel file
        file_name, _ = QFileDialog.getOpenFileName(self, "Open Excel File", "", "Excel files (*.xlsx *.xls)")
        if file_name:
            # Read data from Excel into DataFrame
            try:
                self.dfPlcExcel = pd.read_excel(file_name)
                # self.thread_and_handle(self.insert_data_into_mysql())
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
            columns = ', '.join([f"{col} VARCHAR(255)" for col in self.dfPlcExcel.columns])
            create_table_query = f"""
                IF NOT EXISTS (SELECT * FROM sys.tables WHERE name='Data')
                BEGIN
                    CREATE TABLE Data ({columns})
                END
            """
            self.cursor.execute(create_table_query)

            # Insert data into the table
            for index, row in self.dfPlcExcel.iterrows():
                # Dynamically generate INSERT INTO query based on DataFrame columns
                placeholders = ', '.join(['?' for _ in self.dfPlcExcel.columns])  # Using ? as parameter placeholder
                columns = ', '.join(self.dfPlcExcel.columns)
                sql = f"INSERT INTO Data ({columns}) VALUES ({placeholders})"
                # Pass values as a tuple directly to execute
                self.cursor.execute(sql, tuple(row))
            # Commit changes            
            self.conn.commit()

            self.logImp.append("Data inserted into MySQL table successfully.")
            self.dfPlc()
        except Exception as e:
            self.logImp.append(f"Error inserting data into MySQL table: {e}")
        
    def dfPlc(self):        
        for index, row in self.dfInfo.iterrows():
            if row['Particulars'] == 'Software_type':
                software_type = row['Info']
                software_type = int(software_type)
                print("Software Type:", software_type)
                try:
                    print("Software Type:", software_type)
                    if software_type == 0 or software_type == 1:
                        print("Software Type:", software_type)
                        # Retrieve data from MySQL table after insertion
                        select_query = text("SELECT  * FROM Data")
                        # Load data into a DataFrame
                        self.dfdemo = pd.read_sql_query(select_query, self.con)

                        self.dfPlcdb = self.dfdemo.head(50)
                        self.dfPlcdb['db_number'] = pd.to_numeric(self.dfPlcdb['db_number'], errors='ignore', downcast='integer')
                        self.dfPlcdb['start_offset'] = pd.to_numeric(self.dfPlcdb['start_offset'], errors='ignore', downcast='integer')
                        self.dfPlcdb['bit_offset'] = pd.to_numeric(self.dfPlcdb['bit_offset'], errors='ignore', downcast='integer')
                        print(self.dfPlcdb)
                        return self.dfPlcdb
                    else:
                        select_query = "SELECT  * FROM Data"
                        self.dfPlcdb = pd.read_sql(select_query, self.engine)
                        self.dfPlcdb['db_number'] = pd.to_numeric(self.dfPlcdb['db_number'], errors='ignore', downcast='integer')
                        self.dfPlcdb['start_offset'] = pd.to_numeric(self.dfPlcdb['start_offset'], errors='ignore', downcast='integer')
                        self.dfPlcdb['bit_offset'] = pd.to_numeric(self.dfPlcdb['bit_offset'], errors='ignore', downcast='integer')
                        print(self.dfPlcdb)
                        return self.dfPlcdb
                    
                except Exception as e:
                    self.logImp.append(f"Error inserting data into MySQL table: {e}")
                # print(self.dfPlcdb)

    def run_logging(self):
        try: 
            while self.local_connStatus == True:
                self.current_date = datetime.now()
                message = 'Data fetching from PLC ' + str(self.current_date)
                self.log_to_file(message)
                print("1")
                # Apply the plcDataSnap7 function to each row of the DataFrame
                self.dfPlcdb[['Value', 'timestamp']] = self.dfPlcdb.apply(lambda row: pd.Series(self.plcDataSnap7(row['db_number'], row['data_type'], row['start_offset'], row['bit_offset'])), axis=1)
                # Assuming 'cursor' is your database cursor object
                # Create a list of tuples containing the values to be inserted
                values = [(row['timestamp'], row['Name'], row['data_type'], row['Value']) for _, row in self.dfPlcdb.iterrows()]

                # Execute the query to insert multiple rows
                self.cursor.executemany('''INSERT INTO plc_data (TimeStamp, Name, DataType, Value)
                                    VALUES (?, ?, ?, ?)''', values)      
                self.conn.commit() 
                time.sleep(5) 
    
        
        except KeyboardInterrupt:
            print("Program terminated by user.") 

    def plcDataSnap7(self, db_number, data_type, start_offset, bit_offset):
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
            return None
        
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
        return value, timestamp     
    
    def show_data(self):
        from_time = self.Ui.from_time.dateTime().toString(Qt.ISODate)
        to_time = self.Ui.to_time.dateTime().toString(Qt.ISODate)

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
        self.Ui.table_view.setModel(model)

    def export_data(self):
        # Get the data from the QStandardItemModel
        model = self.Ui.table_view.model()
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
    app = QtWidgets.QApplication(sys.argv)
    Mainwindow = PLCDataLogger()
    Mainwindow.show()
    sys.exit(app.exec_())

