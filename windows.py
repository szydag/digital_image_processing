from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton
from ui.home_page import create_home_page_content
from ui.image_operations import NewWindow
from ui.sigmoid import SigmoidFunctionsWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dijital Görüntü İşleme")
        self.setGeometry(100, 100, 800, 600)
        self.set_background()

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        create_home_page_content(self)

        self.create_menu_navigation()

    def set_background(self):
        self.setStyleSheet("MainWindow {background-image: url('resources/images/background.png');}")

    def create_menu_navigation(self):
        toolbar = self.addToolBar("Dijital Sinyal İşleme")
        action_odev1 = QtWidgets.QAction("Standart İşlemler", self)
        action_odev1.triggered.connect(self.open_new_window_odev1)
        toolbar.addAction(action_odev1)

        action_odev2 = QtWidgets.QAction("Sigmoid Fonksiyonları", self)
        action_odev2.triggered.connect(self.open_new_window_odev2)
        toolbar.addAction(action_odev2)

    def open_new_window_odev1(self):
        self.new_window = NewWindow("Standart İşlemler")
        self.new_window.show()

    def open_new_window_odev2(self):
        self.new_window = SigmoidFunctionsWindow()
        self.new_window.show()
