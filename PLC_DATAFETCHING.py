import sys
from PyQt5.QtWidgets import QApplication, QFileDialog, QMainWindow, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel
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
from tkinter import Tk, filedialog
from cryptography.fernet import Fernet
from PyQt5.QtCore import QTimer
import os
import smtplib
import ssl
from email.message import EmailMessage
from email.mime.base import MIMEBase
from email import encoders


global local_connStatus

executor = concurrent.futures.ThreadPoolExecutor(max_workers=10)



class PLCDataLogger(QtWidgets.QMainWindow):

    def __init__(self): 
        super(PLCDataLogger, self).__init__()
        uic.loadUi('Welcome_plc.ui', self)

        
        idfont = QFontDatabase.addApplicationFont(
             "open-sans/Opensans-Semibold.ttf")
        
        if idfont < 0:
            print("Font Error")
        families = QFontDatabase.applicationFontFamilies(idfont)
        print("Font Family name : ", families[0])
        self.setFont(QFont("Open Sans"))
        self.logcon = self.findChild(QtWidgets.QTextEdit, 'connStatus')
        self.activateLicense.clicked.connect(self.licence)
        self.btnConnectDb.clicked.connect(self.dbConnection)
        


    def openWindow(self):
        if self.local_A == True & self.dateExp == True:
            if gma(0) == self.macCheck:

                self.window = QtWidgets.QMainWindow()
                self.Ui = Ui_MainWindow()
                self.Ui.setupUi(self.window)
                Mainwindow.hide()
                idfont = QFontDatabase.addApplicationFont(
                "open-sans/Opensans-Semibold.ttf")
            
                if idfont < 0:
                    print("Font Error")
                families = QFontDatabase.applicationFontFamilies(idfont)
                print("Font Family name : ", families[0])
                self.setFont(QFont("Open Sans"))
                self.window.show()
                revision = "0.0.5"
                self.versionSet = self.Ui.versionSet
                self.versionSet.setText(revision)
        
                self.logImp = self.Ui.logImp
                self.logField = self.Ui.logField
                self.log = self.Ui.textStatus
                self.Ui.show_data_btn.clicked.connect(lambda: self.thread_and_handle(self.show_data))
                self.Ui.export_btn.clicked.connect(lambda: self.thread_and_handle(self.export_data))
                self.Ui.btnBackup.clicked.connect(self.select_backup_path)
                self.Ui.btnDownloadExcel.clicked.connect(self.modelExcel)
                self.Ui.btnConnect.clicked.connect(lambda: self.thread_and_handle(self.plcConnect))
                self.Ui.btnConnect.clicked.connect(self.timer)
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
                self.logcon.append('Error: Invalid Licence Contact Admin ')
            
        else:
            self.logcon.append('Error: Contact admin')



    def send_email(self):
        # Define email sender and receiver
        email_sender = 'saravan2406@gmail.com'
        #email_password = os.environ.get("EMAIL_PASSWORD")
        email_password = 'utefbkprwxtdanvc'
        email_receiver = 'saravanan@proliteautomation.com, sureshgopi@proliteautomation.com'
        email_receiver2 = 'sureshgopi@proliteautomation.com'

        # Set the subject and body of the email
        subject = 'Urgent : Data Logger Connection Error!!!'
        body = f"""Urgent Notice: Our records indicate that your data logger connection has been disrupted. 
        Please take immediate action to restore the connection to prevent any potential data loss. 
        Your prompt attention to this matter is greatly appreciated. 

        Please note that this email is sent from an automated system, and replies to this message will not be monitored. 
        If you require assistance or have any questions, please contact our support team directly.

        """
        em = EmailMessage()
        em['From'] = email_sender
        em['To'] = email_receiver
        em['Cc'] = email_receiver2
        em['Subject'] = subject
        em.set_content(body)
        # Make the message multipart
        em.add_alternative(body, subtype='html')
        """
        # Attach the image file
        with open('plcimage.jpg', 'rb') as attachment_file:
            file_data = attachment_file.read()
            file_name = attachment_file.name.split("/")[-1]
        attachment = MIMEBase('application', 'octet-stream')
        attachment.set_payload(file_data)
        encoders.encode_base64(attachment)
        attachment.add_header('Content-Disposition', f'attachment; filename="{file_name}"')
        em.attach(attachment)
        """
        # Add SSL (layer of security)
        context = ssl.create_default_context()
        # Log in and send the email
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver, em.as_string())

    def licence(self):
        self.mac_ver = '00c:9a:3c:f4:b0:55'
        self.lic = self.licenseEnter.text()
        print("Licence key", self.lic)
        try:
            # Construct the SQL query string with CAST function to convert Particulars to nvarchar
            query = "UPDATE Info_DB SET Info = ? WHERE CAST(Particulars AS NVARCHAR(MAX)) = ?"
            # Execute the query with parameters
            self.cursor.execute(query, (self.lic, "Activation_Key"))
            self.cursor.commit()
        except Exception as e:
            print(f"Error updating license: {e}")




    def encrypt (self):
        # Fixed encryption key (ensure it's kept secure)
        crypto_key = b'9tvb2SoOaB11TA4YN3CydnGq4IfvSVSZJy25B6bdskM='
        # Initialize Fernet with the encryption key
        fernet = Fernet(crypto_key)
        # Encrypt the MAC address
        enc_mac = fernet.encrypt(self.mac_ver.encode())
        return enc_mac


    def decrypt (self):
        for index, row in self.dfInfo.iterrows():
            if row['Particulars'] == 'Activation_Key':
                self.lic = row['Info']
                print("Licience:", self.lic)

        # Fixed encryption key (ensure it's kept secure)
        crypto_key = b'9tvb2SoOaB11TA4YN3CydnGq4IfvSVSZJy25B6bdskM='

        # Initialize Fernet with the encryption key
        fernet = Fernet(crypto_key)
        # Encrypt the MAC address

        enc_macid = self.lic.encode('utf-8')
        print("Print Enc mac " ,enc_macid)
        # Decrypt the encrypted MAC address (optional)
        dec_mac = fernet.decrypt(enc_macid).decode()
        self.macCheck = dec_mac[1:]
        self.softwaretypeCheck = int(dec_mac[0])
        return dec_mac

    def select_backup_path(self):
        root = Tk()
        root.withdraw()  # Hide the main window

        # # Prompt user to select backup file path
        self.backup_path = filedialog.asksaveasfilename(defaultextension=".bak",
                                                    filetypes=[("Backup files", "*.bak"), ("All files", "*.*")])
        # self.backup_path = "C:\Program Files\Microsoft SQL Server\MSSQL16.MSSQLSERVER\MSSQL\Backup\PLCDB2.bak"
        server_name = 'SURESHGOPI'
        # server_name = 'localhost\sqlexpress'
        database = 'PLCDB2'

        self.backup_database(server_name, database)

    def backup_database(self, server, database):
        try:
            # Get the backup path selected by the user
            self.conn.autocommit = True

            # # Define the SQL backup command
            backup_command = f'BACKUP DATABASE [{database}] TO DISK = \'{self.backup_path}\''

        
            # Execute the backup command
            self.cursor.execute(backup_command)
            print(f"Backup of database '{database}' completed successfully.")
        except Exception as e:
            print(f"Error occurred: {str(e)}")
        finally:
            # Close cursor and connection
            self.cursor.commit()
            self.conn.commit()
           
    def log_to_file(self, message): 
        # timestamp = datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S] ")  
        with open('log.txt', 'a') as file:  
            file.write( message + '\n')         
        self.logField.append(message)               

    def clear_logs(self):
        self.logField.clear()  # Clear the text editor
        with open('log.txt', 'w') as file:
            file.write('')  # Clear the log file
  
    def modelExcel(self):
        self.dfPlc()
        self.logImp.append("The Referencre Excel where given in your Folder create the excel in that format then upload")
        # Define the file path
        file_path = 'ReferenceExcel.xlsx'

        # Create Excel Writer Object
        with pd.ExcelWriter(file_path, engine='xlsxwriter') as writer:
            # Write DataFrame to Excel
            self,self.dfPlcdb.to_excel(writer, sheet_name='Sheet1', index=False)

    def restrict_soft(self):
        query = text('SELECT * FROM Info_DB')
        self.dfInfo = pd.read_sql_query(query, self.con)
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
        query = text('SELECT * FROM Info_DB')
        self.dfInfo = pd.read_sql_query(query, self.con)
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
            self.engine = create_engine('mssql+pyodbc://SURESHGOPI/PLCDB2?driver=SQL+Server')
            self.con = self.engine.connect()

            self.logcon.append('SQL DB is connected')

            
            self.authentication()
            self.restrict_soft()
            self.decrypt()
            self.openWindow()

            monitor_timer = QTimer(self)
            monitor_timer.timeout.connect(self.check_variables)
            monitor_timer.start(3600000)
        except Exception as e:
            print("Error connecting to database:", e)
            self.logcon.append("Error connecting to database:" + str(e))

    def plcConnect(self):
        try:
            self.plcIP = self.Ui.inpIp.text()
             
            print(self.plcIP)
            self.current_date = datetime.now()
            self.plc = snap7.client.Client()
            self.plc.connect(self.plcIP, 0, 1)
            print("PLC Connected", self.plc)
            print("DB Connected", self.cursor)
            print("DB Connected", self.conn)
            self.log.append('PLC is connected')
            message = 'PLC is connected ' + str(self.current_date)
            self.log_to_file(message)
            self.local_connStatus = True
            self.dfPlc()
            self.run_logging()
            if self.plcIP == "":
                self.log.append(f'PLC IP: {e}') 
                print("PLC IP address is not provided.")
                # You might want to inform the user or take appropriate action here
        except Exception as e:
            self.log.append(f'PLC is not connected: {e}') 
            print("Not connecting", e)
            self.local_connStatus = False
            self.send_email()
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
            self.log.append('PLC is Disconnected Error: {e}')
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

    def timer(self):
        monitor_timer = QTimer(self)
        monitor_timer.timeout.connect(self.run_logging)
        monitor_timer.start(5000)

    def run_logging(self):
        try: 
            if self.local_connStatus == True:
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
                
        except Exception as e:
            self.local_connStatus = False
            self.logField.append(f"Error : {e}")
            self.send_email() 
      
    def plcDataSnap7(self, db_number, data_type, start_offset, bit_offset):
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
                return None
            
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]

            return value, timestamp  
        except Exception as e:
            self.logField.append(f"Error : {e}")   

    # def plcDataSnap7(self, db_number, data_type, start_offset, bit_offset):
    #     if data_type == 'BOOL':
    #         reading = self.plc.db_read(db_number, start_offset, 1)
    #         value = snap7.util.get_bool(reading, 0, bit_offset)
    #     elif data_type == 'REAL':
    #         reading = self.plc.db_read(db_number, start_offset, 4)
    #         value = struct.unpack('>f', reading)[0]
    #     elif data_type == 'INT':
    #         reading = self.plc.db_read(db_number, start_offset, 2)
    #         value = struct.unpack('>h', reading)[0]
    #     elif data_type == 'DINT':  # Add support for double integer (4 bytes)
    #         reading = self.plc.db_read(db_number, start_offset, 4)
    #         value = struct.unpack('>i', reading)[0]
    #     else:
    #         print("Unsupported data type:", data_type)
    #         return None
    #     return value
    
    def show_data(self):
        from_time = self.Ui.from_time.dateTime().toString(Qt.ISODate)
        to_time = self.Ui.to_time.dateTime().toString(Qt.ISODate)

        try:
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
        except Exception as e:
            self.logImp.append(f"Error: {e}")

    def export_data(self):
        try:
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
        except Exception as e:
                self.logImp.append(f"Error: {e}")

    def check_variables(self):
        self.restrict_soft()
        # Check if self.local_A or self.dateExp is False
        if self.local_A == False or self.dateExp == False:
            # Perform actions when either variable becomes False
            self.close_application()

    def close_application(self):
        # Close the application
        self.Ui.close()


if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    Mainwindow = PLCDataLogger()
    Mainwindow.show()
    sys.exit(app.exec_())

