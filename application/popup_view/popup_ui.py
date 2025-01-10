# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'popup.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Popup(object):
    def setupUi(self, Popup):
        if not Popup.objectName():
            Popup.setObjectName(u"Popup")
        Popup.resize(500, 100)
        self.centralwidget = QWidget(Popup)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.text = QLabel(self.centralwidget)
        self.text.setObjectName(u"text")
        self.text.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.text)

        self.closeButton = QPushButton(self.centralwidget)
        self.closeButton.setObjectName(u"closeButton")

        self.verticalLayout.addWidget(self.closeButton)

        Popup.setCentralWidget(self.centralwidget)

        self.retranslateUi(Popup)

        QMetaObject.connectSlotsByName(Popup)
    # setupUi

    def retranslateUi(self, Popup):
        Popup.setWindowTitle(QCoreApplication.translate("Popup", u"Gestionix - Popup", None))
        self.text.setText(QCoreApplication.translate("Popup", u"Gestionix - Vous ne pouvez pas faire cela", None))
        self.closeButton.setText(QCoreApplication.translate("Popup", u"Close", None))
    # retranslateUi

