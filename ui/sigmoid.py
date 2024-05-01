from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QFileDialog
from PyQt5.QtGui import QPixmap
import numpy as np
from PIL import Image, ImageOps, ImageEnhance

class SigmoidFunctionsWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Sigmoid Kontrast Güçlendirme")
        self.setGeometry(100, 100, 800, 600)
        
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.image_label = QLabel("Görsel Buraya Gelecek")
        self.image_label.setAlignment(QtCore.Qt.AlignCenter)
        self.layout.addWidget(self.image_label)

        self.load_image_button = QPushButton("Görsel Yükle")
        self.load_image_button.clicked.connect(self.load_image)
        self.layout.addWidget(self.load_image_button)

        # Sigmoid Fonksiyonu Butonları
        self.standard_button = QPushButton("Standart Sigmoid Fonksiyonu")
        self.standard_button.clicked.connect(lambda: self.apply_sigmoid('standard'))
        self.layout.addWidget(self.standard_button)

        self.shifted_button = QPushButton("Yatay Kaydırılmış Sigmoid Fonksiyonu")
        self.shifted_button.clicked.connect(lambda: self.apply_sigmoid('shifted'))
        self.layout.addWidget(self.shifted_button)

        self.sloped_button = QPushButton("Eğimli Sigmoid Fonksiyonu")
        self.sloped_button.clicked.connect(lambda: self.apply_sigmoid('sloped'))
        self.layout.addWidget(self.sloped_button)

        self.custom_button = QPushButton("Kendi Fonksiyonun")
        self.custom_button.clicked.connect(lambda: self.apply_sigmoid('custom'))
        self.layout.addWidget(self.custom_button)

        self.image = None

    def load_image(self):
        file_dialog = QFileDialog()
        image_path, _ = file_dialog.getOpenFileName(self, "Görsel Seç", "", "Resim Dosyaları (*.png *.jpg *.jpeg *.bmp *.gif)")
        if image_path:
            self.image = Image.open(image_path)
            self.image_label.setPixmap(QPixmap(image_path))

    def apply_sigmoid(self, mode):
        if self.image is None:
            return

        img = np.array(self.image).astype(np.float32) / 255.0
        
        if mode == 'standard':
            result = self.sigmoid(img)
        elif mode == 'shifted':
            result = self.sigmoid(img - 0.5) + 0.5
        elif mode == 'sloped':
            result = self.sigmoid(img * 1.5)
        elif mode == 'custom':
            result = self.custom_sigmoid(img)
        else:
            return

        result = (result * 255).astype(np.uint8)
        image_pil = Image.fromarray(result)
        image_pil.save("temp.jpg")
        self.image_label.setPixmap(QPixmap("temp.jpg"))

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x * 10))

    def custom_sigmoid(self, x):
        return 1 / (1 + np.exp(-((x - 0.5) * 20)))  # Örnek olarak daha dramatik bir efekt

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = SigmoidFunctionsWindow()
    window.show()
    app.exec_()
