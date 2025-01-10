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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        if not LoginWindow.objectName():
            LoginWindow.setObjectName(u"LoginWindow")
        LoginWindow.resize(1000, 600)
        LoginWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(LoginWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(400, 400))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer_2 = QSpacerItem(20, 89, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(110, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        font = QFont()
        font.setPointSize(50)
        self.label_4.setFont(font)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_4, 1, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(110, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        font1 = QFont()
        font1.setPointSize(13)
        self.label_5.setFont(font1)

        self.verticalLayout_5.addWidget(self.label_5)

        self.usernameLine = QLineEdit(self.widget)
        self.usernameLine.setObjectName(u"usernameLine")
        self.usernameLine.setMinimumSize(QSize(200, 0))
        font2 = QFont()
        self.usernameLine.setFont(font2)

        self.verticalLayout_5.addWidget(self.usernameLine)


        self.gridLayout.addLayout(self.verticalLayout_5, 2, 1, 1, 1)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)

        self.verticalLayout_6.addWidget(self.label_6)

        self.passwordLine = QLineEdit(self.widget)
        self.passwordLine.setObjectName(u"passwordLine")
        self.passwordLine.setFont(font2)
        self.passwordLine.setEchoMode(QLineEdit.EchoMode.Password)
        self.passwordLine.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_6.addWidget(self.passwordLine)


        self.gridLayout.addLayout(self.verticalLayout_6, 3, 1, 1, 1)

        self.message = QLabel(self.widget)
        self.message.setObjectName(u"message")
        font3 = QFont()
        font3.setPointSize(10)
        self.message.setFont(font3)

        self.gridLayout.addWidget(self.message, 4, 1, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.loginButton = QPushButton(self.widget)
        self.loginButton.setObjectName(u"loginButton")

        self.horizontalLayout.addWidget(self.loginButton)

        self.cancelButton = QPushButton(self.widget)
        self.cancelButton.setObjectName(u"cancelButton")

        self.horizontalLayout.addWidget(self.cancelButton)


        self.gridLayout.addLayout(self.horizontalLayout, 5, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 90, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 6, 1, 1, 1)


        self.gridLayout_2.addWidget(self.widget, 0, 0, 1, 1)

        LoginWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(LoginWindow)

        QMetaObject.connectSlotsByName(LoginWindow)
    # setupUi

    def retranslateUi(self, LoginWindow):
        LoginWindow.setWindowTitle(QCoreApplication.translate("LoginWindow", u"Gestionix - Login", None))
        self.label_4.setText(QCoreApplication.translate("LoginWindow", u"Login", None))
        self.label_5.setText(QCoreApplication.translate("LoginWindow", u"Username", None))
        self.usernameLine.setPlaceholderText(QCoreApplication.translate("LoginWindow", u"Your username", None))
        self.label_6.setText(QCoreApplication.translate("LoginWindow", u"Password", None))
        self.passwordLine.setPlaceholderText(QCoreApplication.translate("LoginWindow", u"Your password", None))
        self.message.setText(QCoreApplication.translate("LoginWindow", u"", None))
        self.loginButton.setText(QCoreApplication.translate("LoginWindow", u"Login", None))
        self.cancelButton.setText(QCoreApplication.translate("LoginWindow", u"Cancel", None))
    # retranslateUi

