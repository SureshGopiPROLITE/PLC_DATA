# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Welcome_plc.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(876, 554)
        MainWindow.setStyleSheet("background-color: rgb(20, 20, 20);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("/* Set background colors and properties */\n"
"QFrame#mainFrame{\n"
"background-color: #f0f0f0;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"QFrame#contentFrame{\n"
"background-color: #fff;\n"
"}\n"
"\n"
"QFrame#leftMenuFrame{\n"
"background-color: #36647b;\n"
"}\n"
"\n"
"QWidget#page_License {\n"
"background-color: #f0f0f0;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"color:rgb(255, 166, 0);\n"
"background-color: rgb(88, 88, 88);\n"
"}\n"
"QCheckBox{\n"
"font:  \"Poppins\";\n"
"font-weight: bold;\n"
"font-size: 8pt;\n"
"color: #D7DBEC;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"QPushButton{\n"
" font: 12pt \"Poppins\";\n"
" color:white;\n"
" height:40px;\n"
" border-radius: 5px;\n"
" height:40px;\n"
" width:150px;\n"
"border:2px solid #D7DBEC;\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:hover{\n"
"color:rgb(255, 166, 0);\n"
"}\n"
"\n"
"/* Styles for Tab Widgets */\n"
"QTabWidget::pane {\n"
"border:1px solid lightgray;\n"
"/*background: rgb(245, 245, 245);*/\n"
"\n"
"} \n"
"\n"
"QTabBar::tab {\n"
"/*background: rgb(230, 230, 230);*/ \n"
"background-color: #191C24;\n"
"color:#F1F1F2;\n"
"border: 1px solid lightgray; \n"
"padding: 10px 30px 10px 30px;\n"
"margin:1px;\n"
"} \n"
"QTabBar::tab:hover {\n"
"    background-color:#343434;\n"
"    border-top-left-radius: 5px; \n"
"    border-top-right-radius: 5px; \n"
"    border-bottom-left-radius: 0px; \n"
"    border-bottom-right-radius: 0px; \n"
"} \n"
"\n"
"QTabBar::tab:selected {\n"
"    background: rgb(88,88,88);\n"
"    color:rgb(255, 166, 0);\n"
"    margin-bottom: -1px; \n"
"}\n"
"\n"
"/* QLabel settings */\n"
"QLabel#SettingBg1{\n"
"border-radius: 5px;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgba(40, 40, 40, 0.2);\n"
"\n"
"}\n"
"\n"
"QLabel#SettingBg2{\n"
"border-radius: 5px;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgba(40, 40, 40, 0.2);\n"
"}\n"
"\n"
"QLabel#SettingBg3{\n"
"border-radius: 5px;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgba(40, 40, 40, 0.2);\n"
"}\n"
"\n"
"QLabel#SettingBg4{\n"
"font: 14pt \"Poppins\";\n"
"border-radius: 5px;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color:  rgba(40, 40, 40, 0.2);\n"
"}\n"
"\n"
"QLabel {\n"
"font-size: 12pt;\n"
"font:75  \"Poppins\";\n"
"font-weight: bold;\n"
"color: #D7DBEC;\n"
"background-color: #191C24;\n"
"/*font-family: Noto Sans;*/\n"
"}\n"
"\n"
"/* Global combobox settings */\n"
"QComboBox{\n"
"text-align: center;\n"
"border-radius: 5px;\n"
"border:2px solid #D7DBEC;\n"
"color: #D7DBEC;\n"
"padding: 2px;\n"
"font-weight: bold;\n"
"font-size: 8pt;\n"
"height:40px;\n"
"width:150px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"border: 0px; /* This seems to replace the whole arrow of the combo box */\n"
"\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    text-align: center;\n"
"    qproperty-alignment: AlignCenter;\n"
"    background-color: white; /* Background color */\n"
"    color: #F1F1F2; /* Text color */\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"image: url(img/Arrows-Down-4-icon.png);\n"
"width: 10px;\n"
"height: 10px;\n"
"}\n"
"\n"
"QComboBox:hover{\n"
"color:rgb(255, 166, 0);\n"
"background-color:white;\n"
"/*border: 2px solid #252429;\n"
"color: #252429;*/\n"
"}\n"
"\n"
"QTableView{\n"
"color: rgb(31, 31, 31);\n"
"background-color: rgb(209, 209, 209);\n"
"}\n"
"\n"
"QHeaderView::section { \n"
"font: 75 10pt \"Poppins\";\n"
"color: white;\n"
"background-color:#989898; \n"
"}\n"
"\n"
"QDateTimeEdit{\n"
"background-color: rgb(81, 81, 81);\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QTableView::item { \n"
"font: 75 12pt \"Poppins\";\n"
"color:white; \n"
"background:#2f373d; \n"
"font-weight:900; \n"
"}\n"
"QTableView::item:selected {\n"
"font: 75 12pt \"Poppins\"; \n"
"color:black; \n"
"background:#7cc8b9; \n"
"font-weight:900; \n"
"}\n"
"QTableView{\n"
"color: rgb(31, 31, 31);\n"
"background-color: rgb(25, 28, 36);\n"
"}\n"
"\n"
"QTextEdit{\n"
"background-color: rgb(25, 28, 36);\n"
"color: rgb(255, 255, 255);\n"
"font: 8pt \"Poppins\";\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 0, 861, 511))
        self.widget.setObjectName("widget")
        self.connStatus = QtWidgets.QTextEdit(self.widget)
        self.connStatus.setGeometry(QtCore.QRect(30, 410, 801, 91))
        self.connStatus.setObjectName("connStatus")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setGeometry(QtCore.QRect(30, 30, 801, 371))
        self.widget_2.setStyleSheet("QWidget{\n"
"background-color: #191C24;\n"
"}")
        self.widget_2.setObjectName("widget_2")
        self.btnConnectDb = QtWidgets.QPushButton(self.widget_2)
        self.btnConnectDb.setGeometry(QtCore.QRect(330, 250, 154, 44))
        self.btnConnectDb.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.btnConnectDb.setObjectName("btnConnectDb")
        self.label = QtWidgets.QLabel(self.widget_2)
        self.label.setGeometry(QtCore.QRect(290, 30, 231, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(320, 350, 251, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("")
        self.label_2.setObjectName("label_2")
        self.widget_2.raise_()
        self.connStatus.raise_()
        self.label_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 876, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnConnectDb.setText(_translate("MainWindow", "Connect DB"))
        self.label.setText(_translate("MainWindow", "Welcome To PLCInsight Pro"))
        self.label_2.setText(_translate("MainWindow", "Click on connect to Logging"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
