
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QFileDialog
from PyQt5.QtGui import QPixmap, QImage
import cv2
import numpy as np

class DeblurringFunctionsWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Görüntü İşleme Uygulaması")
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
        
        self.deblur_image_button = QPushButton("Bulanıklığı Gider")
        self.deblur_image_button.clicked.connect(self.deblur_image)
        self.layout.addWidget(self.deblur_image_button)
        
        self.image = None

    def load_image(self):
        file_dialog = QFileDialog()
        image_path, _ = file_dialog.getOpenFileName(self, "Görsel Seç", "", "Resim Dosyaları (*.png *.jpg *.jpeg *.bmp *.gif)")
        if image_path:
            self.image = cv2.imread(image_path)
            self.display_image(self.image)

    def deblur_image(self):
        if self.image is None:
            print("Hata: Hiçbir resim yüklenmedi.")
            return

        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        blurred_image = cv2.GaussianBlur(gray, (21, 21), 0)
        psf = np.zeros((21, 21))
        psf[21 // 2, :] = 1 / 21 

        deblurred_image = self.wiener_filter(blurred_image, psf)

        # Normalize the result and convert to uint8
        deblurred_image = np.fft.fftshift(deblurred_image)
        deblurred_image = (deblurred_image - np.min(deblurred_image)) / (np.max(deblurred_image) - np.min(deblurred_image))
        deblurred_image = (deblurred_image * 255).astype(np.uint8)

        self.display_image(deblurred_image)

    def display_image(self, image):
        if len(image.shape) == 2:
            image = cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)
        height, width, channel = image.shape
        bytes_per_line = 3 * width
        q_image = QPixmap.fromImage(QImage(image.data, width, height, bytes_per_line, QImage.Format_RGB888))
        self.image_label.setPixmap(q_image)


    def wiener_filter(self, image, kernel, K=0.01):
        dummy = np.copy(image)
        image = np.fft.fft2(image)
        kernel = np.fft.fft2(kernel, s=image.shape)
        kernel = np.conj(kernel) / (np.abs(kernel) ** 2 + K)
        image = np.fft.ifft2(image * kernel)
        image = np.abs(np.fft.fftshift(image))
        return image

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = DeblurringFunctionsWindow()
    window.show()
    app.exec_()
