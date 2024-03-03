import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMdiArea, QMdiSubWindow, QAction, QMenu, QLabel, QVBoxLayout, QWidget, QFrame
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dijital Görüntü İşleme")
        self.setGeometry(100, 100, 800, 600)
        self.set_background()
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.central_widget.setLayout(QVBoxLayout())
        self.create_menu()
        #self.create_home_page_content()
        self.create_work1_content()
        
    def create_menu(self):
        self.file_menu = self.menuBar().addMenu("Anasayfa")
        
        self.work1_action = QAction("Aç", self)
        self.work1_action.triggered.connect(self.create_work1_content)  # QAction'a slot bağlama
        self.point_operations_menu = self.menuBar().addMenu("Ödev 1: Temel İşlevsellik Oluşturma")
        self.point_operations_menu.addAction(self.work1_action)
        
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
        
    def set_background(self):
        self.setStyleSheet("MainWindow {background-image: url('assets/images/background.png');}")
        
    def create_work1_content(self):
        self.clear_content()  # Mevcut içeriği temizle

        # Yeni içeriği merkezi widget'a ekleyin
        layout = self.central_widget.layout()

        label1 = QLabel("ödev1 ")
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
        
    def clear_content(self):
        # Mevcut içeriği temizleyin
        for i in reversed(range(self.central_widget.layout().count())): 
            widget_to_remove = self.central_widget.layout().itemAt(i).widget()
            if widget_to_remove is not None:  # Eğer widget varsa, kaldır
                widget_to_remove.setParent(None)
            else:  # Eğer widget yoksa, layout item'ını kaldır
                self.central_widget.layout().itemAt(i).layout().setParent(None)
        
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())