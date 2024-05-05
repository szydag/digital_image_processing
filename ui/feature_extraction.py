from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QFileDialog
from PyQt5.QtGui import QPixmap, QImage
import cv2
import numpy as np
import pandas as pd

class FeatureExtraction(QMainWindow):
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
        
        self.feature_extraction_button = QPushButton("Özellik Çıkar")
        self.feature_extraction_button.clicked.connect(self.extract_features)
        self.layout.addWidget(self.feature_extraction_button)
        
        self.image = None

    def load_image(self):
        file_dialog = QFileDialog()
        image_path, _ = file_dialog.getOpenFileName(self, "Görsel Seç", "", "Resim Dosyaları (*.png *.jpg *.jpeg *.bmp *.gif)")
        if image_path:
            self.image = cv2.imread(image_path)
            self.display_image(self.image)

    def display_image(self, image):
        if image is None:
            return
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        height, width, channel = image.shape
        bytes_per_line = 3 * width
        q_image = QPixmap.fromImage(QImage(image.data, width, height, bytes_per_line, QImage.Format_RGB888))
        self.image_label.setPixmap(q_image)

    def extract_features(self):
        if self.image is None:
            print("Hata: Hiçbir resim yüklenmedi.")
            return

        # Hiperspektral resmi RGB'ye dönüştür
        hiperspektral_resim_rgb = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)

        # Koyu yeşil bölgeleri tespit etmek için eşik değerleri belirle
        lower_green = np.array([0, 100, 0], dtype="uint8")
        upper_green = np.array([50, 255, 50], dtype="uint8")

        # Eşikleme işlemi uygula
        mask = cv2.inRange(hiperspektral_resim_rgb, lower_green, upper_green)

        # Koyu yeşil bölgelerin konturunu bul
        konturlar, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        contour_image = np.zeros_like(self.image)

        # Konturları bu görüntünün üzerine çiz
        cv2.drawContours(contour_image, konturlar, -1, (0, 255, 0), 3)
        cv2.imshow('Islem Sonucu Olusan Goruntu', contour_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        # Boş bir liste oluştur
        veri_listesi = []

        # Konturları işle
        for i, kontur in enumerate(konturlar):
            # Konturun alanını hesapla
            alan = cv2.contourArea(kontur)
            # Konturun merkezini ve dış dikdörtgenin koordinatlarını bul
            M = cv2.moments(kontur)

            if M["m00"] != 0:
                cx = int(M["m10"] / M["m00"])
                cy = int(M["m01"] / M["m00"])
                x, y, w, h = cv2.boundingRect(kontur)
                # Diagonal hesapla
                diagonal = np.sqrt(w*2 + h*2)
                # Energy ve Entropy hesapla
                mask_kontur = np.zeros_like(mask)
                cv2.drawContours(mask_kontur, [kontur], -1, 255, -1)
                moments = cv2.moments(mask_kontur)
                hu_moments = cv2.HuMoments(moments).flatten()
                energy = np.sum(hu_moments[1:] ** 2)
                entropy = -np.sum(hu_moments * np.log(np.abs(hu_moments) + 1e-10))
                # Mean ve Median hesapla
                mean_val = np.mean(hiperspektral_resim_rgb[mask_kontur == 255])
                median_val = np.median(hiperspektral_resim_rgb[mask_kontur == 255])
                # Verileri liste içine ekle
                veri_listesi.append({'No': i+1, 'Center': (cx, cy), 'Length': f"{w} px", 'Width': f"{h} px", 'Diagonal': f"{diagonal} px",
                                    'Energy': energy, 'Entropy': entropy, 'Mean': mean_val, 'Median': median_val})

        # Listeyi DataFrame'e dönüştür
        excel_tablosu = pd.DataFrame(veri_listesi)
        print(excel_tablosu)
        # Verileri Excel'e aktar
        excel_tablosu.to_excel('koyu_yesil_bolgeler.xlsx', index=False)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = FeatureExtraction()
    window.show()
    app.exec_()
