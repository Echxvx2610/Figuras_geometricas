# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'V_Esfera.ui'
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
import pyqtgraph.opengl as gl


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(323, 394)
        # Crear la vista OpenGL para los gráficos
        self.plot_3d = gl.GLViewWidget()
        self.plot_3d.setObjectName(u"openGLWidget")
        self.plot_3d.setMinimumSize(400, 400)  # Para que la vista 3D sea visible desde el principio
        # Cambiar el color de fondo de la vista 3D
        self.plot_3d.setBackgroundColor((255, 255, 255, 255))
        self.Lbl_Formula = QLabel(Dialog)
        self.Lbl_Formula.setObjectName(u"Lbl_Formula")
        self.Lbl_Formula.setGeometry(QRect(10, 280, 211, 16))
        font = QFont()
        font.setFamilies([u"MS Gothic"])
        font.setPointSize(14)
        self.Lbl_Formula.setFont(font)
        self.Lbl_Resultado = QLabel(Dialog)
        self.Lbl_Resultado.setObjectName(u"Lbl_Resultado")
        self.Lbl_Resultado.setGeometry(QRect(10, 310, 241, 16))
        self.Lbl_Resultado.setFont(font)
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 250, 21, 16))
        self.label_3.setFont(font)
        self.Txb_r = QLineEdit(Dialog)
        self.Txb_r.setObjectName(u"Txb_r")
        self.Txb_r.setGeometry(QRect(30, 250, 41, 20))
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


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.Lbl_Formula.setText(QCoreApplication.translate("Dialog", u"Formula:  4/3\u03c0r\u00b3", None))
        self.Lbl_Resultado.setText(QCoreApplication.translate("Dialog", u"Resultado:", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"r:", None))
        self.Btn_Regresar.setText(QCoreApplication.translate("Dialog", u"Regresar", None))
        self.Btn_Calcular.setText(QCoreApplication.translate("Dialog", u"Calcular", None))
        self.Btn_Salir.setText(QCoreApplication.translate("Dialog", u"Salir", None))
    # retranslateUi

