import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QMdiArea, QMdiSubWindow, QAction, QMenu, QLabel, QVBoxLayout, QWidget,QDialog,QToolBar,QPushButton,QFileDialog, QFrame
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
from PyQt5.QtGui import QPixmap

class NewWindow(QMainWindow):
    def __init__(self, text, parent =None):
        super().__init__()

        self.setWindowTitle("İşlem Sayfası")
        self.setGeometry(100, 100, 600, 400)
        
        self.info_label = QLabel("", self)
        self.info_label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(self.info_label)

    def set_info(self, text):
        self.info_label.setText(text)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.image_label = QLabel("Görsel Buraya Gelecek")
        self.layout.addWidget(self.image_label, 0, Qt.AlignCenter)

        self.load_image_button = QPushButton("Görsel Yükle")
        self.load_image_button.clicked.connect(self.load_image)
        self.layout.addWidget(self.load_image_button, 0, Qt.AlignCenter)

        self.central_widget.setLayout(self.layout)

    def load_image(self):
        file_dialog = QFileDialog()
        image_path, _ = file_dialog.getOpenFileName(self, "Görsel Seç", "", "Resim Dosyaları (*.png *.jpg *.jpeg *.bmp *.gif)")

        if image_path:
            pixmap = QPixmap(image_path)
            self.image_label.setPixmap(pixmap.scaledToWidth(400))  # Genişlik 400 piksel olacak şekilde ölçeklendir
            self.image_label.setAlignment(Qt.AlignCenter)
            
    def create_work1_page_content(self):
        # Bu metodun içeriğini MainWindow sınıfından alıyoruz
        pass


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Dijital Görüntü İşleme")
        self.setGeometry(100, 100, 800, 600)
        self.set_background()

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        self.create_home_page_content()
        self.create_menu_navigation()
        
    def set_background(self):
        self.setStyleSheet("MainWindow {background-image: url('assets/images/background.png');}")

    def create_home_page_content(self):
        frame = QFrame(self)
        frame_size = (500, 400)
        frame.setGeometry(
            int((self.width() - frame_size[0]) / 2),
            int((self.height() - frame_size[1]) / 2),
            frame_size[0],
            frame_size[1]
        )
        frame.setStyleSheet("background-color: #C6E0F1; border-radius: 15px;")
        
        layout = QVBoxLayout()
        layout.setSpacing(-50)

        label1 = QLabel("Dijital Görüntü İşleme")
        label1.setAlignment(Qt.AlignCenter)
        label1.setStyleSheet("QLabel { color: #022D4A; font-size: 40px; }")
        layout.addWidget(label1)

        label2 = QLabel("211229036")
        label2.setAlignment(Qt.AlignCenter)
        label2.setStyleSheet("QLabel { color: #022D4A; font-size: 25px; }")
        layout.addWidget(label2)

        label3 = QLabel("Şaziye Dağ")
        label3.setAlignment(Qt.AlignCenter)
        label3.setStyleSheet("QLabel { color: #022D4A; font-size: 30px; }")
        layout.addWidget(label3)

        frame.setLayout(layout)

    def create_work1_page_content(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.image_label = QLabel("Görsel Buraya Gelecek")
        self.layout.addWidget(self.image_label, 0, Qt.AlignCenter)

        self.load_image_button = QPushButton("Görsel Yükle")
        self.load_image_button.clicked.connect(self.load_image)
        self.layout.addWidget(self.load_image_button, 0, Qt.AlignCenter)

        self.central_widget.setLayout(self.layout)
    
    def load_image(self):
        file_dialog = QFileDialog()
        image_path, _ = file_dialog.getOpenFileName(self, "Görsel Seç", "", "Resim Dosyaları (*.png *.jpg *.jpeg *.bmp *.gif)")

        if image_path:
            pixmap = QPixmap(image_path)
            self.image_label.setPixmap(pixmap.scaledToWidth(400))  # Genişlik 400 piksel olacak şekilde ölçeklendir
            self.image_label.setAlignment(Qt.AlignCenter)
            
            
    def create_menu_navigation(self):
        # Toolbar oluştur
        toolbar = QToolBar("Dijital Sinyal İşleme")
        self.addToolBar(toolbar)

        # Ödev 1 butonu
        action_odev1 = QAction("Ödev 1: Temel İşlevsellik Oluşturma", self)
        action_odev1.triggered.connect(self.open_new_window_odev1)
        toolbar.addAction(action_odev1)
        
        # Ödev 2 butonu
        action_odev2 = QAction("Ödev 2: Temel Görüntü Operasyonları ve İnterpolasyon", self)
        action_odev2.triggered.connect(self.open_new_window_odev2)
        toolbar.addAction(action_odev2)

    def open_new_window_odev1(self):
        self.new_window = NewWindow("Ödev 1 ")
        text = "Histogam Alma"
        self.new_window.set_info(text)
        self.new_window.show()
        
    def open_new_window_odev2(self):
        self.new_window = NewWindow("Ödev 2 ")
        self.new_window.create_work1_page_content()  # Ödev 2'nin içeriğini oluşturmak için yeni bir fonksiyon çağırıyoruz
        self.new_window.show()


if __name__ == "__main__":

    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()