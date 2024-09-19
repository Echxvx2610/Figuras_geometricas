# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'P_Cometa.ui'
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
        Dialog.resize(537, 519)
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(310, 100, 21, 16))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(50, 40, 431, 321))
        self.label_3.setStyleSheet(u"image: url(:/perimetros/p_cometa.png);")
        self.Txb_a = QLineEdit(Dialog)
        self.Txb_a.setObjectName(u"Txb_a")
        self.Txb_a.setGeometry(QRect(320, 100, 51, 22))
        font1 = QFont()
        font1.setFamilies([u"MS PGothic"])
        font1.setPointSize(11)
        self.Txb_a.setFont(font1)
        self.Btn_Salir = QPushButton(Dialog)
        self.Btn_Salir.setObjectName(u"Btn_Salir")
        self.Btn_Salir.setGeometry(QRect(420, 470, 93, 28))
        self.Btn_Salir.setFont(font1)
        self.Lbl_Formula = QLabel(Dialog)
        self.Lbl_Formula.setObjectName(u"Lbl_Formula")
        self.Lbl_Formula.setGeometry(QRect(30, 360, 331, 41))
        font2 = QFont()
        font2.setFamilies([u"MS PGothic"])
        font2.setPointSize(16)
        self.Lbl_Formula.setFont(font2)
        self.Btn_Regresar = QPushButton(Dialog)
        self.Btn_Regresar.setObjectName(u"Btn_Regresar")
        self.Btn_Regresar.setGeometry(QRect(190, 470, 93, 28))
        self.Btn_Regresar.setFont(font1)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(140, 40, 261, 20))
        self.label.setFont(font2)
        self.label.setAlignment(Qt.AlignCenter)
        self.Btn_Calcular = QPushButton(Dialog)
        self.Btn_Calcular.setObjectName(u"Btn_Calcular")
        self.Btn_Calcular.setGeometry(QRect(300, 470, 93, 28))
        self.Btn_Calcular.setFont(font1)
        self.Lbl_Resultado = QLabel(Dialog)
        self.Lbl_Resultado.setObjectName(u"Lbl_Resultado")
        self.Lbl_Resultado.setGeometry(QRect(30, 410, 331, 31))
        self.Lbl_Resultado.setFont(font2)
        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(300, 270, 21, 16))
        self.label_5.setFont(font)
        self.Txb_b = QLineEdit(Dialog)
        self.Txb_b.setObjectName(u"Txb_b")
        self.Txb_b.setGeometry(QRect(310, 270, 51, 22))
        self.Txb_b.setFont(font1)
        self.label_3.raise_()
        self.label_4.raise_()
        self.Txb_a.raise_()
        self.Btn_Salir.raise_()
        self.Lbl_Formula.raise_()
        self.Btn_Regresar.raise_()
        self.label.raise_()
        self.Btn_Calcular.raise_()
        self.Lbl_Resultado.raise_()
        self.label_5.raise_()
        self.Txb_b.raise_()

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"a", None))
        self.label_3.setText("")
        self.Btn_Salir.setText(QCoreApplication.translate("Dialog", u"Salir", None))
        self.Lbl_Formula.setText(QCoreApplication.translate("Dialog", u"Formula:  2a + 2b", None))
        self.Btn_Regresar.setText(QCoreApplication.translate("Dialog", u"Regresar", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Perimetro Cometa", None))
        self.Btn_Calcular.setText(QCoreApplication.translate("Dialog", u"Calcular", None))
        self.Lbl_Resultado.setText(QCoreApplication.translate("Dialog", u"Resultado:", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"b", None))
    # retranslateUi

