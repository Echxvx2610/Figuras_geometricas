#pyside6
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
#importacion de diseños propios
from menu import Ui_MainWindow as MenuPrincipal
#diseños de perimetros
from menu_perimetros import Ui_MainWindow as MenuPerimetros
from P_Circulo import Ui_Dialog as PerimetroCirculo
from P_Rombo import Ui_Dialog as PerimetroRombo
from P_Cometa import Ui_Dialog as PerimetroCometa
#diseños de areas
from menu_areas import Ui_MainWindow as MenuAreas
from A_Circulo import Ui_Dialog as AreaCirculo
from A_Rombo import Ui_Dialog as AreaRombo
from A_Cometa import Ui_Dialog as AreaCometa

#libreria matematica
import math

class StyledWindow:
    def cargarEstilos(self, archivo_qss):
        '''
        Carga estilos desde un archivo .qss y los aplica a la ventana
        '''
        estilo = QFile(archivo_qss)
        if estilo.open(QFile.ReadOnly | QFile.Text):
            stream = QTextStream(estilo)
            self.setStyleSheet(stream.readAll())
            estilo.close()
        else:
            QMessageBox.critical(self, "Error", f"No fue posible cargar el archivo: {archivo_qss}")


class MainWindow(QMainWindow, StyledWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = MenuPrincipal()  # Aplicamos la UI del menú principal
        self.ui.setupUi(self)
        # cargar estilos
        self.cargarEstilos("ui/resources/style.qss")
        
        # Conectar el botón para abrir el menú de perímetros
        self.ui.Btn_Perimetros.clicked.connect(self.openMenuPerimetros)
        self.ui.Btn_Areas.clicked.connect(self.openMenuAreas)
            
    def openMenuPerimetros(self):
        #self.hide() #esconde ventana
        # Crear una nueva ventana para el menú de perímetros
        self.menu_perimetros_window = MenuPerimetrosWindow()
        self.menu_perimetros_window.show()
        
    def openMenuAreas(self):
        self.menu_areas_window = MenuAreasWindow()
        self.menu_areas_window.show()
    
# Clases para el menú de perimetros
class MenuPerimetrosWindow(QMainWindow):
    def __init__(self):
        super(MenuPerimetrosWindow, self).__init__()
        self.ui = MenuPerimetros()  # Aplicamos la UI del menú de perímetros
        self.ui.setupUi(self)
        
        # Conectar el botón para abrir el diálogo de perímetro del círculo
        self.ui.Btn_P_Circulo.clicked.connect(self.openPerimetroCirculo)
        self.ui.Btn_P_Rombo.clicked.connect(self.openPerimetroRombo)
        self.ui.Btn_P_Cometa.clicked.connect(self.openPerimetroCometa)
        
        self.ui.Btn_Salir.clicked.connect(self.close)
        self.ui.Btn_Regresar.clicked.connect(self.close)
        
    def openPerimetroCirculo(self):
        # Crear un diálogo para el perímetro del círculo
        self.perimetro_circulo_dialog = PerimetroCirculoDialog()
        self.perimetro_circulo_dialog.exec()  # Mostrar como un diálogo modal
        
    def openPerimetroRombo(self):
        self.perimetro_rombo_dialog = PerimetroRomboDialog()
        self.perimetro_rombo_dialog.exec()

    def openPerimetroCometa(self):
        self.perimetro_cometa_dialog = PerimetroCometaDialog()
        self.perimetro_cometa_dialog.exec()

class PerimetroCirculoDialog(QDialog):
    def __init__(self):
        super(PerimetroCirculoDialog, self).__init__()
        self.ui = PerimetroCirculo()  # Aplicamos la UI del diálogo de perímetro del círculo
        self.ui.setupUi(self)
        
        # Conectar el botón para calcular el perímetro
        self.ui.Btn_Calcular.clicked.connect(self.calcular_perimetro)
        self.ui.Btn_Salir.clicked.connect(self.close)
        self.ui.Btn_Regresar.clicked.connect(self.close)
        
    def calcular_perimetro(self):
        try:
            # Obtener el valor del radio desde un QLineEdit (supongamos que se llama 'input_radio')
            radio = float(self.ui.Txb_r.text())

            # Calcular el perímetro: P = 2 * π * radio
            perimetro = 2 * math.pi * radio

            # Mostrar el resultado en un QLabel (supongamos que se llama 'label_resultado')
            self.ui.Lbl_Resultado.setText(f"Resultado: {perimetro:.2f}")
        except ValueError:
            # En caso de que el valor del radio no sea válido, mostramos un mensaje de error
            self.ui.Lbl_Resultado.setText("Error: Ingresa un número válido")

class PerimetroRomboDialog(QDialog):
    def __init__(self):
        super(PerimetroRomboDialog, self).__init__()
        self.ui = PerimetroRombo()  # Aplicamos la UI del diálogo de perímetro del círculo
        self.ui.setupUi(self)
        
        # Conectar el botón para calcular el perímetro
        self.ui.Btn_Calcular.clicked.connect(self.calcular_perimetro)
        self.ui.Btn_Salir.clicked.connect(self.close)
        self.ui.Btn_Regresar.clicked.connect(self.close)
    
    def calcular_perimetro(self):
        try:
            # Obtener el valor del radio desde un QLineEdit (supongamos que se llama 'input_radio')
            lado = float(self.ui.Txb_L.text())

            # Calcular el perímetro: P = 2 * π * radio
            perimetro = 4 * lado

            # Mostrar el resultado en un QLabel (supongamos que se llama 'label_resultado')
            self.ui.Lbl_Resultado.setText(f"Resultado: {perimetro:.2f}")
        except ValueError:
            # En caso de que el valor del radio no sea válido, mostramos un mensaje de error
            self.ui.Lbl_Resultado.setText("Error: Ingresa un número válido")
        
class PerimetroCometaDialog(QDialog):
    def __init__(self):
        super(PerimetroCometaDialog, self).__init__()
        self.ui = PerimetroCometa()  # Aplicamos la UI del diálogo de longitud del círculo
        self.ui.setupUi(self)
        
        # Conectar el botón para calcular el número de lados
        self.ui.Btn_Calcular.clicked.connect(self.calcular_perimetro)
        self.ui.Btn_Salir.clicked.connect(self.close)
        self.ui.Btn_Regresar.clicked.connect(self.close)

    def calcular_perimetro(self):
        try:
            lado_a = float(self.ui.Txb_a.text())
            lado_b = float(self.ui.Txb_b.text())
            
            perimetro = (2 * lado_a) + (2 * lado_b)

            self.ui.Lbl_Resultado.setText(f"Resultado: {perimetro:.2f}")
        except ValueError:
            self.ui.Lbl_Resultado.setText("Error: Ingresa un número válido")

# Clases para el menú de areas
class MenuAreasWindow(QMainWindow):
    def __init__(self):
        super(MenuAreasWindow, self).__init__()
        self.ui = MenuAreas()  # Aplicamos la UI del menú de areas
        self.ui.setupUi(self)
        
        # Conectar el botón para abrir el diálogo de longitud del círculo
        self.ui.Btn_A_Circulo.clicked.connect(self.openAreaCirculo)
        self.ui.Btn_A_Rombo.clicked.connect(self.openAreaRombo)
        self.ui.Btn_A_Cometa.clicked.connect(self.openAreaCometa)
        self.ui.Btn_Regresar.clicked.connect(self.close)
        self.ui.Btn_Salir.clicked.connect(self.close)
        
    def openAreaCirculo(self):
        # Crear un diálogo para el número de lados
        self.area_circulo_dialog = AreaCirculoDialog()
        self.area_circulo_dialog.exec()
        
    def openAreaRombo(self):
        self.area_rombo_dialog = AreaRomboDialog()
        self.area_rombo_dialog.exec()
    
    def openAreaCometa(self):
        self.area_cometa_dialog = AreaCometaDialog()
        self.area_cometa_dialog.exec()

class AreaCirculoDialog(QDialog):
    def __init__(self):
        super(AreaCirculoDialog, self).__init__()
        self.ui = AreaCirculo()  # Aplicamos la UI del diálogo de longitud del círculo
        self.ui.setupUi(self)
        
        # Conectar el boton para calcular el area
        self.ui.Btn_Calcular.clicked.connect(self.calcular_area)
        self.ui.Btn_Regresar.clicked.connect(self.close)
        self.ui.Btn_Salir.clicked.connect(self.close)
        
        
    def calcular_area(self):
        pass
    
class AreaRomboDialog(QDialog):
    def __init__(self):
        super(AreaRomboDialog, self).__init__()
        self.ui = AreaRombo()  # Aplicamos la UI del diálogo de longitud del círculo
        self.ui.setupUi(self)
        
        # Conectar el boton para calcular el area
        self.ui.Btn_Calcular.clicked.connect(self.calcular_area)
        self.ui.Btn_Regresar.clicked.connect(self.close)
        self.ui.Btn_Salir.clicked.connect(self.close)
        
    def calcular_area(self):
        pass
    
class AreaCometaDialog(QDialog):
    def __init__(self):
        super(AreaCometaDialog,self).__init__()
        self.ui = AreaCometa()
        self.ui.setupUi(self)
        
        # Conectar el boton para calcular el area
        self.ui.Btn_Calcular.clicked.connect(self.calcular_area)
        self.ui.Btn_Regresar.clicked.connect(self.close)
        self.ui.Btn_Salir.clicked.connect(self.close)
        
    def calcular_area(self):
        pass

if __name__ == "__main__":
    app = QApplication([])

    # Mostrar la ventana principal
    window = MainWindow()
    window.show()

    app.exec()
