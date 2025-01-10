# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'addProducts.ui'
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
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpinBox, QVBoxLayout, QWidget)

class Ui_AddProducts(object):
    def setupUi(self, AddProducts):
        if not AddProducts.objectName():
            AddProducts.setObjectName(u"AddProducts")
        AddProducts.resize(654, 266)
        AddProducts.setMinimumSize(QSize(0, 0))
        AddProducts.setMaximumSize(QSize(16777215, 16777215))
        AddProducts.setStyleSheet(u"")
        self.centralwidget = QWidget(AddProducts)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.productLine = QLineEdit(self.centralwidget)
        self.productLine.setObjectName(u"productLine")

        self.verticalLayout.addWidget(self.productLine)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.priceBox = QDoubleSpinBox(self.centralwidget)
        self.priceBox.setObjectName(u"priceBox")
        self.priceBox.setMaximum(999999999999999.000000000000000)

        self.verticalLayout.addWidget(self.priceBox)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout.addWidget(self.label_5)

        self.stockBox = QSpinBox(self.centralwidget)
        self.stockBox.setObjectName(u"stockBox")
        self.stockBox.setMaximum(999999999)

        self.verticalLayout.addWidget(self.stockBox)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.saveButton = QPushButton(self.centralwidget)
        self.saveButton.setObjectName(u"saveButton")

        self.horizontalLayout_2.addWidget(self.saveButton)

        self.cancelButton = QPushButton(self.centralwidget)
        self.cancelButton.setObjectName(u"cancelButton")

        self.horizontalLayout_2.addWidget(self.cancelButton)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        AddProducts.setCentralWidget(self.centralwidget)

        self.retranslateUi(AddProducts)

        QMetaObject.connectSlotsByName(AddProducts)
    # setupUi

    def retranslateUi(self, AddProducts):
        AddProducts.setWindowTitle(QCoreApplication.translate("AddProducts", u"Gestionix - AddProducts", None))
        self.label.setText(QCoreApplication.translate("AddProducts", u"Product Name", None))
        self.label_2.setText(QCoreApplication.translate("AddProducts", u"Unity price", None))
        self.priceBox.setPrefix(QCoreApplication.translate("AddProducts", u"", None))
        self.priceBox.setSuffix("")
        self.label_5.setText(QCoreApplication.translate("AddProducts", u"Current Stock", None))
        self.saveButton.setText(QCoreApplication.translate("AddProducts", u"Save", None))
        self.cancelButton.setText(QCoreApplication.translate("AddProducts", u"Cancel", None))
    # retranslateUi

