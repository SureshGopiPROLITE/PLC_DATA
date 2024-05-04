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
        MainWindow.resize(1922, 1102)
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
        self.widget.setGeometry(QtCore.QRect(10, 0, 1901, 1080))
        self.widget.setObjectName("widget")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setGeometry(QtCore.QRect(0, -10, 1881, 81))
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
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("font: 24pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setGeometry(QtCore.QRect(-1, 70, 261, 931))
        self.widget_3.setStyleSheet("\n"
"QPushButton{\n"
" font: 14pt \"Poppins\";\n"
" color:white;\n"
" text-align:left;\n"
" height:40px;\n"
" border:none;\n"
" padding-left:10px;\n"
"}\n"
"QPushButton:checked{\n"
"color:rgb(255, 166, 0);\n"
"background-color:#18202f;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:#18202f;\n"
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
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.navHome.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icons/home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.navHome.setIcon(icon)
        self.navHome.setIconSize(QtCore.QSize(25, 25))
        self.navHome.setCheckable(True)
        self.navHome.setAutoExclusive(True)
        self.navHome.setObjectName("navHome")
        self.verticalLayout.addWidget(self.navHome)
        self.navExport = QtWidgets.QPushButton(self.widget_3)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.navExport.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Icons/export.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.navExport.setIcon(icon1)
        self.navExport.setIconSize(QtCore.QSize(25, 25))
        self.navExport.setCheckable(True)
        self.navExport.setAutoExclusive(True)
        self.navExport.setObjectName("navExport")
        self.verticalLayout.addWidget(self.navExport)
        self.navLog = QtWidgets.QPushButton(self.widget_3)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.navLog.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/Icons/log.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.navLog.setIcon(icon2)
        self.navLog.setIconSize(QtCore.QSize(25, 25))
        self.navLog.setCheckable(True)
        self.navLog.setAutoExclusive(True)
        self.navLog.setObjectName("navLog")
        self.verticalLayout.addWidget(self.navLog)
        self.navHelp = QtWidgets.QPushButton(self.widget_3)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.navHelp.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/Icons/help.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.navHelp.setIcon(icon3)
        self.navHelp.setIconSize(QtCore.QSize(25, 25))
        self.navHelp.setCheckable(True)
        self.navHelp.setAutoExclusive(True)
        self.navHelp.setObjectName("navHelp")
        self.verticalLayout.addWidget(self.navHelp)
        self.navAbout = QtWidgets.QPushButton(self.widget_3)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.navAbout.setFont(font)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/Icons/about.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.navAbout.setIcon(icon4)
        self.navAbout.setIconSize(QtCore.QSize(25, 25))
        self.navAbout.setCheckable(True)
        self.navAbout.setAutoExclusive(True)
        self.navAbout.setObjectName("navAbout")
        self.verticalLayout.addWidget(self.navAbout)
        self.navImp = QtWidgets.QPushButton(self.widget_3)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.navImp.setFont(font)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/Icons/import.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.navImp.setIcon(icon5)
        self.navImp.setIconSize(QtCore.QSize(25, 25))
        self.navImp.setCheckable(True)
        self.navImp.setAutoExclusive(True)
        self.navImp.setObjectName("navImp")
        self.verticalLayout.addWidget(self.navImp)
        spacerItem = QtWidgets.QSpacerItem(20, 118, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.stackedWidget = QtWidgets.QStackedWidget(self.widget)
        self.stackedWidget.setGeometry(QtCore.QRect(280, 100, 1601, 911))
        self.stackedWidget.setObjectName("stackedWidget")
        self.homePage = QtWidgets.QWidget()
        self.homePage.setObjectName("homePage")
        self.widget_4 = QtWidgets.QWidget(self.homePage)
        self.widget_4.setGeometry(QtCore.QRect(-10, 0, 1611, 911))
        self.widget_4.setStyleSheet("QWidget{\n"
"background-color: #191C24;\n"
"}\n"
"")
        self.widget_4.setObjectName("widget_4")
        self.textStatus = QtWidgets.QTextBrowser(self.widget_4)
        self.textStatus.setGeometry(QtCore.QRect(90, 90, 1101, 771))
        self.textStatus.setObjectName("textStatus")
        self.inpIp = QtWidgets.QLineEdit(self.widget_4)
        self.inpIp.setGeometry(QtCore.QRect(240, 20, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.inpIp.setFont(font)
        self.inpIp.setStyleSheet("color: rgb(255, 255, 255);")
        self.inpIp.setObjectName("inpIp")
        self.gridLayoutWidget = QtWidgets.QWidget(self.widget_4)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(550, 0, 631, 71))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.gridLayout.setHorizontalSpacing(20)
        self.gridLayout.setObjectName("gridLayout")
        self.btnConnect = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnConnect.setCheckable(True)
        self.btnConnect.setAutoExclusive(True)
        self.btnConnect.setObjectName("btnConnect")
        self.gridLayout.addWidget(self.btnConnect, 0, 0, 1, 1)
        self.btnDisconnect = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnDisconnect.setCheckable(True)
        self.btnDisconnect.setAutoExclusive(True)
        self.btnDisconnect.setObjectName("btnDisconnect")
        self.gridLayout.addWidget(self.btnDisconnect, 0, 1, 1, 1)
        self.btnDisconnect.raise_()
        self.btnConnect.raise_()
        self.label_6 = QtWidgets.QLabel(self.widget_4)
        self.label_6.setGeometry(QtCore.QRect(110, 20, 121, 41))
        self.label_6.setObjectName("label_6")
        self.label_6.raise_()
        self.textStatus.raise_()
        self.inpIp.raise_()
        self.gridLayoutWidget.raise_()
        self.stackedWidget.addWidget(self.homePage)
        self.exportPage = QtWidgets.QWidget()
        self.exportPage.setObjectName("exportPage")
        self.table_view = QtWidgets.QTableView(self.exportPage)
        self.table_view.setGeometry(QtCore.QRect(90, 90, 1391, 781))
        self.table_view.setObjectName("table_view")
        self.label_2 = QtWidgets.QLabel(self.exportPage)
        self.label_2.setGeometry(QtCore.QRect(80, 20, 60, 44))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.from_time = QtWidgets.QDateTimeEdit(self.exportPage)
        self.from_time.setGeometry(QtCore.QRect(146, 24, 252, 41))
        self.from_time.setDateTime(QtCore.QDateTime(QtCore.QDate(2024, 1, 1), QtCore.QTime(0, 0, 0)))
        self.from_time.setDate(QtCore.QDate(2024, 1, 1))
        self.from_time.setTime(QtCore.QTime(0, 0, 0))
        self.from_time.setMinimumDate(QtCore.QDate(2024, 1, 1))
        self.from_time.setTimeSpec(QtCore.Qt.LocalTime)
        self.from_time.setObjectName("from_time")
        self.label_3 = QtWidgets.QLabel(self.exportPage)
        self.label_3.setGeometry(QtCore.QRect(480, 22, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.to_time = QtWidgets.QDateTimeEdit(self.exportPage)
        self.to_time.setGeometry(QtCore.QRect(532, 21, 251, 41))
        self.to_time.setDate(QtCore.QDate(2024, 1, 1))
        self.to_time.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2024, 1, 1), QtCore.QTime(0, 0, 0)))
        self.to_time.setObjectName("to_time")
        self.widget_8 = QtWidgets.QWidget(self.exportPage)
        self.widget_8.setGeometry(QtCore.QRect(0, 0, 1601, 911))
        self.widget_8.setStyleSheet("QWidget{\n"
"background-color: #191C24;\n"
"}\n"
"")
        self.widget_8.setObjectName("widget_8")
        self.layoutWidget = QtWidgets.QWidget(self.widget_8)
        self.layoutWidget.setGeometry(QtCore.QRect(830, 0, 651, 80))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_4.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_4.setHorizontalSpacing(20)
        self.gridLayout_4.setVerticalSpacing(0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.show_data_btn = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.show_data_btn.setFont(font)
        self.show_data_btn.setCheckable(True)
        self.show_data_btn.setAutoExclusive(True)
        self.show_data_btn.setObjectName("show_data_btn")
        self.gridLayout_4.addWidget(self.show_data_btn, 0, 2, 1, 1)
        self.export_btn = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.export_btn.setFont(font)
        self.export_btn.setCheckable(True)
        self.export_btn.setAutoExclusive(True)
        self.export_btn.setObjectName("export_btn")
        self.gridLayout_4.addWidget(self.export_btn, 0, 1, 1, 1)
        self.widget_8.raise_()
        self.table_view.raise_()
        self.label_2.raise_()
        self.from_time.raise_()
        self.label_3.raise_()
        self.to_time.raise_()
        self.stackedWidget.addWidget(self.exportPage)
        self.logPage = QtWidgets.QWidget()
        self.logPage.setObjectName("logPage")
        self.widget_9 = QtWidgets.QWidget(self.logPage)
        self.widget_9.setGeometry(QtCore.QRect(0, 0, 1601, 911))
        self.widget_9.setStyleSheet("QWidget{\n"
"background-color: #191C24;\n"
"}\n"
"")
        self.widget_9.setObjectName("widget_9")
        self.layoutWidget1 = QtWidgets.QWidget(self.widget_9)
        self.layoutWidget1.setGeometry(QtCore.QRect(440, 10, 631, 71))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_3.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_3.setHorizontalSpacing(20)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.btnClearLog = QtWidgets.QPushButton(self.layoutWidget1)
        self.btnClearLog.setCheckable(True)
        self.btnClearLog.setAutoExclusive(True)
        self.btnClearLog.setObjectName("btnClearLog")
        self.gridLayout_3.addWidget(self.btnClearLog, 0, 0, 1, 1)
        self.btnBackup = QtWidgets.QPushButton(self.layoutWidget1)
        self.btnBackup.setCheckable(True)
        self.btnBackup.setAutoExclusive(True)
        self.btnBackup.setObjectName("btnBackup")
        self.gridLayout_3.addWidget(self.btnBackup, 0, 1, 1, 1)
        self.logField = QtWidgets.QTextBrowser(self.logPage)
        self.logField.setGeometry(QtCore.QRect(90, 90, 1401, 761))
        self.logField.setObjectName("logField")
        self.stackedWidget.addWidget(self.logPage)
        self.helpPage = QtWidgets.QWidget()
        self.helpPage.setObjectName("helpPage")
        self.widget_6 = QtWidgets.QWidget(self.helpPage)
        self.widget_6.setGeometry(QtCore.QRect(0, 0, 1601, 911))
        self.widget_6.setStyleSheet("QWidget{\n"
"background-color: #191C24;\n"
"}")
        self.widget_6.setObjectName("widget_6")
        self.stackedWidget.addWidget(self.helpPage)
        self.aboutPage = QtWidgets.QWidget()
        self.aboutPage.setObjectName("aboutPage")
        self.widget_7 = QtWidgets.QWidget(self.aboutPage)
        self.widget_7.setGeometry(QtCore.QRect(0, 0, 1601, 911))
        self.widget_7.setStyleSheet("QWidget{\n"
"background-color: #191C24;\n"
"}")
        self.widget_7.setObjectName("widget_7")
        self.label_7 = QtWidgets.QLabel(self.widget_7)
        self.label_7.setGeometry(QtCore.QRect(1290, 813, 171, 51))
        self.label_7.setStyleSheet("font: 8pt \"Poppins\";")
        self.label_7.setObjectName("label_7")
        self.versionSet = QtWidgets.QLabel(self.widget_7)
        self.versionSet.setGeometry(QtCore.QRect(1400, 813, 171, 51))
        self.versionSet.setStyleSheet("font: 8pt \"Poppins\";")
        self.versionSet.setText("")
        self.versionSet.setObjectName("versionSet")
        self.activateLicense = QtWidgets.QPushButton(self.widget_7)
        self.activateLicense.setGeometry(QtCore.QRect(1134, 830, 81, 21))
        self.activateLicense.setObjectName("activateLicense")
        self.licenseEnter = QtWidgets.QLineEdit(self.widget_7)
        self.licenseEnter.setGeometry(QtCore.QRect(720, 832, 409, 20))
        self.licenseEnter.setObjectName("licenseEnter")
        self.licenseLabel = QtWidgets.QLabel(self.widget_7)
        self.licenseLabel.setGeometry(QtCore.QRect(720, 810, 181, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.licenseLabel.setFont(font)
        self.licenseLabel.setObjectName("licenseLabel")
        self.textBrowser = QtWidgets.QTextBrowser(self.widget_7)
        self.textBrowser.setGeometry(QtCore.QRect(90, 40, 1401, 711))
        self.textBrowser.setStyleSheet("font: 9pt \"Poppins\";\n"
"color: rgb(255, 255, 255);")
        self.textBrowser.setObjectName("textBrowser")
        self.stackedWidget.addWidget(self.aboutPage)
        self.importPage = QtWidgets.QWidget()
        self.importPage.setObjectName("importPage")
        self.widget_5 = QtWidgets.QWidget(self.importPage)
        self.widget_5.setGeometry(QtCore.QRect(-140, 0, 1741, 761))
        self.widget_5.setStyleSheet("QWidget{\n"
"background-color: #191C24;\n"
"}\n"
"")
        self.widget_5.setObjectName("widget_5")
        self.layoutWidget2 = QtWidgets.QWidget(self.widget_5)
        self.layoutWidget2.setGeometry(QtCore.QRect(390, 300, 1011, 261))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget2)
        self.gridLayout_2.setContentsMargins(25, 25, 40, 30)
        self.gridLayout_2.setHorizontalSpacing(35)
        self.gridLayout_2.setVerticalSpacing(30)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.btnDownloadExcel = QtWidgets.QPushButton(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btnDownloadExcel.setFont(font)
        self.btnDownloadExcel.setCheckable(True)
        self.btnDownloadExcel.setAutoExclusive(True)
        self.btnDownloadExcel.setObjectName("btnDownloadExcel")
        self.gridLayout_2.addWidget(self.btnDownloadExcel, 1, 1, 1, 1)
        self.btnImpExcel = QtWidgets.QPushButton(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btnImpExcel.setFont(font)
        self.btnImpExcel.setCheckable(True)
        self.btnImpExcel.setAutoExclusive(True)
        self.btnImpExcel.setObjectName("btnImpExcel")
        self.gridLayout_2.addWidget(self.btnImpExcel, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.layoutWidget2)
        self.label.setStyleSheet("font: 12pt \"Poppins\";")
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_5.setStyleSheet("font: 12pt \"Poppins\";")
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 1, 0, 1, 1)
        self.logImp = QtWidgets.QTextBrowser(self.importPage)
        self.logImp.setGeometry(QtCore.QRect(0, 780, 1601, 121))
        self.logImp.setObjectName("logImp")
        self.stackedWidget.addWidget(self.importPage)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1922, 21))
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
        self.label_4.setText(_translate("MainWindow", "PLCInsight Pro"))
        self.navHome.setText(_translate("MainWindow", "  Home"))
        self.navExport.setText(_translate("MainWindow", "  Export"))
        self.navLog.setText(_translate("MainWindow", "  Log"))
        self.navHelp.setText(_translate("MainWindow", "  Help"))
        self.navAbout.setText(_translate("MainWindow", "  About"))
        self.navImp.setText(_translate("MainWindow", "  Settings"))
        self.btnConnect.setText(_translate("MainWindow", "Connect"))
        self.btnDisconnect.setText(_translate("MainWindow", "Disconnect"))
        self.label_6.setText(_translate("MainWindow", "Enter PLC IP  :"))
        self.label_2.setText(_translate("MainWindow", "  From :"))
        self.label_3.setText(_translate("MainWindow", "  To :"))
        self.show_data_btn.setText(_translate("MainWindow", "Show Data"))
        self.export_btn.setText(_translate("MainWindow", "Export Excel"))
        self.btnClearLog.setText(_translate("MainWindow", "Clear"))
        self.btnBackup.setText(_translate("MainWindow", "BackUP"))
        self.label_7.setText(_translate("MainWindow", "Software  Version   : "))
        self.activateLicense.setText(_translate("MainWindow", "Activate"))
        self.licenseLabel.setText(_translate("MainWindow", "Enter License Key:"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Poppins\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">PLCInsight Pro</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">                          Welcome to PLCInsight Pro, your ultimate solution for efficient data handling, analytics, visualization from Programmable Logic Controllers (PLCs).</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Introduction:</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-size:10pt;\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">PLCInsight Pro is a cutting-edge software designed to streamline the process of fetching data from PLCs, empowering you to delve deep into your industrial operations. With its robust analytics engine, PLCInsight Pro provides unparalleled insights into your data, uncovering trends, anomalies, and correlations that drive informed decision-making.</li>\n"
"<li style=\" font-size:10pt;\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Visualizing your data is made easy with PLCInsight Pro\'s intuitive interface, allowing you to explore your data in meaningful ways. Whether you\'re monitoring production metrics, analyzing equipment performance, or optimizing processes, our visualization tools help you grasp the full picture with clarity and precision.</li>\n"
"<li style=\" font-size:10pt;\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Experience the next level of PLC data management with PLCInsight Pro. Revolutionize your operations, maximize efficiency, and unlock the full potential of your industrial processes.</li></ul>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Who Can Benefit?</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-size:10pt;\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Manufacturers</span>: Streamline production processes, minimize downtime, and optimize resource utilization with real-time insights into equipment performance and production metrics.</li>\n"
"<li style=\" font-size:10pt;\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Automation Engineers</span>: Enhance system performance and reliability by monitoring PLC data in real time and proactively addressing issues before they escalate.</li>\n"
"<li style=\" font-size:10pt;\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Plant Managers</span>: Gain visibility into plant operations, track key performance indicators, and make data-driven decisions to improve overall efficiency and productivity.</li>\n"
"<li style=\" font-size:10pt;\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Maintenance Teams</span>: Predict equipment failures, schedule preventive maintenance tasks, and ensure optimal equipment performance to minimize costly downtime</li></ul>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Contact Us  :  </span><span style=\" font-size:10pt;\">info@proliteautomation.com</span></p></body></html>"))
        self.btnDownloadExcel.setText(_translate("MainWindow", "Download reference file"))
        self.btnImpExcel.setText(_translate("MainWindow", "Open"))
        self.label.setText(_translate("MainWindow", "Open the excel file and upload in DB"))
        self.label_5.setText(_translate("MainWindow", "For referencr click the download Btn and make the excel format as it in reference file"))
# import main_resource_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
