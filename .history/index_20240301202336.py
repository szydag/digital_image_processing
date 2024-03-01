import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMdiArea, QMdiSubWindow, QAction, QMenu, QLabel, QVBoxLayout, QWidget
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import Qt

class ImageProcessingWindow(QMdiSubWindow):
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

        self.mdi_area = QMdiArea()
        self.setCentralWidget(self.mdi_area)

        self.create_actions()
        self.create_menus()

        self.setWindowTitle("Görüntü İşleme Uygulaması")
        self.setGeometry(100, 100, 800, 600)

    def create_actions(self):
        self.new_action = QAction("Yeni", self)
        self.new_action.setShortcut("Ctrl+N")
        self.new_action.triggered.connect(self.new_image_processing_window)

        # Diğer eylemleri burada ekleyebilirsiniz...

    def create_menus(self):
        self.file_menu = self.menuBar().addMenu("Dosya")
        self.file_menu.addAction(self.new_action)

        self.point_operations_menu = self.menuBar().addMenu("Noktasal İşlemler")
        # Noktasal İşlemler menüsü altındaki eylemleri burada ekleyebilirsiniz...

        self.digital_operations_menu = self.menuBar().addMenu("Sayısal İşlemler")
        # Sayısal İşlemler menüsü altındaki eylemleri burada ekleyebilirsiniz...

        self.filters_menu = self.menuBar().addMenu("Filtreler")
        # Filtreler menüsü altındaki eylemleri burada ekleyebilirsiniz...

        self.matrix_operations_menu = self.menuBar().addMenu("Matris İşlemleri")
        # Matris İşlemleri menüsü altındaki eylemleri burada ekleyebilirsiniz...

    def new_image_processing_window(self):
        # Yeni bir görüntü işleme penceresi aç
        image = QImage(640, 480, QImage.Format_RGB32)
        image.fill(Qt.white)  # Örnek olarak beyaz bir arka plan ekleyin
        image_processing_window = ImageProcessingWindow(image)
        self.mdi_area.addSubWindow(image_processing_window)
        image_processing_window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
