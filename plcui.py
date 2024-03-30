import sys
from PyQt5.QtWidgets import QApplication, QDialog, QFileDialog, QMainWindow
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt
import pyodbc
import pandas as pd
from PyQt5.QtWidgets import QMainWindow


class MainWindow(QMainwindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi('plc_data.ui', self)  # Load the UI file

        self.show_data_btn.clicked.connect(self.show_data)
        self.export_btn.clicked.connect(self.export_data)  # Connect export button to export_data method

        # Connect to SQL Server database
        self.conn = pyodbc.connect(
            'DRIVER=SQL Server;'
            'SERVER=SURESHGOPI;'
            'DATABASE=PLCDB2;'
        )
        self.cursor = self.conn.cursor()

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
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
