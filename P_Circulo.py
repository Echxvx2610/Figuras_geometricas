# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'P_Circulo.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)
import resources_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(496, 423)
        Dialog.setStyleSheet(u"")
        self.Lbl_Formula = QLabel(Dialog)
        self.Lbl_Formula.setObjectName(u"Lbl_Formula")
        self.Lbl_Formula.setGeometry(QRect(20, 270, 331, 41))
        font = QFont()
        font.setFamilies([u"MS PGothic"])
        font.setPointSize(16)
        self.Lbl_Formula.setFont(font)
        self.Lbl_Resultado = QLabel(Dialog)
        self.Lbl_Resultado.setObjectName(u"Lbl_Resultado")
        self.Lbl_Resultado.setGeometry(QRect(20, 310, 281, 31))
        self.Lbl_Resultado.setFont(font)
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(50, 30, 401, 221))
        self.label_3.setStyleSheet(u"image: url(:/perimetros/perimetro_circulo.png);")
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(270, 130, 21, 16))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.label_4.setFont(font1)
        self.Txb_r = QLineEdit(Dialog)
        self.Txb_r.setObjectName(u"Txb_r")
        self.Txb_r.setGeometry(QRect(280, 130, 51, 22))
        font2 = QFont()
        font2.setFamilies([u"MS PGothic"])
        font2.setPointSize(11)
        self.Txb_r.setFont(font2)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(90, 10, 281, 21))
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        self.layoutWidget = QWidget(Dialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(170, 370, 295, 30))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.Btn_Regresar = QPushButton(self.layoutWidget)
        self.Btn_Regresar.setObjectName(u"Btn_Regresar")
        self.Btn_Regresar.setFont(font2)

        self.horizontalLayout.addWidget(self.Btn_Regresar)

        self.Btn_Calcular = QPushButton(self.layoutWidget)
        self.Btn_Calcular.setObjectName(u"Btn_Calcular")
        self.Btn_Calcular.setFont(font2)

        self.horizontalLayout.addWidget(self.Btn_Calcular)

        self.Btn_Salir = QPushButton(self.layoutWidget)
        self.Btn_Salir.setObjectName(u"Btn_Salir")
        self.Btn_Salir.setFont(font2)

        self.horizontalLayout.addWidget(self.Btn_Salir)

        self.layoutWidget.raise_()
        self.label_3.raise_()
        self.Lbl_Formula.raise_()
        self.Lbl_Resultado.raise_()
        self.label_4.raise_()
        self.Txb_r.raise_()
        self.label.raise_()

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.Lbl_Formula.setText(QCoreApplication.translate("Dialog", u"Formula:  2\u03c0 * r", None))
        self.Lbl_Resultado.setText(QCoreApplication.translate("Dialog", u"Resultado:", None))
        self.label_3.setText("")
        self.label_4.setText(QCoreApplication.translate("Dialog", u"r", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Perimetro Circulo", None))
        self.Btn_Regresar.setText(QCoreApplication.translate("Dialog", u"Regresar", None))
        self.Btn_Calcular.setText(QCoreApplication.translate("Dialog", u"Calcular", None))
        self.Btn_Salir.setText(QCoreApplication.translate("Dialog", u"Salir", None))
    # retranslateUi

