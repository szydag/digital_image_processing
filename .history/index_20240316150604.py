import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QFileDialog, QFrame, QAction, QVBoxLayout, QToolBar
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import numpy as np
from PyQt5.QtWidgets import QLineEdit


class NewWindow(QMainWindow):
    def __init__(self, text="", parent=None):
        super().__init__(parent)
        self.setWindowTitle("İşlem Sayfası")
        self.setGeometry(100, 100, 600, 400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.info_label = QLabel(text, self)
        self.info_label.setAlignment(QtCore.Qt.AlignCenter)
        self.layout.addWidget(self.info_label)

        self.image_label = QLabel("Görsel Buraya Gelecek")
        self.image_label.setAlignment(QtCore.Qt.AlignCenter)
        self.layout.addWidget(self.image_label)

        self.load_image_button = QPushButton("Görsel Yükle")
        self.load_image_button.clicked.connect(self.load_image)
        self.layout.addWidget(self.load_image_button)
        
        self.image_path = None
        
        self.resize_ratio_edit = QLineEdit(self)
        self.resize_ratio_edit.setPlaceholderText("Yeniden Boyutlandırma Oranı (örn: 0.5)")
        self.layout.addWidget(self.resize_ratio_edit)
        
        self.resize_image_button = QPushButton("Resmi Yeniden Boyutlandır")
        self.resize_image_button.clicked.connect(self.resize_loaded_image)
        self.layout.addWidget(self.resize_image_button)
        
    def load_image(self):
        file_dialog = QFileDialog()
        self.image_path, _ = file_dialog.getOpenFileName(self, "Görsel Seç", "", "Resim Dosyaları (*.png *.jpg *.jpeg *.bmp *.gif)")
        if self.image_path:
            pixmap = QPixmap(self.image_path)
            self.image_label.setPixmap(pixmap.scaledToWidth(400))  # Başlangıçta bir genişlik ayarlayarak göster
            self.info_label.setText("Resim yüklendi. Yeniden boyutlandırmak için bir oran girin.")

    def resize_loaded_image(self):
        if self.image_path is None or self.resize_ratio_edit.text() == "":
            self.info_label.setText("Lütfen önce bir resim yükleyin ve bir oran girin.")
            return
        
        try:
            ratio = float(self.resize_ratio_edit.text())
            if not (0 < ratio):
                raise ValueError("Oran 0'dan büyük olmalıdır.")
        except ValueError:
            self.info_label.setText("Geçersiz oran. Lütfen geçerli bir sayı girin.")
            return

        # Yüklenen resmi ve kullanıcı tarafından girilen oranı kullanarak yeniden boyutlandırma
        pixmap = QPixmap(self.image_path)
        new_width = int(pixmap.width() * ratio)
        scaled_pixmap = pixmap.scaledToWidth(new_width)
        self.image_label.setPixmap(scaled_pixmap)
        self.info_label.setText("Resim yeniden boyutlandırıldı.")


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

    def create_menu_navigation(self):
        toolbar = self.addToolBar("Dijital Sinyal İşleme")

        action_odev1 = QtWidgets.QAction("Ödev 1: Temel İşlevsellik Oluşturma", self)
        action_odev1.triggered.connect(self.open_new_window_odev1)
        toolbar.addAction(action_odev1)

        action_odev2 = QtWidgets.QAction("Ödev 2: Temel Görüntü Operasyonları ve İnterpolasyon", self)
        action_odev2.triggered.connect(self.open_new_window_odev2)
        toolbar.addAction(action_odev2)

    def open_new_window_odev1(self):
        self.new_window = NewWindow("Ödev 1 ")
        self.new_window.show()

    def open_new_window_odev2(self):
        self.new_window = NewWindow("Ödev 2 ")
        self.new_window.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
