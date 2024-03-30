# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'plc_data.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(962, 891)
        MainWindow.setStyleSheet("background-color: rgb(20, 20, 20);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("/* Set background colors and properties */\n"
"QFrame#mainFrame{\n"
"background-color: #f0f0f0;\n"
"}\n"
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
"/* Global styles for buttons */\n"
"QPushButton{\n"
"/*background-color: #383838;*/\n"
"border-radius: 5px;\n"
"border:2px solid #D7DBEC;;\n"
"font-weight: bold;\n"
"font-size: 8pt;\n"
"background:#2f373d; \n"
"/*font-family: Noto Sans;*/\n"
"font: 75 10pt \"Poppins\";\n"
"color: #fff;\n"
"height:40px;\n"
"width:150px;\n"
"}\n"
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
"font-size: 8pt;\n"
"font:75  \"Poppins\";\n"
"font-weight: bold;\n"
"color: #D7DBEC;\n"
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
        self.widget.setGeometry(QtCore.QRect(10, 0, 991, 841))
        self.widget.setObjectName("widget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.widget)
        self.stackedWidget.setGeometry(QtCore.QRect(200, 90, 741, 751))
        self.stackedWidget.setObjectName("stackedWidget")
        self.homePage = QtWidgets.QWidget()
        self.homePage.setObjectName("homePage")
        self.widget_4 = QtWidgets.QWidget(self.homePage)
        self.widget_4.setGeometry(QtCore.QRect(0, 10, 701, 741))
        self.widget_4.setStyleSheet("QWidget{\n"
"background-color: #191C24;\n"
"}\n"
"")
        self.widget_4.setObjectName("widget_4")
        self.gridLayoutWidget = QtWidgets.QWidget(self.widget_4)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(40, 50, 631, 123))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.btnConnect = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnConnect.setObjectName("btnConnect")
        self.gridLayout.addWidget(self.btnConnect, 0, 0, 1, 1)
        self.btnDisconnect = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnDisconnect.setObjectName("btnDisconnect")
        self.gridLayout.addWidget(self.btnDisconnect, 0, 1, 1, 1)
        self.textStatus = QtWidgets.QTextEdit(self.widget_4)
        self.textStatus.setGeometry(QtCore.QRect(40, 180, 631, 221))
        self.textStatus.setObjectName("textStatus")
        self.listView = QtWidgets.QListView(self.widget_4)
        self.listView.setGeometry(QtCore.QRect(40, 420, 631, 241))
        self.listView.setObjectName("listView")
        self.stackedWidget.addWidget(self.homePage)
        self.exportPage = QtWidgets.QWidget()
        self.exportPage.setObjectName("exportPage")
        self.label_3 = QtWidgets.QLabel(self.exportPage)
        self.label_3.setGeometry(QtCore.QRect(310, 40, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.from_time = QtWidgets.QDateTimeEdit(self.exportPage)
        self.from_time.setGeometry(QtCore.QRect(70, 40, 191, 31))
        self.from_time.setObjectName("from_time")
        self.to_time = QtWidgets.QDateTimeEdit(self.exportPage)
        self.to_time.setGeometry(QtCore.QRect(350, 40, 194, 22))
        self.to_time.setObjectName("to_time")
        self.export_btn = QtWidgets.QPushButton(self.exportPage)
        self.export_btn.setGeometry(QtCore.QRect(570, 90, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.export_btn.setFont(font)
        self.export_btn.setObjectName("export_btn")
        self.show_data_btn = QtWidgets.QPushButton(self.exportPage)
        self.show_data_btn.setGeometry(QtCore.QRect(570, 160, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.show_data_btn.setFont(font)
        self.show_data_btn.setObjectName("show_data_btn")
        self.table_view = QtWidgets.QTableView(self.exportPage)
        self.table_view.setGeometry(QtCore.QRect(10, 80, 541, 511))
        self.table_view.setObjectName("table_view")
        self.label_2 = QtWidgets.QLabel(self.exportPage)
        self.label_2.setGeometry(QtCore.QRect(20, 40, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3.raise_()
        self.to_time.raise_()
        self.export_btn.raise_()
        self.show_data_btn.raise_()
        self.table_view.raise_()
        self.label_2.raise_()
        self.from_time.raise_()
        self.stackedWidget.addWidget(self.exportPage)
        self.logPage = QtWidgets.QWidget()
        self.logPage.setObjectName("logPage")
        self.logField = QtWidgets.QTextEdit(self.logPage)
        self.logField.setGeometry(QtCore.QRect(0, 30, 731, 681))
        self.logField.setObjectName("logField")
        self.stackedWidget.addWidget(self.logPage)
        self.helpPage = QtWidgets.QWidget()
        self.helpPage.setObjectName("helpPage")
        self.stackedWidget.addWidget(self.helpPage)
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setGeometry(QtCore.QRect(0, -10, 941, 101))
        self.widget_2.setStyleSheet("QWidget{\n"
"background-color: rgb(25, 28, 36);\n"
"}\n"
"QPushButton{\n"
" font: 12pt \"Poppins\";\n"
" border:none;\n"
"}\n"
"QPushButton:checked{\n"
"color: rgb(248, 172, 35);\n"
"background-color: rgb(0, 0, 0);\n"
"border-color: rgb(248, 172, 35);\n"
"border-color: rgb(251, 220, 175);\n"
"}\n"
"")
        self.widget_2.setObjectName("widget_2")
        self.label = QtWidgets.QLabel(self.widget_2)
        self.label.setGeometry(QtCore.QRect(410, 30, 141, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("font: 24pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setGeometry(QtCore.QRect(-1, 90, 191, 751))
        self.widget_3.setStyleSheet("\n"
"QPushButton{\n"
" font: 12pt \"Poppins\";\n"
" color:white;\n"
" text-align:left;\n"
" height:40px;\n"
" border:none;\n"
" padding-left:10px;\n"
"}\n"
"QPushButton:checked{\n"
"color:rgb(255, 166, 0);\n"
"background-color: rgb(88, 88, 88);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:#343434;\n"
"}\n"
"\n"
"QWidget{\n"
"background-color: #191C24;\n"
"}\n"
"")
        self.widget_3.setObjectName("widget_3")
        self.navHome = QtWidgets.QPushButton(self.widget_3)
        self.navHome.setGeometry(QtCore.QRect(20, 20, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.navHome.setFont(font)
        self.navHome.setObjectName("navHome")
        self.navExport = QtWidgets.QPushButton(self.widget_3)
        self.navExport.setGeometry(QtCore.QRect(20, 70, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.navExport.setFont(font)
        self.navExport.setObjectName("navExport")
        self.navLog = QtWidgets.QPushButton(self.widget_3)
        self.navLog.setGeometry(QtCore.QRect(20, 120, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.navLog.setFont(font)
        self.navLog.setObjectName("navLog")
        self.navHelp = QtWidgets.QPushButton(self.widget_3)
        self.navHelp.setGeometry(QtCore.QRect(20, 170, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.navHelp.setFont(font)
        self.navHelp.setObjectName("navHelp")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 962, 21))
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
        self.btnConnect.setText(_translate("MainWindow", "Connect"))
        self.btnDisconnect.setText(_translate("MainWindow", "Disconnect"))
        self.label_3.setText(_translate("MainWindow", "To :"))
        self.export_btn.setText(_translate("MainWindow", "Export Excel"))
        self.show_data_btn.setText(_translate("MainWindow", "Show Data"))
        self.label_2.setText(_translate("MainWindow", "From :"))
        self.label.setText(_translate("MainWindow", "PLC Data"))
        self.navHome.setText(_translate("MainWindow", "Home"))
        self.navExport.setText(_translate("MainWindow", "Export"))
        self.navLog.setText(_translate("MainWindow", "Log"))
        self.navHelp.setText(_translate("MainWindow", "Help"))
import main_icons_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
