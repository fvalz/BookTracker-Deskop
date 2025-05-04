from PyQt5.QtWidgets import QDialog, QLineEdit, QPushButton, QVBoxLayout, QLabel, QMessageBox
from db import add_book

class AddBookDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dodaj książkę")
        self.setFixedSize(300, 200)

        self.title_input = QLineEdit()
        self.title_input.setPlaceholderText("Tytuł")

        self.author_input = QLineEdit()
        self.author_input.setPlaceholderText("Autor")

        self.year_input = QLineEdit()
        self.year_input.setPlaceholderText("Rok")

        self.add_button = QPushButton("Dodaj")
        self.add_button.clicked.connect(self.add_book)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Tytuł:"))
        layout.addWidget(self.title_input)
        layout.addWidget(QLabel("Autor:"))
        layout.addWidget(self.author_input)
        layout.addWidget(QLabel("Rok:"))
        layout.addWidget(self.year_input)
        layout.addWidget(self.add_button)

        self.setLayout(layout)

    def add_book(self):
        title = self.title_input.text()
        author = self.author_input.text()
        year = self.year_input.text()

        if not title or not author or not year.isdigit():
            QMessageBox.warning(self, "Błąd", "Uzupełnij poprawnie wszystkie pola.")
            return

        add_book(title, author, int(year))
        QMessageBox.information(self, "Sukces", "Książka dodana!")
        self.accept()
