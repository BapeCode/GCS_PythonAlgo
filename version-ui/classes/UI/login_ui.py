# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_LoginWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(650, 650)
        MainWindow.setStyleSheet(u"QMainWindow {\n"
"	background-color: #ffffff\n"
"}\n"
"\n"
"QWidget #widget {\n"
"	border-radius: 10px;\n"
"	border: 1px solid #ccc;\n"
"	background-color: #ededed\n"
"}\n"
"\n"
"QLabel {\n"
"	color: black\n"
"}\n"
"\n"
"#label_4{\n"
"	color: #400b97\n"
"}\n"
"\n"
"QPushButton {\n"
"	padding: 10px;\n"
"	border-radius: 10px;\n"
"	background-color: #400b97\n"
"}\n"
"\n"
"QPushButton:hover,\n"
"QPushButton:clicked {\n"
"	background-color: #400baa\n"
"}\n"
"\n"
"QLineEdit {\n"
"	background-color: #400b97;\n"
"	padding: 5px;\n"
"	border: none;\n"
"	border-bottom: 1px solid black;\n"
"	border-radius: 6px;\n"
"	color: white;\n"
"	font-size: 12px\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalSpacer_4 = QSpacerItem(20, 75, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_4, 2, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(75, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 1, 0, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(75, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_4, 1, 2, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 75, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_3, 0, 1, 1, 1)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(450, 450))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(-1)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_2 = QSpacerItem(20, 88, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(110, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        font = QFont()
        font.setPointSize(40)
        self.label_4.setFont(font)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        font1 = QFont()
        font1.setPointSize(13)
        self.label_5.setFont(font1)

        self.verticalLayout_5.addWidget(self.label_5)

        self.lineEdit_3 = QLineEdit(self.widget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMinimumSize(QSize(200, 0))
        font2 = QFont()
        self.lineEdit_3.setFont(font2)

        self.verticalLayout_5.addWidget(self.lineEdit_3)


        self.verticalLayout_4.addLayout(self.verticalLayout_5)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)

        self.verticalLayout_6.addWidget(self.label_6)

        self.lineEdit_4 = QLineEdit(self.widget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setFont(font2)
        self.lineEdit_4.setEchoMode(QLineEdit.EchoMode.Password)
        self.lineEdit_4.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_6.addWidget(self.lineEdit_4)


        self.verticalLayout_4.addLayout(self.verticalLayout_6)

        self.message = QLabel(self.widget)
        self.message.setObjectName(u"message")
        font3 = QFont()
        font3.setPointSize(10)
        self.message.setFont(font3)

        self.verticalLayout_4.addWidget(self.message)

        self.pushButton_2 = QPushButton(self.widget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.pushButton_2)


        self.gridLayout.addLayout(self.verticalLayout_4, 1, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(110, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 88, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 2, 1, 1, 1)


        self.gridLayout_2.addWidget(self.widget, 1, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Gestionix - Login", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"email@example.com", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Your password", None))
        self.message.setText(QCoreApplication.translate("MainWindow", u"Identifier or password not correct", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Login", None))
    # retranslateUi

