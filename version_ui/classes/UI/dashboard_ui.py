# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dashboard.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGroupBox,
    QHBoxLayout, QLabel, QMainWindow, QPushButton,
    QScrollArea, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Dashboard(object):
    def setupUi(self, Dashboard):
        if not Dashboard.objectName():
            Dashboard.setObjectName(u"Dashboard")
        Dashboard.resize(900, 600)
        Dashboard.setMinimumSize(QSize(0, 5))
        Dashboard.setStyleSheet(u"QMainWindow {\n"
"	background-image: url(static/background_principal.png);\n"
"}\n"
"\n"
"QLabel {\n"
"	color: black\n"
"}\n"
"\n"
"QGroupBox {\n"
"	color: black;\n"
"	background-color: rgba(245, 245, 245, 0.8);\n"
"	border-radius: 5px;\n"
"	padding: 10px\n"
"}\n"
"\n"
"QScrollArea {\n"
"	background-color: rgba(245, 245, 245, 0.8);\n"
"}\n"
"\n"
"#scrollAreaWidgetContents {\n"
"	background-color: rgba(245, 245, 245, 0.8);\n"
"}\n"
"\n"
"#title {\n"
"	color: #400b97\n"
"}\n"
"\n"
"QPushButton {\n"
"	background-color: #400b97;\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 10px\n"
"}\n"
"\n"
"QPushButton:hover,\n"
"QPushButton:clicked {\n"
"	background-color: #400baa;\n"
"}\n"
"\n"
"QScrollArea {\n"
"	border-radius: 12px;\n"
"}\n"
"\n"
"QCombotBox {\n"
"	color: black;\n"
"	background-color: #400baa\n"
"}")
        self.centralwidget = QWidget(Dashboard)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_5 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setSpacing(30)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.dashboard = QGroupBox(self.widget)
        self.dashboard.setObjectName(u"dashboard")
        self.dashboard.setMinimumSize(QSize(200, 50))
        self.dashboard.setMaximumSize(QSize(16777215, 80))
        self.horizontalLayout = QHBoxLayout(self.dashboard)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 25, -1, -1)
        self.settingsButton = QPushButton(self.dashboard)
        self.settingsButton.setObjectName(u"settingsButton")
        self.settingsButton.setMinimumSize(QSize(100, 25))
        self.settingsButton.setMaximumSize(QSize(150, 50))
        self.settingsButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout.addWidget(self.settingsButton)

        self.title = QLabel(self.dashboard)
        self.title.setObjectName(u"title")
        font = QFont()
        font.setPointSize(18)
        self.title.setFont(font)
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.title)

        self.logoutButton = QPushButton(self.dashboard)
        self.logoutButton.setObjectName(u"logoutButton")
        self.logoutButton.setMinimumSize(QSize(100, 25))
        self.logoutButton.setMaximumSize(QSize(150, 50))
        self.logoutButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout.addWidget(self.logoutButton)


        self.verticalLayout.addWidget(self.dashboard)

        self.action = QGroupBox(self.widget)
        self.action.setObjectName(u"action")
        self.action.setMinimumSize(QSize(600, 80))
        self.action.setMouseTracking(False)
        self.verticalLayout_3 = QVBoxLayout(self.action)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.button = QWidget(self.action)
        self.button.setObjectName(u"button")
        self.button.setMaximumSize(QSize(16777215, 80))
        self.horizontalLayout_2 = QHBoxLayout(self.button)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.addButton = QPushButton(self.button)
        self.addButton.setObjectName(u"addButton")
        self.addButton.setMinimumSize(QSize(0, 30))
        self.addButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.addButton)

        self.sortButton = QPushButton(self.button)
        self.sortButton.setObjectName(u"sortButton")
        self.sortButton.setMinimumSize(QSize(0, 30))
        self.sortButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.sortButton)

        self.searchButton = QPushButton(self.button)
        self.searchButton.setObjectName(u"searchButton")
        self.searchButton.setMinimumSize(QSize(0, 30))
        self.searchButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.searchButton)


        self.verticalLayout_3.addWidget(self.button)

        self.content = QWidget(self.action)
        self.content.setObjectName(u"content")
        self.content.setMinimumSize(QSize(0, 0))
        self.content.setMaximumSize(QSize(16777215, 275))
        self.verticalLayout_4 = QVBoxLayout(self.content)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.infosContainer = QHBoxLayout()
        self.infosContainer.setObjectName(u"infosContainer")
        self.nameLabel = QLabel(self.content)
        self.nameLabel.setObjectName(u"nameLabel")

        self.infosContainer.addWidget(self.nameLabel)

        self.priceLabel = QLabel(self.content)
        self.priceLabel.setObjectName(u"priceLabel")
        self.priceLabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.infosContainer.addWidget(self.priceLabel)

        self.stockLabel = QLabel(self.content)
        self.stockLabel.setObjectName(u"stockLabel")
        self.stockLabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.infosContainer.addWidget(self.stockLabel)

        self.dateLabel = QLabel(self.content)
        self.dateLabel.setObjectName(u"dateLabel")
        self.dateLabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.infosContainer.addWidget(self.dateLabel)

        self.actionLabel = QLabel(self.content)
        self.actionLabel.setObjectName(u"actionLabel")

        self.infosContainer.addWidget(self.actionLabel)


        self.verticalLayout_4.addLayout(self.infosContainer)

        self.line = QFrame(self.content)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_4.addWidget(self.line)

        self.scrollArea = QScrollArea(self.content)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(Qt.AlignmentFlag.AlignJustify|Qt.AlignmentFlag.AlignTop)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 784, 208))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 3, 5, 3)
        self.containerItems = QWidget(self.scrollAreaWidgetContents)
        self.containerItems.setObjectName(u"containerItems")
        self.containerItems.setMinimumSize(QSize(0, 50))
        self.containerItems.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_3 = QHBoxLayout(self.containerItems)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(5, 3, 5, 3)
        self.label_4 = QLabel(self.containerItems)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_3.addWidget(self.label_4)

        self.label = QLabel(self.containerItems)
        self.label.setObjectName(u"label")

        self.horizontalLayout_3.addWidget(self.label)

        self.label_5 = QLabel(self.containerItems)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_3.addWidget(self.label_5)

        self.label_6 = QLabel(self.containerItems)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_3.addWidget(self.label_6)

        self.comboBox = QComboBox(self.containerItems)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout_3.addWidget(self.comboBox)


        self.verticalLayout_2.addWidget(self.containerItems)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_4.addWidget(self.scrollArea)


        self.verticalLayout_3.addWidget(self.content)


        self.verticalLayout.addWidget(self.action)


        self.verticalLayout_5.addWidget(self.widget)

        Dashboard.setCentralWidget(self.centralwidget)

        self.retranslateUi(Dashboard)

        QMetaObject.connectSlotsByName(Dashboard)
    # setupUi

    def retranslateUi(self, Dashboard):
        Dashboard.setWindowTitle(QCoreApplication.translate("Dashboard", u"Gestionix - DashBoard", None))
        self.dashboard.setTitle(QCoreApplication.translate("Dashboard", u"Gestionix - Dashboard", None))
        self.settingsButton.setText(QCoreApplication.translate("Dashboard", u"Settings", None))
        self.title.setText(QCoreApplication.translate("Dashboard", u"GESTIONIX : Connected as **username**", None))
        self.logoutButton.setText(QCoreApplication.translate("Dashboard", u"Logout", None))
        self.action.setTitle(QCoreApplication.translate("Dashboard", u"Action", None))
        self.addButton.setText(QCoreApplication.translate("Dashboard", u"Add Products", None))
        self.sortButton.setText(QCoreApplication.translate("Dashboard", u"Sort Products", None))
        self.searchButton.setText(QCoreApplication.translate("Dashboard", u"Search Products", None))
        self.nameLabel.setText(QCoreApplication.translate("Dashboard", u"Name", None))
        self.priceLabel.setText(QCoreApplication.translate("Dashboard", u"Price", None))
        self.stockLabel.setText(QCoreApplication.translate("Dashboard", u"Stock", None))
        self.dateLabel.setText(QCoreApplication.translate("Dashboard", u"Date", None))
        self.actionLabel.setText(QCoreApplication.translate("Dashboard", u"Action", None))
        self.label_4.setText(QCoreApplication.translate("Dashboard", u"Bread", None))
        self.label.setText(QCoreApplication.translate("Dashboard", u"2,3\u20ac", None))
        self.label_5.setText(QCoreApplication.translate("Dashboard", u"x20", None))
        self.label_6.setText(QCoreApplication.translate("Dashboard", u"03/12/2000 - 09:20", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Dashboard", u"Supprimer", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Dashboard", u"Modifier", None))

    # retranslateUi

