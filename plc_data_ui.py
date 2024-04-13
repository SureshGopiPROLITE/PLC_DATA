# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Plc_data.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(974, 891)
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
        self.widget.setGeometry(QtCore.QRect(10, 0, 951, 841))
        self.widget.setObjectName("widget")
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
        self.widget_3.setGeometry(QtCore.QRect(-1, 90, 191, 741))
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
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.navHome = QtWidgets.QPushButton(self.widget_3)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.navHome.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icons/home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.navHome.setIcon(icon)
        self.navHome.setIconSize(QtCore.QSize(20, 20))
        self.navHome.setObjectName("navHome")
        self.verticalLayout.addWidget(self.navHome)
        self.navExport = QtWidgets.QPushButton(self.widget_3)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.navExport.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Icons/export.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.navExport.setIcon(icon1)
        self.navExport.setIconSize(QtCore.QSize(20, 20))
        self.navExport.setObjectName("navExport")
        self.verticalLayout.addWidget(self.navExport)
        self.navLog = QtWidgets.QPushButton(self.widget_3)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.navLog.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/Icons/lod.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.navLog.setIcon(icon2)
        self.navLog.setIconSize(QtCore.QSize(20, 20))
        self.navLog.setObjectName("navLog")
        self.verticalLayout.addWidget(self.navLog)
        self.navHelp = QtWidgets.QPushButton(self.widget_3)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.navHelp.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/Icons/help.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.navHelp.setIcon(icon3)
        self.navHelp.setIconSize(QtCore.QSize(20, 20))
        self.navHelp.setObjectName("navHelp")
        self.verticalLayout.addWidget(self.navHelp)
        self.navImp = QtWidgets.QPushButton(self.widget_3)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.navImp.setFont(font)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/Icons/import.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.navImp.setIcon(icon4)
        self.navImp.setIconSize(QtCore.QSize(20, 20))
        self.navImp.setObjectName("navImp")
        self.verticalLayout.addWidget(self.navImp)
        spacerItem = QtWidgets.QSpacerItem(20, 118, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.stackedWidget = QtWidgets.QStackedWidget(self.widget)
        self.stackedWidget.setGeometry(QtCore.QRect(200, 100, 741, 751))
        self.stackedWidget.setObjectName("stackedWidget")
        self.homePage = QtWidgets.QWidget()
        self.homePage.setObjectName("homePage")
        self.widget_4 = QtWidgets.QWidget(self.homePage)
        self.widget_4.setGeometry(QtCore.QRect(-10, 20, 741, 741))
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
        self.textStatus.setGeometry(QtCore.QRect(40, 180, 631, 521))
        self.textStatus.setObjectName("textStatus")
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
        self.importPage = QtWidgets.QWidget()
        self.importPage.setObjectName("importPage")
        self.widget_5 = QtWidgets.QWidget(self.importPage)
        self.widget_5.setGeometry(QtCore.QRect(-20, -20, 741, 621))
        self.widget_5.setStyleSheet("QWidget{\n"
"background-color: #191C24;\n"
"}\n"
"")
        self.widget_5.setObjectName("widget_5")
        self.btnImpExcel = QtWidgets.QPushButton(self.widget_5)
        self.btnImpExcel.setGeometry(QtCore.QRect(270, 210, 171, 61))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.btnImpExcel.setFont(font)
        self.btnImpExcel.setObjectName("btnImpExcel")
        self.logImp = QtWidgets.QTextEdit(self.importPage)
        self.logImp.setGeometry(QtCore.QRect(0, 650, 741, 91))
        self.logImp.setObjectName("logImp")
        self.stackedWidget.addWidget(self.importPage)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 974, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "PLC Data"))
        self.navHome.setText(_translate("MainWindow", "Home"))
        self.navExport.setText(_translate("MainWindow", "Export"))
        self.navLog.setText(_translate("MainWindow", "Log"))
        self.navHelp.setText(_translate("MainWindow", "Help"))
        self.navImp.setText(_translate("MainWindow", "Import Excel"))
        self.btnConnect.setText(_translate("MainWindow", "Connect"))
        self.btnDisconnect.setText(_translate("MainWindow", "Disconnect"))
        self.label_3.setText(_translate("MainWindow", "To :"))
        self.export_btn.setText(_translate("MainWindow", "Export Excel"))
        self.show_data_btn.setText(_translate("MainWindow", "Show Data"))
        self.label_2.setText(_translate("MainWindow", "From :"))
        self.btnImpExcel.setText(_translate("MainWindow", "Open"))
# import Icons_reso_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
