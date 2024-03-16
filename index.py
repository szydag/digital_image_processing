import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QFileDialog, QInputDialog, QFrame, QLineEdit
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt
import numpy as np
import math
from PIL import Image, ImageQt
from PyQt5.QtGui import QTransform


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
        
        self.zoom_factor = 1.0  # Başlangıçta zoom faktörü 1.0 olarak ayarlanır

        self.zoom_in_button = QPushButton("Zoom In")
        self.zoom_in_button.clicked.connect(self.zoom_in)
        self.layout.addWidget(self.zoom_in_button)

        self.zoom_out_button = QPushButton("Zoom Out")
        self.zoom_out_button.clicked.connect(self.zoom_out)
        self.layout.addWidget(self.zoom_out_button)
        
        self.rotate_button = QPushButton("Görüntüyü Döndür")
        self.rotate_button.clicked.connect(self.rotate_image)
        self.layout.addWidget(self.rotate_button)
        
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

        pixmap = QPixmap(self.image_path)
        new_width = int(pixmap.width() * ratio)
        scaled_pixmap = pixmap.scaledToWidth(new_width)
        self.image_label.setPixmap(scaled_pixmap)
        self.info_label.setText("Resim yeniden boyutlandırıldı.")
        
    def rotate_image(self):
        angle, ok = QInputDialog.getDouble(self, "Döndürme Açısı", "Açıyı giriniz (derece):", decimals=2)
        if ok:
            self.rotate_angle = angle
            self.update_image_rotate()
            
    def update_image_rotate(self):
        if self.image_path is None:
            self.info_label.setText("Önce bir resim yükleyin.")
            return
        
        try:
            pixmap = QPixmap(self.image_path)
            
            transform = QTransform()
            transform.rotate(self.rotate_angle)
            
            rotated_pixmap = pixmap.transformed(transform, Qt.SmoothTransformation)
            
            self.image_label.setPixmap(rotated_pixmap)
            
            self.info_label.setText(f"Resim {self.rotate_angle} derece döndürüldü.")
        except Exception as e:
            self.info_label.setText(f"Hata oluştu: {str(e)}")
            
        
    def zoom_in(self):
        self.zoom_factor *= 1.1 
        self.update_image()

    def zoom_out(self):
        self.zoom_factor /= 1.1  
        self.update_image()
        

    def update_image(self):
        if self.image_path is None:
            self.info_label.setText("Önce bir resim yükleyin.")
            return
        
        try:
            pixmap = QPixmap(self.image_path)
            new_width = int(pixmap.width() * self.zoom_factor)
            new_height = int(pixmap.height() * self.zoom_factor)
            scaled_pixmap = pixmap.scaled(new_width, new_height, Qt.KeepAspectRatio)
            self.image_label.setPixmap(scaled_pixmap)
            self.info_label.setText(f"Görüntü zoom in veya zoom out yapıldı. Yeni boyut: {new_width}x{new_height}")
        except Exception as e:
            self.info_label.setText(f"Hata oluştu: {str(e)}")
            
        if hasattr(self, 'rotate_angle'):
            try:
                # PIL Image kütüphanesini kullanarak döndürme işlemi
                image = Image.open(self.image_path)
                rotated_image = image.rotate(self.rotate_angle, resample=Image.BICUBIC, expand=True)
                
                # Döndürülen görüntüyü QPixmap nesnesine dönüştür
                rotated_pixmap = QPixmap.fromImage(rotated_image.toqimage())

                # QLabel üzerinde döndürülen görüntüyü göster
                self.image_label.setPixmap(rotated_pixmap.scaledToWidth(400))
                self.info_label.setText(f"Görüntü {self.rotate_angle} derece döndürüldü.")
            except Exception as e:
                self.info_label.setText(f"Döndürme sırasında bir hata oluştu: {str(e)}")



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
