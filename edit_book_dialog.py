from PyQt5.QtWidgets import QDialog, QLineEdit, QPushButton, QVBoxLayout, QLabel, QMessageBox
from db import update_book

class EditBookDialog(QDialog):
    def __init__(self, book):
        super().__init__()
        self.setWindowTitle("Edytuj książkę")
        self.setFixedSize(300, 200)
        self.book_id = book[0]

        self.title_input = QLineEdit(book[1])
        self.author_input = QLineEdit(book[2])
        self.year_input = QLineEdit(str(book[3]))

        self.save_button = QPushButton("Zapisz zmiany")
        self.save_button.clicked.connect(self.save_changes)

        self.setStyleSheet("""
            QDialog {
                background-color: #f8f8f8;
            }
            QLineEdit {
                padding: 5px;
                border-radius: 5px;
                border: 1px solid #ccc;
            }
            QPushButton {
                background-color: #28a745;
                color: white;
                font-size: 14px;
                border-radius: 5px;
                padding: 8px;
            }
            QPushButton:hover {
                background-color: #218838;
            }
        """)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Tytuł:"))
        layout.addWidget(self.title_input)
        layout.addWidget(QLabel("Autor:"))
        layout.addWidget(self.author_input)
        layout.addWidget(QLabel("Rok:"))
        layout.addWidget(self.year_input)
        layout.addWidget(self.save_button)

        self.setLayout(layout)

    def save_changes(self):
        title = self.title_input.text()
        author = self.author_input.text()
        year = self.year_input.text()

        if not title or not author or not year.isdigit():
            QMessageBox.warning(self, "Błąd", "Uzupełnij poprawnie wszystkie pola.")
            return

        update_book(self.book_id, title, author, int(year))
        QMessageBox.information(self, "Zapisano", "Dane książki zostały zaktualizowane.")
        self.accept()
