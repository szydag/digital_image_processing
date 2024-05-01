from PyQt5.QtWidgets import QLabel, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt


def create_home_page_content(main_window):
    layout = QVBoxLayout()
    main_window.layout.addLayout(layout)

    label1 = QLabel("Dijital Görüntü İşleme")
    label1.setAlignment(Qt.AlignCenter)
    label1.setStyleSheet("QLabel { color: #FFFFFF; font-size: 40px; }")
    layout.addWidget(label1)

    label2 = QLabel("211229036")
    label2.setAlignment(Qt.AlignCenter)
    label2.setStyleSheet("QLabel { color: #FFFFFF; font-size: 25px; }")
    layout.addWidget(label2)

    label3 = QLabel("Şaziye Dağ")
    label3.setAlignment(Qt.AlignCenter)
    label3.setStyleSheet("QLabel { color: #FFFFFF; font-size: 30px; }")
    layout.addWidget(label3)
