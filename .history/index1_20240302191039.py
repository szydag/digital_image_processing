import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMdiArea, QMdiSubWindow, QAction, QMenu, QLabel, QVBoxLayout, QWidget, QFrame
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import Qt

class Work1Window(QMdiSubWindow): 
    def __init__(self, image, parent=None):
        super().__init__(parent)

        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setPixmap(QPixmap.fromImage(image))

        self.histogram_label = QLabel("Histogram")
        self.channels_label = QLabel("Kanallar")
        
        layout = QVBoxLayout()
        layout.addWidget(self.image_label)
        layout.addWidget(self.histogram_label)
        layout.addWidget(self.channels_label)

        widget = QWidget()
        widget.setLayout(layout)
        self.setWidget(widget)
        
        
class MainWindow(QMainWindow):   
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dijital Görüntü İşleme")
        self.setGeometry(100, 100, 800, 600)
        self.set_background()
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.central_widget.setLayout(QVBoxLayout())
        self.create_actions()
        self.create_menu()
        self.create_home_page_content()
        
    def create_actions(self):
        self.new_action = QAction("Yeni", self)
        self.new_action.setShortcut("Ctrl+N")
        self.new_action.triggered.connect(self.new_image_processing_window)
        
    def create_menu(self):
        self.file_menu = self.menuBar().addMenu("Anasayfa")
        self.file_menu.addAction(self.new_action)

        self.point_operations_menu = self.menuBar().addMenu("Ödev 1: Temel İşlevsellik Oluşturma")
        
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
    
    def new_image_processing_window(self):
        # Yeni bir görüntü işleme penceresi aç
        image = QImage(640, 480, QImage.Format_RGB32)
        image.fill(Qt.white)  # Örnek olarak beyaz bir arka plan ekleyin
        image_processing_window = Work1Window(image)
        self.mdi_area.addSubWindow(image_processing_window)
        image_processing_window.show()
            


                
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())