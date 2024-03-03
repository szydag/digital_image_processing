import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QMdiArea, QMdiSubWindow, QAction, QMenu, QLabel, QVBoxLayout, QWidget,QDialog,QToolBar,QPushButton,QFileDialog
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor

class NewWindow(QMainWindow):
    def __init__(self, title):
        super().__init__()
        self.setWindowTitle(title)
        self.setGeometry(150, 150, 400, 300)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        self.info_label = QLabel(self)
        self.info_label.setAlignment(Qt.AlignCenter)
        layout = QVBoxLayout(central_widget)
        layout.addWidget(self.info_label)
        layout.addStretch()

    def set_info(self, info_text, detail_text):
        full_text = f"{info_text}\n{detail_text}"
        self.info_label.setText(full_text)

        # Set text style
        font = QFont("Arial", 10)
        self.info_label.setFont(font)

        # Set text color
        text_color = QColor(54, 54, 54)
        self.info_label.setStyleSheet(f"color: {text_color.name()};")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Dijital Görüntü İşleme Uygulaması")
        self.setGeometry(100, 100, 600, 400)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        self.create_main_page()
        self.create_menu_navigation()

    def create_main_page(self):
        title_label = QLabel("Dijital Görüntü İşleme Uygulaması", self)

        text_color = QColor(8 ,126 ,176)  # RGB formatında renk
        title_label.setStyleSheet(f"color: {text_color.name()}; font-size: 16pt; font-weight: bold; margin:15px;")

        student_info_label = QLabel("Numara: 211229001\nAd Soyad: Şeyda Açıkgöz", self)
        text_color = QColor(135, 206, 250	)  # RGB formatında renk
        student_info_label.setStyleSheet(f"color: {text_color.name()}; font-size: 16pt; font-weight: bold; margin:15px;")

        layout = QVBoxLayout(self.centralWidget())
        layout.addWidget(title_label, alignment=QtCore.Qt.AlignCenter)
        layout.addWidget(student_info_label, alignment=QtCore.Qt.AlignCenter)
        layout.addStretch()


    def create_menu_navigation(self):
        # Toolbar oluştur
        toolbar = QToolBar("Ödevler")
        self.addToolBar(toolbar)

        # Ödev 1 butonu
        action_odev1 = QAction("Ödev 1", self)
        action_odev1.triggered.connect(self.open_new_window_odev1)
        toolbar.addAction(action_odev1)

        # Ödev 2 butonu
        action_odev2 = QAction("Ödev 2", self)
        action_odev2.triggered.connect(self.open_new_window_odev2)
        toolbar.addAction(action_odev2)

        # Ödev 3 butonu
        action_odev3 = QAction("Ödev 3", self)
        action_odev3.triggered.connect(self.open_new_window_odev3)
        toolbar.addAction(action_odev3)

    def open_new_window_odev1(self):
        self.new_window = NewWindow("Ödev 1 ")
        info_text = "Ödev 1: Temel İşlevselliği Oluştur"
        detail_text = "Bu ödevde kullanıcıdan görüntü alınacak ve histogramı oluşturulacaktır."
        self.new_window.set_info(info_text,detail_text)
        self.new_window.show()

    def open_new_window_odev2(self):
        self.new_window = NewWindow("Ödev 2 ")
        info_text = " Ödev 2: Filtre Uygulama"
        detail_text = "Ödevin detayları"
        self.new_window.set_info(info_text,detail_text)
        self.new_window.show()


    def open_new_window_odev3(self):
        self.new_window = NewWindow("Ödev 3 ")
        info_text = " Ödev 3 ile ilgili bilgiler "
        detail_text = "Ödevin detayları"
        self.new_window.set_info(info_text, detail_text)
        self.new_window.show()


if __name__ == "__main__":

    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()