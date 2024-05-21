import sys
from PyQt5.QtWidgets import QApplication, QFileDialog, QMainWindow, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QDialog, QHeaderView,QHBoxLayout,  QSpacerItem, QSizePolicy
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
from PyQt5 import QtCore, QtWidgets, QtWebEngineWidgets
import plotly.express as px

global local_connStatus

executor = concurrent.futures.ThreadPoolExecutor(max_workers=10)



class PLCDataLogger(QtWidgets.QMainWindow, QDialog):

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

    def popUp(self, msg):
        parent_center = self.geometry().center() 
        PopUp = QDialog(self)
        PopUp.setWindowTitle("License Authentication")
        # PopUp.setGeometry(300, 300, 400, 200)  # Set the geometry (x, y, width, height)
        PopUp.setGeometry(parent_center.x() - 200, parent_center.y() - 100, 400, 200)  # Set the geometry (x, y, width, height)

        layout = QVBoxLayout()

        label = QLabel(msg, PopUp)
        label.setStyleSheet("color: #171725;background-color: #ECF1F7;"
                                "font-size: 16px; font-family: Open Sans;")  # Set the font color of the label to white
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)

        save_button = QPushButton("Close", PopUp)
        save_button.setStyleSheet("color: #171725;background-color: #ECF1F7;"
                                "font-size: 16px; font-family: Open Sans;")
        layout.addWidget(save_button)

        # Connecting the button's clicked signal to close the pop-up
        save_button.clicked.connect(PopUp.accept)

        PopUp.setLayout(layout)

        # Executing the dialog as a modal (blocks the parent window until closed)
        PopUp.exec_()

    def graph(self):
        self.Ui.progressBar.show()
        layout = QDialog(self)
        vlayout = QVBoxLayout()
        layout.setWindowTitle("Plot Graph")
        self.button = QtWidgets.QPushButton('Plot', self)
        self.browser = QtWebEngineWidgets.QWebEngineView(self)

        
        vlayout.addWidget(self.button, alignment=QtCore.Qt.AlignHCenter)
        vlayout.addWidget(self.browser)

        # Enable the maximize button
        layout.setWindowFlags(self.windowFlags() | Qt.WindowMaximizeButtonHint)
      
        self.button.clicked.connect(self.plot_graph)
        layout.resize(1000,800)
        layout.setLayout(vlayout)
        layout.exec_()
        self.Ui.progressBar.hide()

    def plot_graph(self):
        try:
            self.Ui.progressBar.show()
            # self.browser = self.Ui.plotGraph
            df = self.df
            print("DF completed")
            # fig = px.line(df, x="TimeStamp", y="Value", color="Name")
            fig = px.line(df, x="TimeStamp", y="Value", color = "Name", markers=True)    
            print("Fig completed")                                                                              
            self.browser.setHtml(fig.to_html(include_plotlyjs='cdn'))  
            # for i in range (1,20):
            #     df1 = df.head(10000*i)
            #     fig = px.line(df1, x="TimeStamp", y="Value", color = "Name", markers=True)
            #     self.browser.setHtml(fig.to_html(include_plotlyjs='cdn')) 
            #     time.sleep(5000)
            print("HTML completed") 
            self.Ui.progressBar.hide()
        except Exception as e:
            print(f"Error: {e}")
        

    def openWindow(self):
        try:
            if self.dateExp == False and gma(0) == self.macCheck:
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
                revision =  self.dfInfo.loc[1, 'Info']
                print(revision)
                self.versionSet = self.Ui.versionSet
                self.versionSet.setText(revision)
                Licence = self.dfInfo.loc[4, 'Info']
                self.Ui.licenseEnter.setText(Licence)
                
                self.Ui.progressBar.hide()
                self.logImp = self.Ui.logImp
                self.logField = self.Ui.logField
                self.log = self.Ui.textStatus
                self.Ui.show_data_btn.clicked.connect(lambda: self.thread_and_handle(lambda: self.show_data()))
                self.Ui.export_btn.clicked.connect(lambda: self.thread_and_handle(self.export_data))
                self.Ui.btnBackup.clicked.connect(self.select_backup_path)
                self.Ui.btnDownloadExcel.clicked.connect(self.modelExcel)
                self.Ui.activateLicense.clicked.connect(self.licence_main)
                self.Ui.btnConnect.clicked.connect(lambda: self.thread_and_handle(self.plcConnect))
                self.Ui.btnConnect.clicked.connect(self.timer)
                self.Ui.btnDisconnect.clicked.connect(lambda: self.thread_and_handle(self.plcDisconnect))
                self.Ui.btnClearLog.clicked.connect(self.clear_logs)
                # self.Ui.btnShowGraph.clicked.connect(self.plot_graph)
                self.Ui.btnShowGraph.clicked.connect(self.graph)
                self.Ui.navHome.clicked.connect(lambda: self.Ui.stackedWidget.setCurrentWidget(self.Ui.homePage))
                self.Ui.navExport.clicked.connect(lambda: self.Ui.stackedWidget.setCurrentWidget(self.Ui.exportPage))
                self.Ui.navLog.clicked.connect(lambda: self.Ui.stackedWidget.setCurrentWidget(self.Ui.logPage))
                self.Ui.navHelp.clicked.connect(lambda: self.Ui.stackedWidget.setCurrentWidget(self.Ui.helpPage))
                self.Ui.navImp.clicked.connect(lambda: self.Ui.stackedWidget.setCurrentWidget(self.Ui.importPage))
                self.Ui.navAbout.clicked.connect(lambda: self.Ui.stackedWidget.setCurrentWidget(self.Ui.aboutPage))
                self.Ui.btnImpExcel.clicked.connect(self.open_excel_file)
                
            else:
                self.logcon.append('Error Licence expired: Contact admin')

        except Exception as e:
            print(f"Error on opening: {e}")


    def send_email(self): 
         # Define email sender and receiver
        email_sender = 'saravan2406@gmail.com'
        #email_password = os.environ.get("EMAIL_PASSWORD")
        email_password = 'utefbkprwxtdanvc'
        email_receiver = 'saravanan@proliteautomation.com','sureshgopi@proliteautomation.com'
        email_receiver2 = 'saravanan@proliteautomation.com'

        # Set the subject and body of the email
        subject = 'Urgent : Data Logger Connection Error!!!'
        body = """<p><b>Urgent Notice:</b> Our records indicate that your data logger connection has been disrupted.<br>
Please take immediate action to restore the connection to prevent any potential data loss.<br>
Your prompt attention to this matter is greatly appreciated.</p><br>
<p>Please note that this email is sent from an automated system, and replies to this message will not be monitored.<br>
If you require assistance or have any questions, please contact our support team directly.</p>"""
        
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
        self.conn = pyodbc.connect(
            'DRIVER=SQL Server;'
            'SERVER=SURESHGOPI;'
            # 'SERVER=Localhost\SQLEXPRESS;'
            'DATABASE=PLCDB2;'
        )
        self.cursor = self.conn.cursor()
        self.engine = create_engine('mssql+pyodbc://SURESHGOPI/PLCDB2?driver=SQL+Server')
        # self.engine = create_engine('mssql+pyodbc://Localhost\SQLEXPRESS/PLCDB2?driver=SQL+Server')
        self.con = self.engine.connect()

        self.logcon.append('SQL DB is connected')

        self.lic = self.licenseEnter.text()
        print("Licence key", self.lic)
        # Construct the SQL query string with CAST function to convert Particulars to nvarchar
        query = "UPDATE Info_DB SET Info = ? WHERE CAST(Particulars AS NVARCHAR(MAX)) = ?"
        # Execute the query with parameters
        self.cursor.execute(query, (self.lic, "Activation_Key"))
        self.cursor.commit()
        self.date_enc()


    def licence_main(self):
        lic = self.Ui.licenseEnter.text()
        self.licc = self.Ui.licenseEnter.text()
        print("Licence key", lic)
        try:
            lic = self.decrypt(lic)
            self.macCheck = lic[1:]
            self.softwaretypeCheck = int(lic[0])
            if gma(0) == self.macCheck:
                # Construct the SQL query string with CAST function to convert Particulars to nvarchar
                query = "UPDATE Info_DB SET Info = ? WHERE CAST(Particulars AS NVARCHAR(MAX)) = ?"
                # Execute the query with parameters
                self.cursor.execute(query, (self.licc, "Activation_Key"))
                self.cursor.commit()
                msg = "License verified!"
                self.popUp(msg)
            
                
        except Exception as e:
            msg = "Invalid License !!!"
            self.popUp(msg)
            print(f"Error updating license: {e}")
            self.close_application()


    def licence_dec(self):
        query = text('SELECT * FROM Info_DB')
        self.dfInfo = pd.read_sql_query(query, self.con)
        self.mac_ver = '00c:9a:3c:f4:b0:55'
        self.lic = self.licenseEnter.text()
        print("Licence key", self.lic)
        try:
            for index, row in self.dfInfo.iterrows():
                if row['Particulars'] == 'Activation_Key':
                    lic = row['Info']
                    print("Licience:", lic)
            self.lic = self.decrypt(lic)
            self.macCheck = self.lic[1:]
            self.softwaretypeCheck = int(self.lic[0])

        except Exception as e:
            print(f"Error updating license: {e}")

    def date_enc(self):
        date = '30/04/2024'
        Software_sold_date = self.encrypt(date) 
        print(Software_sold_date)
        Software_sold_date = Software_sold_date.decode('utf-8')
        try:
            # Construct the SQL query string with CAST function to convert Particulars to nvarchar
            query = "UPDATE Info_DB SET Info = ? WHERE CAST(Particulars AS NVARCHAR(MAX)) = ?"
            # Execute the query with parameters
            self.cursor.execute(query, (Software_sold_date, "Software_sold_date"))
            self.cursor.commit()
            # Software_sold_date = Software_sold_date.decode('utf-8')
            soft = self.decrypt(Software_sold_date)
            print(soft)
            
        except Exception as e:
            print(f"Error updating license: {e}")
        

    def encrypt (self, enc_msg):
        # Fixed encryption key (ensure it's kept secure)
        crypto_key = b'9tvb2SoOaB11TA4YN3CydnGq4IfvSVSZJy25B6bdskM='
        # Initialize Fernet with the encryption key
        fernet = Fernet(crypto_key)
        # Encrypt the MAC address
        # enc_msg = enc_msg.decode('utf-8')
        enc_mac = fernet.encrypt(enc_msg.encode())
        return enc_mac


    def decrypt (self, dec_msg):
        crypto_key = b'9tvb2SoOaB11TA4YN3CydnGq4IfvSVSZJy25B6bdskM='

        # Initialize Fernet with the encryption key
        fernet = Fernet(crypto_key)
        # Encrypt the MAC address

        enc_macid = dec_msg.encode('utf-8')
        print("Print Enc mac " ,enc_macid)
        # Decrypt the encrypted MAC address (optional)
        dec_mac = fernet.decrypt(enc_macid).decode()
        return dec_mac

    def select_backup_path(self):
        root = Tk()
        root.withdraw()  # Hide the main window

        # # Prompt user to select backup file path
        self.backup_path = filedialog.asksaveasfilename(defaultextension=".bak",
                                                    filetypes=[("Backup files", "*.bak"), ("All files", "*.*")])
        # self.backup_path = "C:\Program Files\Microsoft SQL Server\MSSQL16.MSSQLSERVER\MSSQL\Backup\PLCDB2.bak"
        server_name = 'SURESHGOPI'
        # server_name = 'Localhost\SQLEXPRESS'
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
            message = 'File Backuped Successful'
            self.log_to_file(message)
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
        for index, row in self.dfInfo.iterrows():               
            if row['Particulars'] == 'Software_sold_date':
                Software_sold_date = row['Info']
                Software_sold_date = self.decrypt(Software_sold_date)
                print("Release Date String:", Software_sold_date)
                
                try:
                    # Assuming the date format is 'DD/MM/YYYY'
                    Software_date = datetime.strptime(Software_sold_date, '%d/%m/%Y')
                    print("Release Date:", Software_date)
                    
                    self.current_date = datetime.now()
                    print(self.current_date)

                    if self.softwaretypeCheck == 0:
                        a = (self.current_date - Software_date ).days
                        print(a)
                        # Check if the software is within the allowed time period (1 month)
                        if (self.current_date - Software_date ).days < 30:
                            self.dateExp = False
                            print("Date Expired:", self.dateExp) 
                        else:
                            self.dateExp = True
                            self.logcon.append("License Expired" )
                            print("Date Expired:", self.dateExp)
                        
                except ValueError as e:
                    print("Error parsing release date:", e)
                    
    
        return self.dateExp
 
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
                # 'SERVER=Localhost\SQLEXPRESS;'
                'DATABASE=PLCDB2;'
            )
            self.cursor = self.conn.cursor()
            self.engine = create_engine('mssql+pyodbc://SURESHGOPI/PLCDB2?driver=SQL+Server')
            # self.engine = create_engine('mssql+pyodbc://Localhost\SQLEXPRESS/PLCDB2?driver=SQL+Server')
            self.con = self.engine.connect()

            self.logcon.append('SQL DB is connected')

            self.licence_dec()
            self.restrict_soft()
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
            query = text('SELECT * FROM Info_DB')
            self.dfInfo = pd.read_sql_query(query, self.con)
            if self.plcIP == "":
                self.plcIP = self.dfInfo.loc[0, 'Info']               
                self.current_date = datetime.now()
                self.plc = snap7.client.Client()
                self.plc.connect(self.plcIP, 0, 1)
                print("PLC Connected" , self.plc)
                print("DB Connected", self.cursor)
                print("DB Connected", self.conn)
                self.log.append('PLC is connected'  +  str(self.current_date))
                message = 'Info  - '  + str(self.current_date) + ' -  PLC is connected ' 
                self.log_to_file(message)
                self.local_connStatus = True
                self.dfPlc()
                self.run_logging()
            elif self.plcIP:
                query = "UPDATE Info_DB SET Info = ? WHERE CAST(Particulars AS NVARCHAR(MAX)) = ?"
                # Execute the query with parameters
                self.cursor.execute(query, (self.plcIP, "Plc_IP"))
                self.cursor.commit()
                self.current_date = datetime.now()
                self.plc = snap7.client.Client()
                self.plc.connect(self.plcIP, 0, 1)
                print("PLC Connected" , self.plc)
                print("DB Connected", self.cursor)
                print("DB Connected", self.conn)
                self.log.append('PLC is connected'  +  str(self.current_date))
                message = 'Info  - '  + str(self.current_date) + ' -  PLC is connected ' 
                self.log_to_file(message)
                self.local_connStatus = True
                self.dfPlc()
                self.run_logging()
            else:
                self.log.append(f'PLC IP: {e}') 
                print("PLC IP address is not provided.")
                # You might want to inform the user or take appropriate action here
        except Exception as e:
            self.log.append(f'PLC is not connected: {e}') 
            print("Not connecting", e)
            self.logField.append(f"Error : {e}")
            self.monitor_timer.stop()
            self.local_connStatus = False
            self.send_email()
        return self.local_connStatus

    def plcDisconnect(self):
        try:
            self.current_date = datetime.now()
            self.plc.disconnect()
            self.log.append('PLC is Disconnected'+ str(self.current_date))
            self.local_connStatus = False
            self.monitor_timer.stop()
            # message = 'PLC data fetching Disconnected' + str(self.current_date)
            message = '"Alert"  - '  + str(self.current_date) + ' -  PLC data fetching Disconnected ' 
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
        try:
            print("Software Type:", self.softwaretypeCheck)
            if self.softwaretypeCheck == 0 or self.softwaretypeCheck == 1:
                print("Software Type:", self.softwaretypeCheck)
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
        self.monitor_timer = QTimer(self)
        self.monitor_timer.timeout.connect(self.timer1)
        self.monitor_timer.start(5000)
        
    def timer1 (self):
        if self.local_conn == False:                
            self.plcConnect() 
        elif self.local_connStatus == True:
            self.run_logging()
        else:
            print("true")


    # def sleep(self):
    #     self.run_logging()
    #     time.sleep(5)

    def run_logging(self):
        try: 
            if self.local_connStatus == True:
                self.current_date = datetime.now()
                message = 'Data fetching from PLC '
                message = 'Logging  - '  + str(self.current_date) + ' -  Data fetching from PLC ' 
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
                self.local_conn = True
                
        except Exception as e:
            self.monitor_timer.stop()
            self.local_conn = False
            self.logField.append(f"Error : {e}")
            self.send_email() 
      
    def plcDataSnap7(self, db_number, data_type, start_offset, bit_offset):
        try: 
            if data_type == 'BOOL':
                reading = self.plc.db_read(db_number, start_offset, 1)
                value = snap7.util.get_bool(reading, 0, bit_offset)
            elif data_type == 'REAL':
                reading = self.plc.db_read(db_number, start_offset, 4)
                value = round(struct.unpack('>f', reading)[0], 2)
                # real_value = snap7.util.get_real(reading, 188)
                # value = round(real_value, 2)
            elif data_type == 'INT':
                reading = self.plc.db_read(db_number, start_offset, 2)
                value = struct.unpack('>h', reading)[0]
            else:
                print("Unsupported data type:", data_type)
                return None
            
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]

            return value, timestamp  
        except Exception as e:
            self.monitor_timer.stop()
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
    
    # def show_data(self):
    #     from_time = self.Ui.from_time.dateTime().toString(Qt.ISODate)
    #     to_time = self.Ui.to_time.dateTime().toString(Qt.ISODate)

    #     try:
    #         self.Ui.progressBar.show()            
    #         # Query database for data between specified timestamps
    #         query = "SELECT * FROM plc_data WHERE TimeStamp BETWEEN ? AND ?"
    #         df = pd.read_sql_query(query, self.con, params=(from_time, to_time))
    #         print(df)
    #         self.df = df
    #         self.model = PandasTableModel(df)
    #         self.Ui.table_view.setModel(self.model)
    #         self.Ui.table_view.setSortingEnabled(True)
    #         self.Ui.table_view.resizeColumnToContents(0)
    #         # header = self.Ui.table_view.horizontalHeader()
    #         # header.setSectionResizeMode(0, 1000)
    #         # header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
    #         # header.setSectionResizeMode(2, QHeaderView.ResizeToContents)
    #         # header.setSectionResizeMode(3, QHeaderView.ResizeToContents)
    #         # header.setSectionResizeMode(4, QHeaderView.ResizeToContents)
    #         # # header.setSectionResizeMode(4, QHeaderView.ResizeToContents)
    #         # self.Ui.table_view.horizontalHeader().setStretchLastSection(True)
    #         self.Ui.progressBar.hide()
    #         # self.pdtable.setModel(self.model)
    #     except Exception as e:
    #         self.logImp.append(f"Error: {e}")

    def show_data(self):
        from_time = self.Ui.from_time.dateTime().toString(Qt.ISODate)
        to_time = self.Ui.to_time.dateTime().toString(Qt.ISODate)

        try:
            self.Ui.progressBar.show()
            # Query database for data between specified timestamps
            query = "SELECT * FROM plc_data WHERE TimeStamp BETWEEN ? AND ?"
            df = pd.read_sql_query(query, self.con, params=(from_time, to_time))
            print(df)
            self.df = df
            self.model = PandasTableModel(df)
            self.Ui.table_view.setModel(self.model)
            self.Ui.table_view.setSortingEnabled(True)

           # Set a fixed width for all columns
            self.Ui.table_view.setColumnWidth(0, 150)
            self.Ui.table_view.setColumnWidth(1, 300)
            self.Ui.table_view.setColumnWidth(2, 500)
            self.Ui.table_view.setColumnWidth(3, 150)
            self.Ui.table_view.setColumnWidth(4, 150)

        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            self.Ui.progressBar.hide()


    def export_data(self):
        from_time = self.Ui.from_time.dateTime().toString(Qt.ISODate)
        to_time = self.Ui.to_time.dateTime().toString(Qt.ISODate)
        try:
            self.Ui.progressBar.show()            
            query = "SELECT * FROM plc_data WHERE TimeStamp BETWEEN ? AND ?"
            self.df = pd.read_sql_query(query, self.con, params=(from_time, to_time))
            #  # Check if DataFrame is available
            if self.df is None:
                return  # No data to export
                
            # Export DataFrame to Excel file
            file_name, _ = QFileDialog.getSaveFileName(self, "Save File", "", "Excel files (*.xlsx)")
            if file_name:
                self.df.to_excel(file_name, index=False)
            self.Ui.progressBar.hide()
        except Exception as e:
                self.logImp.append(f"Error: {e}")

    def check_variables(self):
        self.restrict_soft()
        # Check if self.local_A or self.dateExp is False
        if self.dateExp == True and gma(0) == self.macCheck:
            # Perform actions when either variable becomes False
            self.close_application()

    def close_application(self):
        # Close the application
        self.Ui.close()


class PandasTableModel(QAbstractTableModel):
    def __init__(self, data):
        super(PandasTableModel, self).__init__()
        self._data = data

    def rowCount(self, parent=None):
        return self._data.shape[0]

    def columnCount(self, parent=None):
        return self._data.shape[1]

    def data(self, index, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            value = self._data.iloc[index.row(), index.column()]
            return str(value)
        return None

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self._data.columns[section])
            elif orientation == Qt.Vertical:
                return str(section + 1)
        return None

if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    Mainwindow = PLCDataLogger()
    Mainwindow.show()
    sys.exit(app.exec_())