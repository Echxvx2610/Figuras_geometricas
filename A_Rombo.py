# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'A_Rombo.ui'
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
        Dialog.resize(449, 449)
        self.Lbl_Formula = QLabel(Dialog)
        self.Lbl_Formula.setObjectName(u"Lbl_Formula")
        self.Lbl_Formula.setGeometry(QRect(30, 330, 331, 41))
        font = QFont()
        font.setFamilies([u"MS PGothic"])
        font.setPointSize(16)
        self.Lbl_Formula.setFont(font)
        self.Txb_d = QLineEdit(Dialog)
        self.Txb_d.setObjectName(u"Txb_d")
        self.Txb_d.setGeometry(QRect(280, 80, 51, 22))
        font1 = QFont()
        font1.setFamilies([u"MS PGothic"])
        font1.setPointSize(11)
        self.Txb_d.setFont(font1)
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(100, 30, 251, 301))
        self.label_3.setStyleSheet(u"image: url(:/areas/area_rombo.png);")
        self.Lbl_Resultado = QLabel(Dialog)
        self.Lbl_Resultado.setObjectName(u"Lbl_Resultado")
        self.Lbl_Resultado.setGeometry(QRect(30, 370, 281, 31))
        self.Lbl_Resultado.setFont(font)
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(270, 80, 21, 16))
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        self.label_4.setFont(font2)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(80, 10, 261, 20))
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        self.Txb_D = QLineEdit(Dialog)
        self.Txb_D.setObjectName(u"Txb_D")
        self.Txb_D.setGeometry(QRect(300, 270, 51, 22))
        self.Txb_D.setFont(font1)
        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(280, 270, 21, 16))
        self.label_5.setFont(font2)
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(140, 410, 295, 30))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.Btn_Regresar = QPushButton(self.widget)
        self.Btn_Regresar.setObjectName(u"Btn_Regresar")
        self.Btn_Regresar.setFont(font1)

        self.horizontalLayout.addWidget(self.Btn_Regresar)

        self.Btn_Calcular = QPushButton(self.widget)
        self.Btn_Calcular.setObjectName(u"Btn_Calcular")
        self.Btn_Calcular.setFont(font1)

        self.horizontalLayout.addWidget(self.Btn_Calcular)

        self.Btn_Salir = QPushButton(self.widget)
        self.Btn_Salir.setObjectName(u"Btn_Salir")
        self.Btn_Salir.setFont(font1)

        self.horizontalLayout.addWidget(self.Btn_Salir)

        self.label_3.raise_()
        self.Lbl_Formula.raise_()
        self.Txb_d.raise_()
        self.Btn_Regresar.raise_()
        self.Btn_Salir.raise_()
        self.Lbl_Resultado.raise_()
        self.label_4.raise_()
        self.Btn_Calcular.raise_()
        self.label.raise_()
        self.Txb_D.raise_()
        self.label_5.raise_()

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.Lbl_Formula.setText(QCoreApplication.translate("Dialog", u"Formula:  (D x d)/2", None))
        self.label_3.setText("")
        self.Lbl_Resultado.setText(QCoreApplication.translate("Dialog", u"Resultado:", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"d", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Area Rombo", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"D", None))
        self.Btn_Regresar.setText(QCoreApplication.translate("Dialog", u"Regresar", None))
        self.Btn_Calcular.setText(QCoreApplication.translate("Dialog", u"Calcular", None))
        self.Btn_Salir.setText(QCoreApplication.translate("Dialog", u"Salir", None))
    # retranslateUi

