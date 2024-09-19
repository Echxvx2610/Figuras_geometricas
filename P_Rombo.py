# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'P_Rombo.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)
import resources_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(517, 417)
        self.Lbl_Formula = QLabel(Dialog)
        self.Lbl_Formula.setObjectName(u"Lbl_Formula")
        self.Lbl_Formula.setGeometry(QRect(30, 270, 331, 41))
        font = QFont()
        font.setFamilies([u"MS PGothic"])
        font.setPointSize(16)
        self.Lbl_Formula.setFont(font)
        self.Txb_L = QLineEdit(Dialog)
        self.Txb_L.setObjectName(u"Txb_L")
        self.Txb_L.setGeometry(QRect(300, 80, 51, 22))
        font1 = QFont()
        font1.setFamilies([u"MS PGothic"])
        font1.setPointSize(11)
        self.Txb_L.setFont(font1)
        self.Btn_Regresar = QPushButton(Dialog)
        self.Btn_Regresar.setObjectName(u"Btn_Regresar")
        self.Btn_Regresar.setGeometry(QRect(160, 370, 93, 28))
        self.Btn_Regresar.setFont(font1)
        self.Btn_Salir = QPushButton(Dialog)
        self.Btn_Salir.setObjectName(u"Btn_Salir")
        self.Btn_Salir.setGeometry(QRect(390, 370, 93, 28))
        self.Btn_Salir.setFont(font1)
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(50, 40, 401, 221))
        self.label_3.setStyleSheet(u"image: url(:/perimetros/perimetro_rombo.png);")
        self.Lbl_Resultado = QLabel(Dialog)
        self.Lbl_Resultado.setObjectName(u"Lbl_Resultado")
        self.Lbl_Resultado.setGeometry(QRect(30, 310, 300, 31))
        self.Lbl_Resultado.setFont(font)
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(290, 80, 21, 16))
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        self.label_4.setFont(font2)
        self.Btn_Calcular = QPushButton(Dialog)
        self.Btn_Calcular.setObjectName(u"Btn_Calcular")
        self.Btn_Calcular.setGeometry(QRect(280, 370, 93, 28))
        self.Btn_Calcular.setFont(font1)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(120, 10, 261, 20))
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        self.label_3.raise_()
        self.Lbl_Formula.raise_()
        self.Txb_L.raise_()
        self.Btn_Regresar.raise_()
        self.Btn_Salir.raise_()
        self.Lbl_Resultado.raise_()
        self.label_4.raise_()
        self.Btn_Calcular.raise_()
        self.label.raise_()

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.Lbl_Formula.setText(QCoreApplication.translate("Dialog", u"Formula:  L * 4", None))
        self.Btn_Regresar.setText(QCoreApplication.translate("Dialog", u"Regresar", None))
        self.Btn_Salir.setText(QCoreApplication.translate("Dialog", u"Salir", None))
        self.label_3.setText("")
        self.Lbl_Resultado.setText(QCoreApplication.translate("Dialog", u"Resultado:", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"L", None))
        self.Btn_Calcular.setText(QCoreApplication.translate("Dialog", u"Calcular", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Perimetro Rombo", None))
    # retranslateUi

