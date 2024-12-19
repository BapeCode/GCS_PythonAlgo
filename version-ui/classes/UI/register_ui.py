# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'register.ui'
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

class Ui_RegisterWindow(object):
    def setupUi(self, Ui_RegisterWindow):
        if not Ui_RegisterWindow.objectName():
            Ui_RegisterWindow.setObjectName(u"Ui_RegisterWindow")
        Ui_RegisterWindow.resize(650, 650)
        Ui_RegisterWindow.setStyleSheet(u"QMainWindow {\n"
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
"#title{\n"
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
        self.centralwidget = QWidget(Ui_RegisterWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer_2 = QSpacerItem(20, 75, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(75, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(450, 450))
        font = QFont()
        self.widget.setFont(font)
        self.widget.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.title = QLabel(self.widget)
        self.title.setObjectName(u"title")
        font1 = QFont()
        font1.setPointSize(40)
        self.title.setFont(font1)
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_7.addWidget(self.title)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_8 = QLabel(self.widget)
        self.label_8.setObjectName(u"label_8")
        font2 = QFont()
        font2.setPointSize(13)
        self.label_8.setFont(font2)

        self.verticalLayout_8.addWidget(self.label_8)

        self.emailButton = QLineEdit(self.widget)
        self.emailButton.setObjectName(u"emailButton")
        self.emailButton.setMinimumSize(QSize(200, 0))

        self.verticalLayout_8.addWidget(self.emailButton)


        self.verticalLayout_7.addLayout(self.verticalLayout_8)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_9 = QLabel(self.widget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font2)

        self.verticalLayout_9.addWidget(self.label_9)

        self.usernameButton = QLineEdit(self.widget)
        self.usernameButton.setObjectName(u"usernameButton")
        self.usernameButton.setEchoMode(QLineEdit.EchoMode.Normal)
        self.usernameButton.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_9.addWidget(self.usernameButton)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_10 = QLabel(self.widget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font2)

        self.verticalLayout_10.addWidget(self.label_10)

        self.passwordButton = QLineEdit(self.widget)
        self.passwordButton.setObjectName(u"passwordButton")
        self.passwordButton.setEchoMode(QLineEdit.EchoMode.Password)
        self.passwordButton.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_10.addWidget(self.passwordButton)


        self.verticalLayout_9.addLayout(self.verticalLayout_10)


        self.verticalLayout_7.addLayout(self.verticalLayout_9)

        self.succes = QLabel(self.widget)
        self.succes.setObjectName(u"succes")
        font3 = QFont()
        font3.setPointSize(10)
        self.succes.setFont(font3)

        self.verticalLayout_7.addWidget(self.succes)

        self.pushButton_3 = QPushButton(self.widget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_7.addWidget(self.pushButton_3)


        self.gridLayout_2.addLayout(self.verticalLayout_7, 1, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(7, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 1, 0, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(7, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_4, 1, 2, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 33, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_4, 2, 1, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 31, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_3, 0, 1, 1, 1)


        self.gridLayout.addWidget(self.widget, 1, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(75, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 75, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 2, 1, 1, 1)

        Ui_RegisterWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(Ui_RegisterWindow)

        QMetaObject.connectSlotsByName(Ui_RegisterWindow)
    # setupUi

    def retranslateUi(self, Ui_RegisterWindow):
        Ui_RegisterWindow.setWindowTitle(QCoreApplication.translate("Ui_RegisterWindow", u"Register", None))
        self.title.setText(QCoreApplication.translate("Ui_RegisterWindow", u"Register", None))
        self.label_8.setText(QCoreApplication.translate("Ui_RegisterWindow", u"Email", None))
        self.emailButton.setPlaceholderText(QCoreApplication.translate("Ui_RegisterWindow", u"email@example.com", None))
        self.label_9.setText(QCoreApplication.translate("Ui_RegisterWindow", u"Username", None))
        self.usernameButton.setText("")
        self.usernameButton.setPlaceholderText(QCoreApplication.translate("Ui_RegisterWindow", u"Your username", None))
        self.label_10.setText(QCoreApplication.translate("Ui_RegisterWindow", u"Password", None))
        self.passwordButton.setPlaceholderText(QCoreApplication.translate("Ui_RegisterWindow", u"Your password", None))
        self.succes.setText(QCoreApplication.translate("Ui_RegisterWindow", u"Identifier alwready exist", None))
        self.pushButton_3.setText(QCoreApplication.translate("Ui_RegisterWindow", u"Register", None))
    # retranslateUi

