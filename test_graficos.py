import sys
import numpy as np
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QWidget
import pyqtgraph.opengl as gl

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Modelos 2D y 3D de Figuras Geométricas")
        
        # Crear el layout principal como un QHBoxLayout para tener los botones a la izquierda y la vista gráfica a la derecha
        main_layout = QHBoxLayout()

        # Crear el layout para los botones (lateral izquierdo)
        button_layout = QVBoxLayout()

        # Botones para mostrar las figuras
        self.button_circle = QPushButton("Mostrar Círculo 2D")
        self.button_rhombus = QPushButton("Mostrar Rombo 2D")
        self.button_comet = QPushButton("Mostrar Cometa 2D")
        self.button_sphere = QPushButton("Mostrar Esfera 3D")
        self.button_pyramid = QPushButton("Mostrar Pirámide 3D")
        self.button_cylinder = QPushButton("Mostrar Cilindro 3D")

        button_layout.addWidget(self.button_circle)
        button_layout.addWidget(self.button_rhombus)
        button_layout.addWidget(self.button_comet)
        button_layout.addWidget(self.button_sphere)
        button_layout.addWidget(self.button_pyramid)
        button_layout.addWidget(self.button_cylinder)

        # Crear un widget central para contener el layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.central_widget.setLayout(main_layout)

        # Crear la vista OpenGL para los gráficos
        self.plot_3d = gl.GLViewWidget()
        self.plot_3d.setMinimumSize(400, 400)  # Para que la vista 3D sea visible desde el principio
        # Cambiar el color de fondo de la vista 3D
        self.plot_3d.setBackgroundColor((255, 255, 255, 255))  # Fondo blanco (R, G, B, A)

        # Añadir los layouts al layout principal
        main_layout.addLayout(button_layout)
        main_layout.addWidget(self.plot_3d)

        # Conectar los botones a las funciones
        self.button_circle.clicked.connect(self.display_circle)
        self.button_rhombus.clicked.connect(self.display_rhombus)
        self.button_comet.clicked.connect(self.display_comet)
        self.button_sphere.clicked.connect(self.display_sphere)
        self.button_pyramid.clicked.connect(self.display_pyramid)
        self.button_cylinder.clicked.connect(self.display_cylinder)

    def display_circle(self):
        self.clear_view()

        # Crear un círculo en 2D usando OpenGL
        theta = np.linspace(0, 2 * np.pi, 100)
        x = np.cos(theta)
        y = np.sin(theta)
        z = np.zeros_like(x)  # Coordenada Z para 2D

        points = np.vstack([x, y, z]).T
        lines = np.vstack([points[:-1], points[1:]]).reshape((-1, 2, 3))

        self.add_lines_to_3d(lines, color=(0, 0, 1, 1))  # Color azul

    def display_rhombus(self):
        self.clear_view()

        # Crear un rombo en 2D usando OpenGL
        x = [0, 1, 0, -1, 0]
        y = [1, 0, -1, 0, 1]
        z = [0] * 5  # Coordenada Z para 2D

        points = np.vstack([x, y, z]).T
        lines = np.vstack([points[:-1], points[1:]]).reshape((-1, 2, 3))

        self.add_lines_to_3d(lines, color=(0, 1, 0, 1))  # Color verde

    def display_comet(self):
        self.clear_view()

        # Crear una cometa en 2D usando OpenGL ajustando la parte superior del rombo
        x = [0, 1, 0, -1, 0]
        y = [1.5, 0, -1, 0, 1.5]  # Estirar la esquina superior para darle forma de cometa
        z = [0] * 5  # Coordenada Z para 2D

        points = np.vstack([x, y, z]).T
        lines = np.vstack([points[:-1], points[1:]]).reshape((-1, 2, 3))

        self.add_lines_to_3d(lines, color=(1, 0, 0, 1))  # Color rojo


    def display_sphere(self):
        self.clear_view()

        # Crear una esfera en 3D
        mesh_data = gl.MeshData.sphere(rows=20, cols=20)
        mesh_item = gl.GLMeshItem(meshdata=mesh_data, color=(1, 0, 0, 1), shader="shaded", drawEdges=True)
        self.plot_3d.addItem(mesh_item)

    def display_pyramid(self):
        self.clear_view()

        # Crear una pirámide en 3D y aumentar la altura
        verts = np.array([[0, 0, 2], [1, 1, 0], [-1, 1, 0], [-1, -1, 0], [1, -1, 0]])  # Aumentar el Z del vértice superior a 2
        faces = np.array([[0, 1, 2], [0, 2, 3], [0, 3, 4], [0, 4, 1], [1, 2, 3], [1, 3, 4]])  # Base dividida en triángulos
        mesh_data = gl.MeshData(vertexes=verts, faces=faces)
        mesh_item = gl.GLMeshItem(meshdata=mesh_data, color=(0, 1, 0, 1), shader="shaded", drawEdges=True)

        # Añadir el elemento a la vista
        self.plot_3d.addItem(mesh_item)

    def display_cylinder(self):
        self.clear_view()

        # Crear un cilindro en 3D
        mesh_data = gl.MeshData.cylinder(rows=10, cols=20, radius=[1.0, 1.0], length=2.0)
        mesh_item = gl.GLMeshItem(meshdata=mesh_data, color=(0, 0, 1, 1), shader="shaded", drawEdges=True)
        self.plot_3d.addItem(mesh_item)

    def clear_view(self):
        """Limpia la vista actual antes de mostrar una nueva figura"""
        self.plot_3d.clear()  # Limpiar los elementos 3D

    def add_lines_to_3d(self, lines, color=(1, 1, 1, 1)):
        """Añadir líneas 2D/3D a la vista OpenGL"""
        for line in lines:
            line_item = gl.GLLinePlotItem(pos=line, color=color, width=2.0, antialias=True)
            self.plot_3d.addItem(line_item)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
