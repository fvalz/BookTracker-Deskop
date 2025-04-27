import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QPushButton

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Biblioteka")
        self.setGeometry(100, 100, 400, 300)

        
        self.layout = QVBoxLayout()

        
        self.label = QLabel("Lista książek:", self)
        self.layout.addWidget(self.label)

        
        self.add_button = QPushButton("Dodaj książkę", self)
        self.add_button.clicked.connect(self.add_book)
        self.layout.addWidget(self.add_button)

        
        self.setLayout(self.layout)

    def add_book(self):
        print("Kliknięto przycisk 'Dodaj książkę'")


app = QApplication(sys.argv)
window = MainWindow()
window.show()

sys.exit(app.exec_())

