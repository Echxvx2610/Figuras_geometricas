# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'menu_areas.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(333, 374)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(60, 30, 203, 251))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.Btn_A_Circulo = QPushButton(self.layoutWidget)
        self.Btn_A_Circulo.setObjectName(u"Btn_A_Circulo")
        font1 = QFont()
        font1.setFamilies([u"MS PGothic"])
        font1.setPointSize(11)
        self.Btn_A_Circulo.setFont(font1)

        self.verticalLayout.addWidget(self.Btn_A_Circulo)

        self.Btn_A_Rombo = QPushButton(self.layoutWidget)
        self.Btn_A_Rombo.setObjectName(u"Btn_A_Rombo")
        self.Btn_A_Rombo.setFont(font1)

        self.verticalLayout.addWidget(self.Btn_A_Rombo)

        self.Btn_A_Cometa = QPushButton(self.layoutWidget)
        self.Btn_A_Cometa.setObjectName(u"Btn_A_Cometa")
        self.Btn_A_Cometa.setFont(font1)

        self.verticalLayout.addWidget(self.Btn_A_Cometa)

        self.layoutWidget1 = QWidget(self.centralwidget)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 310, 294, 30))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setSpacing(100)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.Btn_Regresar = QPushButton(self.layoutWidget1)
        self.Btn_Regresar.setObjectName(u"Btn_Regresar")
        self.Btn_Regresar.setFont(font1)

        self.horizontalLayout.addWidget(self.Btn_Regresar)

        self.Btn_Salir = QPushButton(self.layoutWidget1)
        self.Btn_Salir.setObjectName(u"Btn_Salir")
        self.Btn_Salir.setFont(font1)

        self.horizontalLayout.addWidget(self.Btn_Salir)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Menu Areas", None))
        self.Btn_A_Circulo.setText(QCoreApplication.translate("MainWindow", u"Circulo", None))
        self.Btn_A_Rombo.setText(QCoreApplication.translate("MainWindow", u"Rombo", None))
        self.Btn_A_Cometa.setText(QCoreApplication.translate("MainWindow", u"Cometa", None))
        self.Btn_Regresar.setText(QCoreApplication.translate("MainWindow", u"Regresar", None))
        self.Btn_Salir.setText(QCoreApplication.translate("MainWindow", u"Salir", None))
    # retranslateUi

