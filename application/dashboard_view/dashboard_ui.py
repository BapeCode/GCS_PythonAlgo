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
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_Dashboard(object):
    def setupUi(self, Dashboard):
        if not Dashboard.objectName():
            Dashboard.setObjectName(u"Dashboard")
        Dashboard.resize(1300, 600)
        Dashboard.setStyleSheet(u"QFrame {\n"
"	border: none;\n"
"}\n"
"\n"
"QLineEdit {\n"
"	padding: 5px;\n"
"}")
        self.actionuserAccounts = QAction(Dashboard)
        self.actionuserAccounts.setObjectName(u"actionuserAccounts")
        self.actionuserAccounts.setMenuRole(QAction.MenuRole.NoRole)
        self.actionExport_PDF = QAction(Dashboard)
        self.actionExport_PDF.setObjectName(u"actionExport_PDF")
        self.actionExport_CSV = QAction(Dashboard)
        self.actionExport_CSV.setObjectName(u"actionExport_CSV")
        self.actionLogout = QAction(Dashboard)
        self.actionLogout.setObjectName(u"actionLogout")
        self.actionExit = QAction(Dashboard)
        self.actionExit.setObjectName(u"actionExit")
        self.centralwidget = QWidget(Dashboard)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.home = QFrame(self.centralwidget)
        self.home.setObjectName(u"home")
        self.home.setFrameShape(QFrame.Shape.StyledPanel)
        self.home.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.home)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_2 = QLabel(self.home)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_3.addWidget(self.label_2)

        self.tableWidget = QTableWidget(self.home)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout_3.addWidget(self.tableWidget)


        self.horizontalLayout.addWidget(self.home)

        self.container = QFrame(self.centralwidget)
        self.container.setObjectName(u"container")
        self.container.setFrameShape(QFrame.Shape.StyledPanel)
        self.container.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.container)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(self.container)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(50)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label)


        self.verticalLayout_2.addWidget(self.frame)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.addButtons = QPushButton(self.container)
        self.addButtons.setObjectName(u"addButtons")

        self.horizontalLayout_2.addWidget(self.addButtons)

        self.viewOrder = QPushButton(self.container)
        self.viewOrder.setObjectName(u"viewOrder")

        self.horizontalLayout_2.addWidget(self.viewOrder)

        self.sortCombo = QComboBox(self.container)
        self.sortCombo.addItem("")
        self.sortCombo.addItem("")
        self.sortCombo.addItem("")
        self.sortCombo.addItem("")
        self.sortCombo.addItem("")
        self.sortCombo.setObjectName(u"sortCombo")

        self.horizontalLayout_2.addWidget(self.sortCombo)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.searchLine = QLineEdit(self.container)
        self.searchLine.setObjectName(u"searchLine")

        self.verticalLayout_2.addWidget(self.searchLine)

        self.label_3 = QLabel(self.container)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_2.addWidget(self.label_3)

        self.tableWidget_2 = QTableWidget(self.container)
        if (self.tableWidget_2.columnCount() < 6):
            self.tableWidget_2.setColumnCount(6)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, __qtablewidgetitem10)
        self.tableWidget_2.setObjectName(u"tableWidget_2")

        self.verticalLayout_2.addWidget(self.tableWidget_2)


        self.horizontalLayout.addWidget(self.container)

        Dashboard.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Dashboard)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1200, 24))
        self.menubar.setNativeMenuBar(False)
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        Dashboard.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionExport_PDF)
        self.menuFile.addAction(self.actionExport_CSV)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionLogout)
        self.menuFile.addAction(self.actionExit)

        self.retranslateUi(Dashboard)

        QMetaObject.connectSlotsByName(Dashboard)
    # setupUi

    def retranslateUi(self, Dashboard):
        Dashboard.setWindowTitle(QCoreApplication.translate("Dashboard", u"Gestionix - Dashboard", None))
        self.actionuserAccounts.setText(QCoreApplication.translate("Dashboard", u"userAccounts", None))
        self.actionExport_PDF.setText(QCoreApplication.translate("Dashboard", u"Export PDF", None))
        self.actionExport_CSV.setText(QCoreApplication.translate("Dashboard", u"Export CSV", None))
        self.actionLogout.setText(QCoreApplication.translate("Dashboard", u"Logout", None))
        self.actionExit.setText(QCoreApplication.translate("Dashboard", u"Exit", None))
        self.label_2.setText(QCoreApplication.translate("Dashboard", u"Products List", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dashboard", u"Product Name", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dashboard", u"Product Price", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Dashboard", u"Product Stock", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Dashboard", u"Stock price ($)", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Dashboard", u"Options", None));
        self.label.setText(QCoreApplication.translate("Dashboard", u"Gestionix", None))
        self.addButtons.setText(QCoreApplication.translate("Dashboard", u"New products", None))
        self.viewOrder.setText(QCoreApplication.translate("Dashboard", u"View order", None))
        self.sortCombo.setItemText(0, QCoreApplication.translate("Dashboard", u"Sort stock", None))
        self.sortCombo.setItemText(1, QCoreApplication.translate("Dashboard", u"Price", None))
        self.sortCombo.setItemText(2, QCoreApplication.translate("Dashboard", u"Name", None))
        self.sortCombo.setItemText(3, QCoreApplication.translate("Dashboard", u"Stock", None))
        self.sortCombo.setItemText(4, QCoreApplication.translate("Dashboard", u"Date", None))

        self.searchLine.setPlaceholderText(QCoreApplication.translate("Dashboard", u"Search products", None))
        self.label_3.setText(QCoreApplication.translate("Dashboard", u"Order list", None))
        ___qtablewidgetitem5 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Dashboard", u"Customer", None));
        ___qtablewidgetitem6 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Dashboard", u"Product", None));
        ___qtablewidgetitem7 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Dashboard", u"Total Price", None));
        ___qtablewidgetitem8 = self.tableWidget_2.horizontalHeaderItem(3)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Dashboard", u"Quantity", None));
        ___qtablewidgetitem9 = self.tableWidget_2.horizontalHeaderItem(4)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Dashboard", u"Date", None));
        ___qtablewidgetitem10 = self.tableWidget_2.horizontalHeaderItem(5)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Dashboard", u"Status", None));
        self.menuFile.setTitle(QCoreApplication.translate("Dashboard", u"File", None))
    # retranslateUi

