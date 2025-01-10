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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_RegisterWindow(object):
    def setupUi(self, RegisterWindow):
        if not RegisterWindow.objectName():
            RegisterWindow.setObjectName(u"RegisterWindow")
        RegisterWindow.resize(1000, 600)
        RegisterWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(RegisterWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(450, 450))
        font = QFont()
        self.widget.setFont(font)
        self.widget.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalSpacer_3 = QSpacerItem(20, 31, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_3, 0, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(7, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 1, 0, 1, 1)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.title = QLabel(self.widget)
        self.title.setObjectName(u"title")
        font1 = QFont()
        font1.setPointSize(50)
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

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.registerButton = QPushButton(self.widget)
        self.registerButton.setObjectName(u"registerButton")

        self.horizontalLayout.addWidget(self.registerButton)

        self.cancelButton = QPushButton(self.widget)
        self.cancelButton.setObjectName(u"cancelButton")

        self.horizontalLayout.addWidget(self.cancelButton)


        self.verticalLayout_7.addLayout(self.horizontalLayout)


        self.gridLayout_2.addLayout(self.verticalLayout_7, 1, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(7, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_4, 1, 2, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 33, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_4, 2, 1, 1, 1)


        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

        RegisterWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(RegisterWindow)

        QMetaObject.connectSlotsByName(RegisterWindow)
    # setupUi

    def retranslateUi(self, RegisterWindow):
        RegisterWindow.setWindowTitle(QCoreApplication.translate("RegisterWindow", u"Gestionix - Register", None))
        self.title.setText(QCoreApplication.translate("RegisterWindow", u"Register", None))
        self.label_8.setText(QCoreApplication.translate("RegisterWindow", u"Email", None))
        self.emailButton.setPlaceholderText(QCoreApplication.translate("RegisterWindow", u"email@example.com", None))
        self.label_9.setText(QCoreApplication.translate("RegisterWindow", u"Username", None))
        self.usernameButton.setText("")
        self.usernameButton.setPlaceholderText(QCoreApplication.translate("RegisterWindow", u"Your username", None))
        self.label_10.setText(QCoreApplication.translate("RegisterWindow", u"Password", None))
        self.passwordButton.setPlaceholderText(QCoreApplication.translate("RegisterWindow", u"Your password", None))
        self.succes.setText(QCoreApplication.translate("RegisterWindow", u"Identifier alwready exist", None))
        self.registerButton.setText(QCoreApplication.translate("RegisterWindow", u"Register", None))
        self.cancelButton.setText(QCoreApplication.translate("RegisterWindow", u"Cancel", None))
    # retranslateUi

