import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QMdiArea, QMdiSubWindow, QAction, QMenu, QLabel, QVBoxLayout, QWidget,QDialog,QToolBar,QPushButton,QFileDialog, QFrame
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor

class NewWindow(QMainWindow):
    def __init__(self, title):
        super().__init__()
        self.setWindowTitle(title)
        self.setGeometry(150, 150, 400, 300)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        self.info_label = QLabel(self)
        self.info_label.setAlignment(Qt.AlignCenter)
        layout = QVBoxLayout(central_widget)
        layout.addWidget(self.info_label)
        layout.addStretch()

    def set_info(self, info_text, detail_text):
        full_text = f"{info_text}\n{detail_text}"
        self.info_label.setText(full_text)

        # Set text style
        font = QFont("Arial", 10)
        self.info_label.setFont(font)

        # Set text color
        text_color = QColor(54, 54, 54)
        self.info_label.setStyleSheet(f"color: {text_color.name()};")


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


    def create_menu_navigation(self):
        # Toolbar oluştur
        toolbar = QToolBar("Dijital Sinyal İşleme")
        self.addToolBar(toolbar)

        # Ödev 1 butonu
        action_odev1 = QAction("Ödev 1: Temel İşlevsellik Oluşturma", self)
        action_odev1.triggered.connect(self.open_new_window_odev1)
        toolbar.addAction(action_odev1)

    def open_new_window_odev1(self):
        self.new_window = NewWindow("Ödev 1 ")
        info_text = "Ödev 1: Temel İşlevselliği Oluştur"
        detail_text = "Bu ödevde kullanıcıdan görüntü alınacak ve histogramı oluşturulacaktır."
        self.new_window.set_info(info_text,detail_text)
        self.new_window.show()

    def open_new_window_odev2(self):
        self.new_window = NewWindow("Ödev 2 ")
        info_text = " Ödev 2: Filtre Uygulama"
        detail_text = "Ödevin detayları"
        self.new_window.set_info(info_text,detail_text)
        self.new_window.show()


    def open_new_window_odev3(self):
        self.new_window = NewWindow("Ödev 3 ")
        info_text = " Ödev 3 ile ilgili bilgiler "
        detail_text = "Ödevin detayları"
        self.new_window.set_info(info_text, detail_text)
        self.new_window.show()


if __name__ == "__main__":

    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()