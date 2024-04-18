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
from sqlalchemy import create_engine
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
        # self.btnConnectDb.clicked.connect(self.openWindow)
    
    def openWindow(self):
        if self.local_A == True & self.dateExp == True:
            self.window = QtWidgets.QMainWindow()
            self.Ui = Ui_MainWindow()
            self.Ui.setupUi(self.window)
            Mainwindow.hide()
            self.window.show()
            
            self.logImp = self.Ui.logImp
            self.logField = self.Ui.logField
            self.log = self.Ui.textStatus
            self.Ui.show_data_btn.clicked.connect(self.show_data)
            self.Ui.export_btn.clicked.connect(self.export_data)
            # self.Ui.btnConnect.clicked.connect(lambda: self.thread_and_handle(self.plcConnect))
            self.Ui.btnConnect.clicked.connect(lambda: self.thread_and_handle(self.plcConnect))
            self.Ui.btnDisconnect.clicked.connect(lambda: self.thread_and_handle(self.plcDisconnect))
            # self.Ui.btnConnect.clicked.connect(self.dfPlc())
            self.Ui.sampleBtn.clicked.connect(self.run_logging)
            self.Ui.navHome.clicked.connect(lambda: self.Ui.stackedWidget.setCurrentWidget(self.Ui.homePage))
            self.Ui.navExport.clicked.connect(lambda: self.Ui.stackedWidget.setCurrentWidget(self.Ui.exportPage))
            self.Ui.navLog.clicked.connect(lambda: self.Ui.stackedWidget.setCurrentWidget(self.Ui.logPage))
            self.Ui.navHelp.clicked.connect(lambda: self.Ui.stackedWidget.setCurrentWidget(self.Ui.helpPage))
            self.Ui.navImp.clicked.connect(lambda: self.Ui.stackedWidget.setCurrentWidget(self.Ui.importPage))
            self.Ui.btnImpExcel.clicked.connect(self.open_excel_file)
        else:
            self.logcon.append('Error: Contact admin')
            
    def restrict_soft(self):
        for index, row in self.dfInfo.iterrows():
            if row['Particulars'] == 'Software_type':
                software_type = row['Info']
                print("Software Type:", software_type)
                
            elif row['Particulars'] == 'Release_date':
                release_date_str = row['Info']
                print("Release Date String:", release_date_str)
                
                try:
                    # Assuming the date format is 'DD/MM/YYYY'
                    release_date = datetime.strptime(release_date_str, '%d/%m/%Y')
                    print("Release Date:", release_date)
                    
                    current_date = datetime.now()
                    print(current_date)

                    if software_type == '0':
                        # Check if the software is within the allowed time period (1 month)
                        if (current_date - release_date).days > 30:
                            self.dateExp = False
                            print("Date Expired:", self.dateExp) 
                        else:
                            self.dateExp = True
                            print("Date Expired:", self.dateExp)
                        
                except ValueError as e:
                    print("Error parsing release date:", e)
                    
        
                
                if software_type == '1':
                    # Check if the software has read access restricted to 50 data from PLC
                    # Assuming '50 data from PLC' is one of the restrictions

                    # Implement other restrictions similarly
                    pass
            # Check for other restrictions and return True if all conditions are met
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
                    return self.local_A             
                     
        # return 2
   
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
            sql = "SELECT * FROM Info_DB"
            self.dfInfo = pd.read_sql(sql, self.engine)

            # self.logImp.append('PLC is connected')
            # self.thread_and_handle(self.authentication)
            self.logcon.append('PLC is connected')
            self.authentication()
            self.restrict_soft()
            self.openWindow()
            
        except Exception as e:
            print("Error connecting to database:", e)

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
            self.local_connStatus = True
            self.dfPlc()
            self.run_logging()
        except Exception as e:
            self.log.append(f'PLC is not connected: {e}') 
            print("Not connecting", e)
            self.local_connStatus = False
        return self.local_connStatus

    def plcDisconnect(self):
        try:
            self.plc.disconnect()
            self.log.append('PLC is Disconnected')
            self.local_connStatus = False
            self.run_logging()
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
                        select_query = "SELECT  * FROM Data"
                        # self.cursor.execute(select_query)
                        # data_from_sql = self.cursor.fetchall()
                        self.dfdemo = pd.read_sql(select_query, self.engine)
                        self.dfPlcdb = self.dfdemo.head(50)
                        # Load data into a DataFrame
                        # columns = [col[0] for col in data_from_sql]
                        # self.dfPlcdb = pd.DataFrame(data_from_sql, columns=columns)
                        print(self.dfPlcdb)
                        return self.dfPlcdb
                    else:
                        select_query = "SELECT  * FROM Data"
                        self.dfPlcdb = pd.read_sql(select_query, self.engine)
                        print(self.dfPlcdb)
                        return self.dfPlcdb
                    
                except Exception as e:
                    self.logImp.append(f"Error inserting data into MySQL table: {e}")
                # print(self.dfPlcdb)
                  
    def run_logging(self):
        try: 
            self.logField.append('PLC data fetching')
            while self.local_connStatus == True:
                # if local_connStatus == True:
                # Loop to log data every 5 seconds until interrupted
                for index, row in self.dfPlcdb.iterrows():
                    db_number = row['db_number']
                    db_number = int(db_number)
                    start_offset = row['start_offset']
                    start_offset = int(start_offset)
                    data_type = row['data_type']
                    name = row['Name']
                    bit_offset = row['bit_offset']
                    bit_offset = int(bit_offset)
                    print(db_number, start_offset, bit_offset, data_type, name)
                    self.read_and_insert(db_number, start_offset, data_type, bit_offset, name)
                time.sleep(5)  # Sleep for 5 second
        except KeyboardInterrupt:
            print("Program terminated by user.")


                                                                                    
    def read_and_insert(self, db_number, start_offset, data_type, bit_offset, name):
        try:
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
        except Exception as e:
                self.logField.append(f"Error: {e}")
                print((f"Error: {e}"))
    
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


