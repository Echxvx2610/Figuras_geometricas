# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'V_Piramide.ui'
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
from PySide6.QtOpenGLWidgets import QOpenGLWidget
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(331, 394)
        self.openGLWidget = QOpenGLWidget(Dialog)
        self.openGLWidget.setObjectName(u"openGLWidget")
        self.openGLWidget.setGeometry(QRect(0, 0, 331, 221))
        self.Lbl_Formula = QLabel(Dialog)
        self.Lbl_Formula.setObjectName(u"Lbl_Formula")
        self.Lbl_Formula.setGeometry(QRect(10, 280, 211, 16))
        font = QFont()
        font.setFamilies([u"MS Gothic"])
        font.setPointSize(14)
        self.Lbl_Formula.setFont(font)
        self.Lbl_Resultado = QLabel(Dialog)
        self.Lbl_Resultado.setObjectName(u"Lbl_Resultado")
        self.Lbl_Resultado.setGeometry(QRect(10, 310, 241, 21))
        self.Lbl_Resultado.setFont(font)
        self.layoutWidget = QWidget(Dialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 360, 295, 31))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.Btn_Regresar = QPushButton(self.layoutWidget)
        self.Btn_Regresar.setObjectName(u"Btn_Regresar")
        font1 = QFont()
        font1.setFamilies([u"MS Gothic"])
        font1.setPointSize(12)
        self.Btn_Regresar.setFont(font1)

        self.horizontalLayout.addWidget(self.Btn_Regresar)

        self.Btn_Calcular = QPushButton(self.layoutWidget)
        self.Btn_Calcular.setObjectName(u"Btn_Calcular")
        self.Btn_Calcular.setFont(font1)

        self.horizontalLayout.addWidget(self.Btn_Calcular)

        self.Btn_Salir = QPushButton(self.layoutWidget)
        self.Btn_Salir.setObjectName(u"Btn_Salir")
        self.Btn_Salir.setFont(font1)

        self.horizontalLayout.addWidget(self.Btn_Salir)

        self.Txb_h = QLineEdit(Dialog)
        self.Txb_h.setObjectName(u"Txb_h")
        self.Txb_h.setGeometry(QRect(250, 240, 41, 20))
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(130, 240, 21, 16))
        self.label_4.setFont(font)
        self.Txb_b = QLineEdit(Dialog)
        self.Txb_b.setObjectName(u"Txb_b")
        self.Txb_b.setGeometry(QRect(150, 240, 41, 20))
        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(230, 240, 21, 16))
        self.label_5.setFont(font)
        self.Txb_a = QLineEdit(Dialog)
        self.Txb_a.setObjectName(u"Txb_a")
        self.Txb_a.setGeometry(QRect(50, 240, 41, 20))
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 240, 21, 16))
        self.label_3.setFont(font)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.Lbl_Formula.setText(QCoreApplication.translate("Dialog", u"Formula: 1/4b*a*h", None))
        self.Lbl_Resultado.setText(QCoreApplication.translate("Dialog", u"Resultado:", None))
        self.Btn_Regresar.setText(QCoreApplication.translate("Dialog", u"Regresar", None))
        self.Btn_Calcular.setText(QCoreApplication.translate("Dialog", u"Calcular", None))
        self.Btn_Salir.setText(QCoreApplication.translate("Dialog", u"Salir", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"b:", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"h:", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"a:", None))
    # retranslateUi

