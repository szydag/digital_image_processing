from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton
from ui.home_page import create_home_page_content
from ui.image_operations import NewWindow
from ui.sigmoid import SigmoidFunctionsWindow
from ui.hough_transform import HoughTransformFunctionsWindow
from ui.deblurring import DeblurringFunctionsWindow
from ui.feature_extraction import FeatureExtraction

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

        action_sigmoid = QtWidgets.QAction("Sigmoid Fonksiyonları", self)
        action_sigmoid.triggered.connect(self.open_new_window_sigmoid)
        toolbar.addAction(action_sigmoid)
        
        action_hough = QtWidgets.QAction("Hough Dönüşleri",self)
        action_hough.triggered.connect(self.open_new_window_hough)
        toolbar.addAction(action_hough)
        
        action_deblurring = QtWidgets.QAction("Debrurring Algoritması",self)
        action_deblurring.triggered.connect(self.open_new_window_deblurring)
        toolbar.addAction(action_deblurring)

        action_feature_extraction = QtWidgets.QAction("Özellik Çıkarma",self)
        action_feature_extraction.triggered.connect(self.open_new_window_feature_extraction)
        toolbar.addAction(action_feature_extraction)
        
    def open_new_window_odev1(self):
        self.new_window = NewWindow("Standart İşlemler")
        self.new_window.show()

    def open_new_window_sigmoid(self):
        self.new_window = SigmoidFunctionsWindow()
        self.new_window.show()
        
    def open_new_window_hough(self):
        self.new_window = HoughTransformFunctionsWindow()
        self.new_window.show()
        
    def open_new_window_deblurring(self):
        self.new_window = DeblurringFunctionsWindow()
        self.new_window.show()
        
    def open_new_window_feature_extraction(self):
        self.new_window = FeatureExtraction()
        self.new_window.show()
