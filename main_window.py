from PyQt5.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget, QListView, QMessageBox, QFrame
from PyQt5.QtCore import QStringListModel
from PyQt5.QtGui import QColor, QPalette, QFont
from add_book_dialog import AddBookDialog
from edit_book_dialog import EditBookDialog
from db import get_books, delete_book
import os
from login_window import LoginWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Biblioteka - Panel główny")
        self.setGeometry(0, 0, 1920, 1080)  # Ustawiamy na pełny ekran
        self.show()

        # Ustawienia ogólne aplikacji
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f0f0f0;
            }
            QPushButton {
                background-color: #007BFF;
                color: white;
                border-radius: 10px;
                font-size: 14px;
                padding: 10px;
                margin-bottom: 10px;
            }
            QPushButton:hover {
                background-color: #0056b3;
            }
            QPushButton:pressed {
                background-color: #004085;
            }
            QListView {
                border: 1px solid #ddd;
                border-radius: 10px;
                padding: 10px;
                background-color: white;
            }
        """)

        # Lista książek
        self.books_list = QListView()
        self.books_list.clicked.connect(self.select_book)

        # Przyciski
        self.add_book_button = QPushButton("Dodaj książkę")
        self.add_book_button.clicked.connect(self.open_add_book)

        self.edit_book_button = QPushButton("Edytuj książkę")
        self.edit_book_button.clicked.connect(self.edit_selected_book)

        self.delete_book_button = QPushButton("Usuń książkę")
        self.delete_book_button.clicked.connect(self.delete_selected_book)

        self.logout_button = QPushButton("Wyloguj")
        self.logout_button.clicked.connect(self.logout_user)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.add_book_button)
        layout.addWidget(self.edit_book_button)
        layout.addWidget(self.delete_book_button)
        layout.addWidget(self.logout_button)
        layout.addWidget(self.books_list)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.books = []
        self.selected_index = None
        self.update_books_list()

    def update_books_list(self):
        self.books = get_books()
        titles = [book[1] for book in self.books]  # book[1] to tytuł
        model = QStringListModel(titles)
        self.books_list.setModel(model)

    def open_add_book(self):
        dialog = AddBookDialog()
        if dialog.exec_():
            self.update_books_list()

    def select_book(self, index):
        self.selected_index = index.row()

    def delete_selected_book(self):
        if self.selected_index is None:
            QMessageBox.warning(self, "Błąd", "Nie wybrano żadnej książki.")
            return

        book = self.books[self.selected_index]
        confirm = QMessageBox.question(self, "Potwierdź", f"Czy na pewno chcesz usunąć '{book[1]}'?",
                                       QMessageBox.Yes | QMessageBox.No)
        if confirm == QMessageBox.Yes:
            delete_book(book[0])
            QMessageBox.information(self, "Usunięto", "Książka została usunięta.")
            self.update_books_list()
            self.selected_index = None

    def edit_selected_book(self):
        if self.selected_index is None:
            QMessageBox.warning(self, "Błąd", "Nie wybrano żadnej książki.")
            return

        book = self.books[self.selected_index]
        dialog = EditBookDialog(book)
        if dialog.exec_():
            self.update_books_list()

    def logout_user(self):
        try:
            os.remove("remember_me.txt")
        except FileNotFoundError:
            pass

        self.close()
        login = LoginWindow()
        if login.exec_():
            self.__init__()
            self.show()
