import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QMdiArea, QMdiSubWindow, QAction, QMenu, QLabel, QVBoxLayout, \
    QWidget, QDialog, QToolBar, QPushButton, QFileDialog, QFrame, QGraphicsView, QGraphicsScene
from PyQt5.QtGui import QFont, QPixmap, QImage
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
from PIL import Image
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class ImageProcessor:
    def __init__(self):
        self.image = None
        self.thresholded_image = None
        self.histogram_window = None

    def load_image(self, file_path):
        if file_path:
            self.image = Image.open(file_path)

    def show_histogram(self):
        if self.image is not None:
            # Convert image to grayscale
            img_gray = self.image.convert("L")

            # Plot histogram
            histogram_values, bins = img_gray.histogram(), list(range(256))

            # Create a new window for histogram
            self.histogram_window = NewWindow("Histogram")
            self.histogram_window.show_histogram(histogram_values, bins)

    def apply_threshold(self, threshold_value):
        if self.image is not None:
            img_gray = self.image.convert("L")
            self.thresholded_image = img_gray.point(lambda x: 255 if x > threshold_value else 0)

class NewWindow(QMainWindow):
    def __init__(self, title):
        super().__init__()
        self.setWindowTitle(title)
        self.setGeometry(150, 150, 400, 300)

        self.info_label = QLabel(self)
        self.info_label.setAlignment(Qt.AlignCenter)
        layout = QVBoxLayout(self)
        layout.addWidget(self.info_label)
        layout.addStretch()

    def set_info(self, text):
        full_text = f"{text}"
        self.info_label.setText(full_text)

        # Set text style
        font = QFont("Arial", 10)
        self.info_label.setFont(font)

        # Set text color
        text_color = QColor(54, 54, 54)
        self.info_label.setStyleSheet(f"color: {text_color.name()};")

    def show_histogram(self, histogram_values, bins):
        # Embed the matplotlib figure in the PyQt5 window
        figure = Figure(figsize=(5, 4), dpi=100)
        subplot = figure.add_subplot(1, 1, 1)
        subplot.bar(bins[:-1], histogram_values, width=1, color='gray', alpha=0.75)
        subplot.set_title('Histogram')
        subplot.set_xlabel('Pixel Değeri')
        subplot.set_ylabel('Frekans')

        canvas = FigureCanvas(figure)
        canvas.draw()
        self.setCentralWidget(canvas)

def main():
    app = QApplication([])
    window = QMainWindow()
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()
