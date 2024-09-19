# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'menu.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(377, 381)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(70, 60, 234, 281))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"MS PGothic"])
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setCursor(QCursor(Qt.CursorShape.OpenHandCursor))
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.Btn_Perimetros = QPushButton(self.layoutWidget)
        self.Btn_Perimetros.setObjectName(u"Btn_Perimetros")
        font1 = QFont()
        font1.setFamilies([u"MS PGothic"])
        font1.setPointSize(11)
        self.Btn_Perimetros.setFont(font1)
        self.Btn_Perimetros.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout.addWidget(self.Btn_Perimetros)

        self.Btn_Areas = QPushButton(self.layoutWidget)
        self.Btn_Areas.setObjectName(u"Btn_Areas")
        self.Btn_Areas.setFont(font1)
        self.Btn_Areas.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout.addWidget(self.Btn_Areas)

        self.Btn_Volumenes = QPushButton(self.layoutWidget)
        self.Btn_Volumenes.setObjectName(u"Btn_Volumenes")
        self.Btn_Volumenes.setFont(font1)
        self.Btn_Volumenes.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout.addWidget(self.Btn_Volumenes)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Figuras Geometricas", None))
        self.Btn_Perimetros.setText(QCoreApplication.translate("MainWindow", u"Perimetros ", None))
        self.Btn_Areas.setText(QCoreApplication.translate("MainWindow", u"Areas", None))
        self.Btn_Volumenes.setText(QCoreApplication.translate("MainWindow", u"Volumenes", None))
    # retranslateUi

