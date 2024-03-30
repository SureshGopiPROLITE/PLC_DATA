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
from timeloop import Timeloop



class Worker(QThread):
    data_logged = pyqtSignal(str)

    # def __init__(self, offsets_df, plc, cursor, conn):
    #     super(Worker, self).__init__()
    #     self.offsets_df = offsets_df
    #     self.plc = plc
    #     self.cursor = cursor
    #     self.conn = conn

    def plc_connect(self):
        # if self.worker is None or not self.worker.isRunning():
            self.offsets_df = pd.read_excel("C:\prolite\Plc_data\PLC_DB_Access.xlsx")
            try:
                self.plc = snap7.client.Client()
                self.plc.connect('192.168.0.1', 0, 1)

                self.conn = pyodbc.connect(
                    'DRIVER=SQL Server;'
                    'SERVER=SURESHGOPI;'
                    'DATABASE=PLCDB2;'
                )
                self.cursor = self.conn.cursor()
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                self.log.append('PLC is connected', timestamp)
                self.run()

                self.worker = Worker(self.offsets_df, self.plc, self.cursor, self.conn)
                self.worker.data_logged.connect(self.update_log)
                self.worker.start()

            except Exception as e:
                self.log.append('PLC is not connected: {}'.format(e))
        # else:
            # self.log.append('PLC connection is already in progress.')

    def plc_disconnect(self):
        # if self.worker and self.worker.isRunning():
            # self.worker.quit()  # Request the thread to exit
            # self.worker.wait()  # Wait for the thread to exit
        t1.stop()
        self.log.append('PLC is Disconnected')

    def update_log(self, message):
        self.log.append(message)


    def run(self):
        try:
            if t2 == True:
                for index, row in self.offsets_df.iterrows():
                    db_number = row['db_number']
                    start_offset = row['start_offset']
                    data_type = row['data_type']
                    name = row['Name']
                    bit_offset = row['bit_offset']
                    self.read_and_insert(db_number, start_offset, data_type, bit_offset, name)
                time.sleep(5)
            

        except KeyboardInterrupt:
            print("Program terminated by user.")

        finally:
            self.cursor.close()
            self.conn.close()
            self.plc.disconnect()

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

        self.data_logged.emit(log_message)

        self.cursor.execute('''INSERT INTO plc_data (TimeStamp, Name, DataType, Value)
                            VALUES (?, ?, ?, ?)''', (timestamp, name, data_type, value))
        self.conn.commit()




class PLCDataLogger(QMainWindow):
    def __init__(self):
        super(PLCDataLogger, self).__init__()
        loadUi('plc_data.ui', self)

        self.show_data_btn.clicked.connect(self.show_data)
        self.export_btn.clicked.connect(self.export_data)
        self.btnConnect.clicked.connect(self.plc_connect)
        self.btnDisconnect.clicked.connect(self.plc_disconnect)
        self.navHome.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.homePage))
        self.navExport.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.exportPage))
        self.navLog.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.logPage))
        self.navHelp.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.helpPage))

        self.log = self.findChild(QtWidgets.QTextEdit, 'textStatus')

        self.worker = None


    
    
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
t2 = PLCDataLogger()
# t1 = Worker()
   

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PLCDataLogger()
    window.show()
    sys.exit(app.exec_())
