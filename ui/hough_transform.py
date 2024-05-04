from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QFileDialog
from PyQt5.QtGui import QPixmap, QImage
import cv2
import numpy as np

class HoughTransformFunctionsWindow(QMainWindow):
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
        
        self.detect_line_button = QPushButton("Çizgileri Tespit Et")
        self.detect_line_button.clicked.connect(self.detect_line)
        self.layout.addWidget(self.detect_line_button)

        self.detect_eyes_button = QPushButton("Gözleri Tespit Et")
        self.detect_eyes_button.clicked.connect(self.detect_eyes)
        self.layout.addWidget(self.detect_eyes_button)

        self.image = None

    def load_image(self):
        file_dialog = QFileDialog()
        image_path, _ = file_dialog.getOpenFileName(self, "Görsel Seç", "", "Resim Dosyaları (*.png *.jpg *.jpeg *.bmp *.gif)")
        if image_path:
            self.image = cv2.imread(image_path)
            self.display_image(self.image)

    def display_image(self, image):
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        height, width, channel = image.shape
        bytes_per_line = 3 * width
        q_image = QPixmap.fromImage(QImage(image.data, width, height, bytes_per_line, QImage.Format_RGB888))
        self.image_label.setPixmap(q_image)

    def detect_line(self):
        if self.image is None:
            print("Hata: Hiçbir resim yüklenmedi.")
            return

        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5, 5), 0)
        edges = cv2.Canny(blur, 50, 150, apertureSize=3)

        lines = cv2.HoughLinesP(edges, 1, np.pi/180, threshold=80, minLineLength=50, maxLineGap=200)

        if lines is not None:
            for line in lines:
                x1, y1, x2, y2 = line[0]
                cv2.line(self.image, (x1, y1), (x2, y2), (0, 255, 0), 2)

        self.display_image(self.image)

    def detect_eyes(self):
        if self.image is None:
            print("Hata: Hiçbir resim yüklenmedi.")
            return

        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

        if face_cascade.empty() or eye_cascade.empty():
            print("Hata: Cascade dosyaları yüklenemedi.")
            return

        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
        if len(faces) == 0:
            print("Uyarı: Hiç yüz tespit edilemedi.")
            return

        for (x, y, w, h) in faces:
            roi_gray = gray[y:y+h, x:x+w]
            eyes = eye_cascade.detectMultiScale(roi_gray)
            if len(eyes) == 0:
                print("Uyarı: Gözler tespit edilemedi.")
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(self.image[y:y+h, x:x+w], (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)

        self.display_image(self.image)

    
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = HoughTransformFunctionsWindow()
    window.show()
    app.exec_()
